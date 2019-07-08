from mne.time_frequency import psd_welch as pw
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mne

def openData(name):
    df = pd.read_csv(name, skiprows=6, names=['index', 'PO3', 'PO4', 'P8', 'O1', 'O2', 'P7', '7', '8', 'x', 'y', 'z', 'tempo'])
    df = df.drop(['index','7', '8', 'x', 'y', 'z', 'tempo'], axis=1)
    dataLen = len(df)
    return dataLen, df.transpose()

def plotGraphic(averageFrequency):
    ASD = averageFrequency
    y= ASD.keys()
    x= ASD.values()
    plt.bar(y, x)
    # plt.axis((x1, x2, 0, 20000))    
    plt.pause(1.00)
    plt.clf()

def getRaw(df):
    ch_types = ['eeg'] * 6
    ch_names = ['PO3', 'PO4', 'P8', 'O1', 'O2', 'P7']
    info = mne.create_info(ch_names= ch_names, sfreq=256 , ch_types=ch_types)
    raw = mne.io.RawArray(df,info)
    montage = mne.channels.read_montage('standard_1020')
    raw.set_montage(montage)
    return raw

def preprocessing(raw):
    raw.notch_filter(np.arange(60, 121, 60), fir_design='firwin') #aplica filtro notch
    raw.filter(5,50) #aplica filtro passa-faixa
    raw.filter(5,50) #aplica filtro passa-faixa
    raw.filter(5,50) #aplica filtro passa-faixa
    return raw

def work(raw, dataLen, bufferSize = 3):
    frequency = {
        'alfa'  : {},
        'beta'  : {},
        'gamma' : {},
        'theta' : {}
    }

    interval = {
        'alfa'  : {'init': 8, 'end': 12},
        'gamma' : {'init': 25, 'end': 100},
        'beta'  : {'init': 12, 'end': 30},
        'theta' : {'init': 5, 'end': 7}
    }

    for i in range(0, int(dataLen/256)):
        #realiza a janela de deslocamento (1 seg)
        psds, freqs = pw(raw,fmin=0,fmax=128,tmin=i,tmax=i+bufferSize)

        #recebe a maior média(dos 6 eletrodos) de cada frequencia em seu intervalo
        for canal in frequency.keys():
            frequency[canal] = max(np.mean(psds[:,interval[canal]['init']:interval[canal]['end']],axis=1))
            
        #verifica se a media do alfa é o maior
        if(frequency['alfa'] == max(frequency.values())):
            plotGraphic(frequency)        
            #hordena a medias
            values = sorted(list(frequency.values()) , reverse = True)
            #retorna a diferença do alfa sobre o segundo maior em escala de (0..100)
            powerAlfa = 100*(values[0] - values[1])/frequency['alfa']
            print(powerAlfa)

dataLen, df = openData("entrada.csv")
raw = preprocessing(getRaw(df))
work(raw, dataLen, bufferSize = 5)