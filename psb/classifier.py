from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PowerTransformer

def extrai(fileName):
    x, y = [], []
    file = open(fileName)

    # pre processing POWER
    power = PowerTransformer()

    for line in file.readlines():
        line = line.replace(';\n', '').split(';')
        y.append(line.pop())
        x.append(line)

    return power.fit_transform(np.array(x)), np.array(y)

def printResult(train_values, test_values, acertos, k=False):
    if k:
        print('KNN:', k)
    else:
        print('SVM:')

    print('Total de treinamento: %d' % len(train_values))
    print('Total de testes: %d' % (len(test_values)))
    print('Total de acertos: %d' % acertos)
    print('Porcentagem de acertos: %.2f%%' % (100 * acertos / (len(test_values))))
    print()

def knn(k):
    global train_values
    global test_values

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_values, train_label)

    rotulos_previstos = knn.predict(test_values)
    acertos, indice_rotulo = 0, 0
    for i in range(0, len(test_values)):
        if rotulos_previstos[indice_rotulo] == test_label[i]:
            acertos += 1
        indice_rotulo += 1

    printResult(train_values, test_values, acertos, k)

def svmPSB():
    global train_values
    global test_values

    xTrain = train_values
    xTest = test_values

    clf = svm.SVC(kernel='linear')
    clf.fit(xTrain, train_label)
    rotulos_previstos = clf.predict(test_values)    

    # Contabilizar acertos para os dados de teste
    acertos, indice_rotulo = 0, 0
    for i in range(0, len(test_values)):
        if rotulos_previstos[indice_rotulo] == test_label[i]:
            acertos += 1
        indice_rotulo += 1

    printResult(train_values, test_values, acertos)

for s in ['s1', 's2', 's2no']:

    print("Category: {}".format(s.upper()))

    fileNameTest = './dataset/test_{}.csv'.format(s)
    fileNameTrain = './dataset/train_{}.csv'.format(s)

    test_values, test_label = extrai(fileNameTest)
    train_values, train_label = extrai(fileNameTrain)

    knn(9)
    knn(7)
    knn(5)

    svmPSB()