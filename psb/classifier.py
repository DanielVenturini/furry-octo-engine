from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

def extrai(fileName):
    x, y = [], []
    file = open(fileName)

    for line in file.readlines():
        line = line.replace(';\n', '').split(';')
        y.append(line.pop())
        x.append(line)

    return x, y

fileNameTest = './dataset/test_full.csv'
fileNameTrain = './dataset/train_full.csv'

test_values, test_label = extrai(fileNameTest)
train_values, train_label = extrai(fileNameTrain)

def knn(k):
    global train_values
    global test_values
    # Chamar a função do skLearn para aplicar o k-NN com K = 13
    knn = KNeighborsClassifier(n_neighbors=k)
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

    print('K:', k)
    print('Total de treinamento: %d' % len(train_values))
    print('Total de testes: %d' % (len(test_values)))
    print('Total de acertos: %d' % acertos)
    print('Porcentagem de acertos: %.2f%%' % (100 * acertos / (len(test_values))))

def svmPSB():
    global train_values
    global test_values

    clf = svm.SVC(gamma='scale')
    clf.fit(train_values, train_label)

    rotulos_previstos = clf.predict(test_values)

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

'''
knn(5)
knn(3)
knn(1)
'''

#svmPSB()