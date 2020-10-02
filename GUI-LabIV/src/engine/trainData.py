import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import cv2
import matplotlib.pyplot as plt
import os
import seaborn as sns
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


def treinaModelo(caminhoPastaTreinamento, caminhoPastaSalvaModelo):

    # Go to the directory taht has the training database
    # ***** It is needed to write the relative directory to catch teh database *****
    # pathDatabase = r"C:\\Users\\diogo\\OneDrive\\Área de Trabalho\\ENGENHARIA DE SISTEMAS\\10º PERÍODO\\LAB. IV\\UTKFace\\UTKFace"
    pathDatabase = caminhoPastaTreinamento
    print("AGARROU AQUI")
    os.chdir(pathDatabase)

    print("PASSOU AQUI?")
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
            "Negro",      # index 1
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
    print('\n', 'Acurácia:', score[1])
    
    model.save(caminhoPastaSalvaModelo + "modelo")
    print('OK')

def main():
    print('TRAIN DATA NO MAIN')
    pastaTreinamento = sys.argv[1]
    pastaSalvaModelo = sys.argv[2]
    treinaModelo(pastaTreinamento, pastaSalvaModelo)

if __name__ == "__main__":
    main()