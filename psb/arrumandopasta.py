import os
import shutil

def processaArquivo(nomepasta, file):

    for i in range(0, 3):
        file.readline()

    return file.readline().replace('#', '').split(',')[0].strip()

def copia(arquivos, nomepasta):

    for arquivo in arquivos:
        try:
            shutil.move(arquivo, nomepasta)
        except (FileExistsError, shutil.Error):
            return

def criaPastas(nomepasta, s1, s2, s2no):
    try:
        os.makedirs(nomepasta + 's1')
        os.makedirs(nomepasta + 's2')
        os.makedirs(nomepasta + 's2no')
    except FileExistsError:
        pass

    copia(s1, nomepasta + 's1/')
    copia(s2, nomepasta + 's2/')
    copia(s2no, nomepasta + 's2no/')

def organiza(nomepasta):
    s1 = []
    s2 = []
    s2no = []

    files = os.listdir(nomepasta)

    for fileName in files:
        if os.path.isdir(nomepasta + fileName):
            continue
        else:
            file = open(nomepasta + fileName)

        resp = processaArquivo(nomepasta, file)

        if 'S1' in resp:
            s1.append(nomepasta + fileName)
        else:
            if 'no' in resp:
                s2no.append(nomepasta + fileName)
            else:
                s2.append(nomepasta + fileName)

    return s1, s2, s2no

def listSubPaths(path):

    subPaths = []
    for subPath in os.listdir(path):
        if os.path.isdir(path + subPath):
            subPaths.append(path + subPath + '/')

    return subPaths



path1 = 'large_test/'
for path2 in listSubPaths('dataset/' + path1):
    s1, s2, s2no = organiza(path2)

    if s1 and s2 and s2no:
        criaPastas(path2, s1, s2, s2no)
