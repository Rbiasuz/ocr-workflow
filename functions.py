from ast import keyword
import numpy as np
#import pytesseract
import PIL
from PIL import Image
import re
import string
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def get_text(image):
    """ 
    Recebe uma imagem e retorna o texto presente na mesma (string)
    """

    im = Image.open(image)
    txt = pytesseract.image_to_string(im)
    txt = re.sub(' +', ' ', txt)
    txt = txt.replace('\n','')
    txt = txt.lower()
    txt = ' '.join([word for word in txt.split() if word not in string.punctuation])
    return txt


def clean_txt(txt):
    """ 
    Recebe uma string vinda de um OCR e organiza em uma lista removendo "S" do final de cada palavra
    """

    txt = txt.split()
    txt = [i.strip('s') for i in txt]

    return txt


def string_distance(x,y, formula):
    """ 
    Recebe duas strings e calcula a distância entre elas
    """

    if formula == 'jaccard':
        """
        Jaccard similarity
        """

        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        return intersection_cardinality/float(union_cardinality)
    
    elif formula == 'cosine':
        """
        Cosine similarity
        """
        l1 =[];l2 =[]

        # tokenization
        X_set = word_tokenize(x)
        Y_set = word_tokenize(y)

        # form a set containing keywords of both strings
        rvector = X_set.union(Y_set)
        for w in rvector:
            if w in X_set: l1.append(1) # create a vector
            else: l1.append(0)
            if w in Y_set: l2.append(1)
            else: l2.append(0)
        c = 0

        # cosine formula
        for i in range(len(rvector)):
            c+= l1[i]*l2[i]
        cosine = c / float((sum(l1)*sum(l2))**0.5)

        return cosine

    elif formula == 'cosine2':

        rvector = x.union(y)

        vectorizer = CountVectorizer(rvector)
        vectorizer.fit(rvector)
        vectors = vectorizer.transform(rvector).toarray()

        return cosine_similarity(vectors[0],vectors[1])[0][0]

    elif formula == 'exact':

        if x == y:
            vreturn =100
        else:
            vreturn =0

        return vreturn

    else:
        return "ERROR - formula unknow"

def salva_imagem(img,url,nome):
    with open(url+nome, 'wb') as f:
        img.save(f)


    