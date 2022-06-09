from ast import keyword
import numpy as np
import pytesseract
import PIL
from PIL import Image
import re
import string

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

        ##TODO 
    
    else:
        return "ERROR - formula unknow"




def salva_imagem(img,url,nome):
    with open(url+nome, 'wb') as f:
        img.save(f)



def main_loop(imagem):
    img = Image.open(imagem)
    texto = get_text(img)
    texto = clean_txt(texto)

    for group in config.keys():
        formula = config[group]['formula']
        keyword = config[group]['keywords']

        if formula == 'exact':
            #TO DO
            
        else:
            for key in keyword:
                for word in texto:
                    result = string_distance(key, word, formula)
                    if result > config[group]['threshold']:
                        salva_imagem(img,config[group]['folder'],imagem)


    