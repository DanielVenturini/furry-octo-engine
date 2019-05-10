from sklearn.neighbors import KNeighborsClassifier

def extrai(fileName):
    x, y = [], []
    file = open(fileName)

    for line in file.readlines():
        line = line.replace(';\n', '').split(';')
        y.append(line.pop())
        x.append(line)

    return x, y

fileNameTest = './dataset/test_s2no.csv'
fileNameTrain = './dataset/train_s2no.csv'

test_values, test_label = extrai(fileNameTest)
train_values, train_label = extrai(fileNameTrain)

# Chamar a função do skLearn para aplicar o k-NN com K = 13
knn = KNeighborsClassifier(n_neighbors=9)
# Ajustar o modelo usando "x_test" como dados de treinamento e "y_test" como valores-alvo
knn.fit(train_values, train_label)
# Previsão dos rótulos das classes para o restante da base de dados
rotulos_previstos = knn.predict(test_values)

# Contabilizar acertos para os dados de teste
acertos, indice_rotulo = 0, 0
for i in range(0, len(test_values)):
	if rotulos_previstos[indice_rotulo] == test_label[i]:
		acertos += 1
	indice_rotulo += 1

print('Total de treinamento: %d' % len(train_values))
print('Total de testes: %d' % (len(test_values)))
print('Total de acertos: %d' % acertos)
print('Porcentagem de acertos: %.2f%%' % (100 * acertos / (len(test_values))))