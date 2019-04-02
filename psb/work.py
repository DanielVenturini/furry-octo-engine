import mne
import numpy as np
from re import search

# identificando pastas
folders = {
    'small': 'dataset/small',
    'large_train': 'dataset/large_train',
    'large_test': 'dataset/large_test',
    'full': 'dataset/full',
}

eletrodo = 'O2'

file = open(folders['small'] + '/a_1_co2a0000364/co2a0000364.rd.000')
fileOutput = open('result.json', 'w')

fileOutput.write('[')

for pos, line in enumerate(file.readlines()):
	if line.startswith('#'):
		continue

	line = line.split()
	if line[1] == eletrodo:
		fileOutput.write(line[3] + ',')

fileOutput.write(']')