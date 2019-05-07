import os
from teste import getSumElectodes

mainPath = 'dataset/'
secondPath = 'large_train/'

pathsS = ['s1', 's2', 's2no']
controle = []

for path in os.listdir(mainPath + secondPath):
    if os.path.isfile(mainPath + secondPath + path):
        continue

    path += '/'

    for s in pathsS:
        s += '/'
        media = getSumElectodes(mainPath + secondPath + path + s)

        if 'a' in path:
            mainPath + 'a' + s + '.csv'
        else:
            mainPath + 'c' + s + '.csv'