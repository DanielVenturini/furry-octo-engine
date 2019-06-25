import pandas as pd
import mne
from mne.time_frequency import psd_welch as pw
import numpy as np

# bandpass mais vezes(fmin, fmax)
# tmin, tmax deslizamento de janela

# usar
# from.mne.decoding import PSDEstimator
# psd = PSDEstimator(sfreq,fmin = 0,fmax = 128)
# x= psd.transform(raw) 
# FilterEstimator

#usar filtro passaFaixa

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

def openData(name):
    df = pd.read_csv(name, skiprows=6, names=['index', 'PO3', 'PO4', 'P8', 'O1', 'O2', 'P7', '7', '8', 'x', 'y', 'z', 'tempo'])
    df = df.drop(['index','7', '8', 'x', 'y', 'z', 'tempo'], axis=1)
    return df.transpose()

df = openData("entrada.csv")
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
bufferSize = 3
for i in range(0, len(df)/256):
    psds, freqs = pw(raw,fmin=0,fmax=128,tmin=i,tmax=i+bufferSize)#arrumar aki buffer
    print(ps[1:4])
    print(ps[5:7])
    print(ps[8:12])
    print(ps[25:100])
    print(ps[12:30])
    print()
    print()
    print()

# for ps in psds:
    
    
# print(psds[:][8:12])#0 ah 5
#usar psd_welch

# notch
# 5,50 passa faixa