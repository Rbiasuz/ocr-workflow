import numpy as np
import pytesseract
import PIL
import re
import string

def get_text(image):
    """ 
    Recebe uma imagem e retorna o texto presente na mesma (string)
    """
    im = PIL.Image.open(image)
    txt = pytesseract.image_to_string(im)
    txt = re.sub(' +', ' ', txt)
    txt = txt.replace('\n','')
    txt = txt.lower()
    txt = ' '.join([word for word in txt.split() if word not in string.punctuation])

    return txt


def string_distance(x,y):
    """ 
    Recebe duas strings e calcula a distância entre elas
    """

    """
    Jaccard similarity
    """

    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)

    return distance

def salva_imagem(img,url):

    im = PIL.Image.open(img)

    with open(url, 'w') as f:
        im.save(f)

def identifica_img_grupo(img):

    def convert(lst):
        return (lst[0].split())

    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    def check(email):
        if(re.search(regex_email,email)):
            return True
        else:
            return False

    texto = get_text(img)

    """
    Verifica se tem emails
    """
    lista_palavras = convert(lista_texto)

    for word in lista_palavras:
        print(word)
        if check(word):
            salva_imagem(img,'/assets/Grupo_1/')
            break



