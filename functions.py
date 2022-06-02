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


def string_distance(str1,str2):
    """ 
    Recebe duas strings e calcula a distância entre elas
    """

    #TODO

    return distance
