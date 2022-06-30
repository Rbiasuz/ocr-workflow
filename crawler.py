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
        ##move arq
        shutil.move(mainfolder+"/"+file, backupfolder+"/"+file)






#while true para intervalo de tempo

#loop os list dir

#


