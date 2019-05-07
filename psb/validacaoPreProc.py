import os
import json
from teste import getSumElectodes, plotaGrafico
from arrumandopasta import listSubPaths

def separaAlcolicosControle(pwd):
    alcolico = []
    controle = []

    for p in pwd:
        if('a' in p.split('/')[2]):
            alcolico.append(p) 
        else:
            controle.append(p)

    return [alcolico, controle]


pathS = ['s2no/']
path1 = 'large_train/'
for path_s in pathS:

    pwds = listSubPaths('dataset/' + path1)
    pwds = separaAlcolicosControle(pwds)
    qtd = len(pwds[0])

    for pwd in pwds:
        electrodesFinal = {}

        for path2 in pwd:
            electrodes = getSumElectodes(path2 + path_s)

            for key in list(electrodes.keys()):
                for pos, value in enumerate(electrodes[key]):
                    try:
                        value2 = electrodesFinal[key][pos]
                    except KeyError:
                        electrodesFinal[key] = [0]*256
                        value2 = 0

                    electrodesFinal[key][pos] = value2 + (value/qtd)

        plotaGrafico(electrodesFinal)
# json.dump(electrodesFinal, open('resp.json', 'w'))