import os
from teste import getSumElectodes, toCSV, plotaGrafico, semMedia
from mne.time_frequency import psd_welch as pw
import numpy

def person(pathName):
    if 'a' in pathName:
        return 'alcohol'
    else:
        return 'control'

categorys = ['train', 'test']
mainPath = 'dataset/'

pathsS = ['s1', 's2', 's2no']

for category in categorys:
    secondPath = 'large_{}/'.format(category)
    for s in pathsS:
        open(mainPath + category + '_' + s.replace('/', '') + '.csv', 'w').close()

    for path in os.listdir(mainPath + secondPath):
        if os.path.isfile(mainPath + secondPath + path):
            continue

        path += '/'

        for s in pathsS:
            s += '/'
            sMedia = semMedia(mainPath + secondPath + path + s)

            for sM in sMedia:
                psds, freqs = pw(plotaGrafico(sM))

                #toCSV(psds[int(len(psds)/2):], mainPath + category + '_' + s.replace('/', '') + '.csv', person(path), 'a')            
                toCSV(psds, mainPath + category + '_' + s.replace('/', '') + '.csv', person(path), 'a')            

            # media = getSumElectodes(mainPath + secondPath + path + s)
            # psds, freqs = pw(plotaGrafico(media))
            # toCSV(psds[int(len(psds)/2):], mainPath + category + '_' + s.replace('/', '') + '.csv', person(path), 'a')