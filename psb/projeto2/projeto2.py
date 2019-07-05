import pandas as pd
import mne
import sys
from mne.time_frequency import psd_welch as pw
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from sklearn.preprocessing import MinMaxScaler

def testData(df):
    lista = []
    lista2 = []
    anterior = 0
    for pos in list(df['index']):
        if(pos < anterior):
            lista.append(lista2)
            lista2 = []
        anterior = pos
        lista2.append(pos)
    lista.append(lista2)

    dc = {}
    
    for x in lista:
        dc[len(x)] = 0
    print(dc.keys())        

def millions(x, pos):
    'The two args are the value and tick position'
    return '$%1.1fM' % (x * 1e-6)

def openData(name):
    df = pd.read_csv(name, skiprows=6, names=['index', 'PO3', 'PO4', 'P8', 'O1', 'O2', 'P7', '7', '8', 'x', 'y', 'z', 'tempo'])
    df = df.drop(['index','7', '8', 'x', 'y', 'z', 'tempo'], axis=1)
    dataLen = len(df)
    return dataLen, df.transpose()

def get_min_max(media):
    min_value = sys.maxsize
    max_value = 0

    for l in media:
        scaler = MinMaxScaler()
        scaler.fit(np.array(l).reshape(-1, 1))
        max_value = scaler.data_max_
        min_value = scaler.data_min_

dataLen, df = openData("entrada.csv")
ch_types = ['eeg'] * 6
ch_names = ['PO3', 'PO4', 'P8', 'O1', 'O2', 'P7']

info = mne.create_info(ch_names= ch_names, sfreq=256 , ch_types=ch_types)
raw = mne.io.RawArray(df,info)
montage = mne.channels.read_montage('standard_1020')
raw.set_montage(montage)

raw.notch_filter(np.arange(60, 121, 60), fir_design='firwin')

raw.filter(5,50)
raw.filter(5,50)
raw.filter(5,50)
#raw.plot_psd()

frequencias = {
    'alfa'  : {},
    'beta'  : {},
    'gamma' : {},
    'theta' : {}
}

intervalos = {
    'alfa'  : {'init': 8, 'end': 12},
    'gamma' : {'init': 25, 'end': 100},
    'beta'  : {'init': 12, 'end': 30},
    'theta' : {'init': 5, 'end': 7}
}

bufferSize = 3
for i in range(0, int(dataLen/256)):
    psds, freqs = pw(raw,fmin=5,fmax=55,tmin=i,tmax=i+bufferSize)

    for canal in frequencias.keys():
        frequencias[canal] = max(np.mean(psds[:,intervalos[canal]['init']:intervalos[canal]['end']],axis=0))
    
    # print(max(np.mean(psds[:,8:12], axis=0)))
    
    medeiaMaior = sorted(frequencias.items(), key=lambda pos : pos[1], reverse= True)
    if(medeiaMaior[0][0] == 'alfa'):
        print(medeiaMaior[0][1]) 
        
    #x = np.arange(4)
    ASD= dict(medeiaMaior)
    x=ASD.keys()
    y=ASD.values()
    print(x)
    print(y)
    plt.bar(y, x)
    # plt.xticks(x, ('alfa', 'beta', 'gamma', 'theta'))
    # x1,x2,y1,y2 = plt.axis()
    # plt.axis((x1, x2, 0, 20000))
    
    # plt.show()
    plt.pause(1.00)
    plt.clf()