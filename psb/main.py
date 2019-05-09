import os
from teste import getSumElectodes, toCSV, plotaGrafico
from mne.time_frequency import psd_welch as pw

def person(pathName):
    if 'a' in pathName:
        return 'alcohol'
    else:
        return 'control'

writeMode = 'w'
category = 'test'
mainPath = 'dataset/'
secondPath = 'large_{}/'.format(category)

pathsS = ['s1', 's2', 's2no']

for path in os.listdir(mainPath + secondPath):
    if os.path.isfile(mainPath + secondPath + path):
        continue

    path += '/'

    for s in pathsS:
        s += '/'
        media = getSumElectodes(mainPath + secondPath + path + s)
        psds, freqs = pw(plotaGrafico(media))
        toCSV(psds[int(len(psds)/2):], mainPath + category + '_' + s.replace('/', '') + '.csv', person(path), writeMode)

    writeMode = 'a'