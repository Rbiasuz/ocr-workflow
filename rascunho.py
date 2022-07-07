for word in texto.split():
    for key in keyword:
        p = string_distance(word,key,formula)
        print(p,word,key)

        if p >= int(threshold):
            salva_imagem(mainfolder+"/"+file,foldersalvar,file):##move arq
            achou = 1
            break