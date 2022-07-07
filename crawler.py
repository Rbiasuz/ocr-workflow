import os
import json
import time
import shutil
from functions import *

with open('config', 'r') as f:
    config = json.load(f)

mainfolder = config['crawler']['mainfolder'][0]
backupfolder = config['crawler']['backupfolder'][0]
fileextennsion = config['crawler']['type'][0]
timedelay = config['crawler']['interval'][0]
targets = list(config.keys())
targets.remove('crawler')


def stringToList(string):
    listRes = list(string.split(","))
    return listRes


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            ext = os.path.splitext(file)[-1].lower()
            extensoes = stringToList(fileextennsion)
            if ext in extensoes:
                yield file



while True:
    time.sleep(int(timedelay))
    for file in files(mainfolder):
        achou = 0
        try:
            texto = get_text(mainfolder+"/"+file)
            for target in targets:
                keyword = config[target]['keywords']
                formula = config[target]['formula']
                threshold = config[target]['threshold']
                foldersalvar = config[target]['folder']

                for word in texto.split():
                    for key in keyword:
                        p = string_distance(word,key,formula)

                        if p >= int(threshold):
                            salva_imagem(mainfolder+"/"+file,foldersalvar,file):##move arq
                            achou = 1
                            break
        except:
            shutil.move(mainfolder+"/"+file, backupfolder+"/"+file)
            print('Erro ao processar arquivo '+file)

        if achou = 0:
            shutil.move(mainfolder+"/"+file, backupfolder+"/"+file)
        else:
            os.remove(mainfolder+"/"+file)
