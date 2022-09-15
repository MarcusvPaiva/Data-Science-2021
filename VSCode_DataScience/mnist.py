#matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
#data_path = "/home/pulgatti/Área de Trabalho/Dropbox/Opet/BI e DW/"
#train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
test_data = np.loadtxt("mnist_test.csv", delimiter=",")
#print(test_data[:10])


#Realiza ajustes nas imagens
fac = 0.99 / 255
#train_imgs = np.asfarray(train_data[:, 1:]) * fac + 0.01
test_imgs = np.asfarray(test_data[:, 1:]) * fac + 0.01
#
#train_labels = np.asfarray(train_data[:, :1])
test_labels = np.asfarray(test_data[:, :1])
'''
for i in range(20):
    img = test_imgs[i].reshape((28,28))
    plt.imshow(img, cmap="Greys")
    plt.show()
'''
def array_definition(imagem):
    linha  = imagem.shape[0] 
    coluna = imagem.shape[1] 
    transicao = [0] * ((linha + coluna ) + 1)

    for i in range(0,linha):  # este loop extrai as características das linhas
        for j in range(0,coluna):
            if imagem[i, j-1] !=  imagem[i, j]:
                transicao[i] = transicao[i] + 1

    for i in range(0,coluna):  # este loop extrai as características das colunas
        for j in range(0,linha):
            if imagem[j-1, i] !=  imagem[j, i]:
                transicao[linha + i] = transicao[linha + i] + 1
    return transicao 

f = open("aula.arff", "w")
f.write("@relation digits\n")
for i in range(1, 57):
    f.write("@attribute " + str(i) +" numeric\n")
f.write("@attribute class {0,1,2,3,4,5,6,7,8,9}\n\n")

f.write("@DATA\n")

transicoes = [0] * 57  # inicializa o array com 0 (zero) antes de entrar no loop
for i in range(len(test_data)):
    img = test_imgs[i].reshape((28,28))
    transicoes = array_definition(img)
    transicoes[56] = int(test_labels[i])
    #print()
    #print("Transições da imagem: "+str(i+1))
    #print(transicoes)
    print(*transicoes, sep=',' , file = f)

f.close()
print("Acabou")
#f=open(data_path+"aula.arff","r")
#print(f.read())