import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import cv2
import matplotlib.pyplot as plt
import os
import seaborn as sns
# from PIL import Image
from os import listdir
from os.path import isfile, join


from random import shuffle
import keras

import imageio
# from collections import Counter
# from sklearn.decomposition import PCA
# from sklearn.manifold import TSNE
# import tensorflow as tf
# from keras.models import Sequential
import sys

print('ENTROU TRAIN DATA ANTES DO PROPS')
print(sys.argv[1])
props = sys.argv[1]
print('ENTROU TRAIN DATA PASSOU DO PROPS')

def treinaModelo():

    # Go to the directory taht has the training database
    # ***** It is needed to write the relative directory to catch teh database *****
    pathDatabase = r"C:\\Users\\diogo\\OneDrive\\Área de Trabalho\\ENGENHARIA DE SISTEMAS\\10º PERÍODO\\LAB. IV\\UTKFace\\UTKFace"
    # pathDatabase = r+pastaTreinamento

    os.chdir(pathDatabase)

    # Define dir
    onlyfiles = os.listdir()

    shuffle(onlyfiles)

    # Classes known - To the original database
    categories = ['0','1','2', '3', '4']
    race = []

    # Captura as classes do arquivo
    print("ANTES DO FOR")
    
    for i in onlyfiles:
        str_split = i.split('_')[2]
        if str_split in categories:
            race.append(str_split)
    print("PASSOU DO FOR")
    # Analyze data
    race_pd = pd.DataFrame(race, columns = ['Coluna 1'])
    race_pd['Coluna 1'].value_counts().index #Show the existing labels

    # Here the adaptation happens to get close on what we have in Brazil
    classes = []
    for i in race:
        try:
            i = int(i)
            if i == 4: # Convert class 4 in 3
                i = 3
            classes.append(i)
        except:
            pass
        
    # Define labels
    labels =["Branco",  # index 0
            "Preto",      # index 1
            "Ásiatico",  # index 2
            "Pardo"      # index 3
            ]

    # After conversion, analyze data again
    classes_pd = pd.DataFrame(classes, columns = ['Coluna 1'])
    classes_pd['Coluna 1'].value_counts()

    # Plot the difference between the classes
    plt.figure(figsize=(12,7))
    ax2 = sns.barplot(x = labels , y = classes_pd['Coluna 1'].value_counts()[:] , hue = classes_pd['Coluna 1'].value_counts() )
    ax2.set_title('Distribuição de classes na base de dados ', fontsize = 20)
    ax2.set_xlabel('Raças/Etnias', fontsize = 14)
    ax2.set_ylabel('Quantidade', fontsize = 14)
    plt.legend( bbox_to_anchor = (1.08, 0.8), loc = 'center' )
    plt.show()

    # Import image lib manipulator 
    import imageio

    X_data =[]
    size_image = 32

    for file in onlyfiles:

        # Filtering data
        str_split = file.split('_')[2]
        if str_split in categories:
            face = imageio.imread(file)
            face = cv2.resize(face, (size_image, size_image) )
            X_data.append(face)
            
    # Transform in a single dimensional input
    X = np.squeeze(X_data)

    # Normalize data
    X = X/255.0

    # Make "Classes" a numpy array
    classes = np.array(classes)

    # Separate data to train and test
    from sklearn.model_selection import train_test_split

    tamanho = min(len(X), len(classes))
    x_train, x_test, y_train, y_test = train_test_split(X[:tamanho], classes[:tamanho], test_size  = 0.33, random_state= 42)

    # Start to use Keras 
    import tensorflow as tf

    model = keras.Sequential([
        keras.layers.Flatten( input_shape = (size_image, size_image, 3) ),
        keras.layers.Dense(128, activation = tf.nn.relu),
        keras.layers.Dense(5, activation = tf.nn.softmax)
    ])

    # Model compile
    model.compile(loss='sparse_categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])

    # Model fit
    model.fit(x_train,
            y_train,
            epochs=10
        )

    # Evaluate the model on test set
    score = model.evaluate(x_test, y_test)

    # Print test accuracy 
    print('\n', 'Test accuracy:', score[1])
    
    model.save("./../../Projeto-LAB_IV/modelo")
    aplicaModelo()
    # aplicaModelo(model)


def aplicaModelo():
    # Use the folder created by createDatbase algorithm
    # testing my own data
    folderName = "Teste"

    print('ENTROU APPLY JS')
    print(os.getcwd())
    
    modelo = keras.models.load_model("../modelo")
    
    pathFolder = r"C:\\Users\\diogo\\OneDrive\\Área de Trabalho\\ENGENHARIA DE SISTEMAS\\10º PERÍODO\\LAB. IV\\Projeto-LAB_IV\\GUI-LabIV\\{0}".format(folderName)
    os.chdir(pathFolder) # changing directory
    onlyimage = os.listdir()

    size_image = 32

    # Define labels
    labels =["Branco",  # index 0
            "Preto",      # index 1
            "Ásiatico",  # index 2
            "Pardo"      # index 3
            ]

    # Creating the input to the model
    myDATA =[]
    for file in onlyimage:
        face = imageio.imread(file)
        face = cv2.resize(face, (size_image, size_image) )
        myDATA.append(face)

    myDATA = np.squeeze(myDATA)

    # Normalize data
    myDATA = myDATA/255.0

    print('E AQUI')

    # Predicting my data
    myFace_predict = modelo.predict(myDATA)

    # print(myFace_predict[0])

    # Create PARDO class (Indian + Latino percents)
    myFace_hat = myFace_predict[:, :4]
    myFace_hat[:, 3] = myFace_predict[:, 3] + myFace_predict[:, 4] 

    # Join data - mean from individually calculus 
    dados = [ myFace_hat[:,0].mean(), myFace_hat[:,1].mean(), myFace_hat[:,2].mean(), myFace_hat[:,3].mean()]


    # Making a dataframe from data
    dados = pd.DataFrame(dados, columns = ['Percentual'] ,index= labels)

    #Show data
    print(dados['Percentual'])
    print('\n')

    # Show the sum of percentuals, it must be equal to 1
    print('Soma = {}'.format(sum(dados['Percentual']) ))

    # What i classify me
    myLabel = 0 # Branco

    # Plot a random sample of 30 test images, their predicted labels and ground truth
    figure = plt.figure(figsize=(12, 8))
    plt.tight_layout()

    random_number = np.random.choice(myDATA.shape[0], size=15, replace=False)
    for i, index in enumerate( random_number ):
        ax = figure.add_subplot(3, 5, i + 1, xticks=[], yticks=[])
        # Display each image
        ax.imshow(np.squeeze(myDATA[index]))
        predict_index = np.argmax(myFace_hat[index])

        
        # Set the title for each image
        ax.set_title("B:{}%  Pt:{}%  A:{}%  Pr:{}%".format( (myFace_hat[index][0] * 100).round(1), (myFace_hat[index][1] * 100).round(1), 
                                    (myFace_hat[index][2] * 100).round(1), (myFace_hat[index][3] * 100).round(1)),
                                    color=("green" if predict_index == myLabel else "red"))
    plt.show()


    # Plot percents of means from folder created
    plt.figure(figsize=(12,8))
    ax2 = sns.barplot(x = labels, y = dados['Percentual'], hue = (dados['Percentual'] * 100).round(2) )
    ax2.set_ylim((0, 1))
    ax2.set_title('Média das tendências étnicas calculadas - {} amostras'.format(len(myDATA)), fontsize = 20)
    ax2.set_xlabel('Raças/Etnias', fontsize = 14)
    ax2.set_ylabel('Porcentagem', fontsize = 14)
    plt.legend( bbox_to_anchor = (1.08, 0.8), loc = 'center' )
    plt.show()



#função principal da aplicação
def main():
    
    print('TRAIN DATA NO MAIN')
    if (props == 'true'):
        print('TRAIN DATA NO TREINO')
        # treinaModelo()
        aplicaModelo()


if __name__ == "__main__":
    main()