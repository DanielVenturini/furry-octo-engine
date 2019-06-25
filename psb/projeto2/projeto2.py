import pandas as pd
import mne
from mne.time_frequency import psd_welch as pw

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

raw.filter(5,50)
raw.filter(5,50)
raw.filter(5,50)

#raw.plot_psd()
psds, freqs = pw(raw,fmin=0,fmax=128,tmin=0,tmax=3)#arrumar aki buffer
print(psds[0][8:12])#0 ah 5
#usar psd_welch
