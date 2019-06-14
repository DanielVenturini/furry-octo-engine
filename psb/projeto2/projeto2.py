import pandas as pd

df = pd.read_csv("file1.csv", skiprows=6, names=['index','PO3','PO4','P8','O1','O2','P7','7','8','x','y','z','tempo'])
df.drop(['7', '8','x', 'y', 'z', 'tempo'], axis=1)

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
    try:
        dc[len(x)] = 10
    except:
        pass

print(dc.keys())

        



