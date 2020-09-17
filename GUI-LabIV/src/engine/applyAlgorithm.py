import numpy as np # linear algebra
import cv2
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import os
import imageio
import sys

argumentos = sys.argv[1]

model = argumentos

# Use the folder created by createDatbase algorithm
# testing my own data
folderName = "Teste"

print('ENTROU APPLY JS')

pathFolder = r'C:\\Users\\diogo\\OneDrive\\Área de Trabalho\\ENGENHARIA DE SISTEMAS\\10º PERÍODO\\LAB. IV\\Projeto-LABIV' + folderName
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


# Predicting my data
myFace_predict = model.predict(myDATA)

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
figure = plt.figure(figsize=(20, 8))
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
plt.figure(figsize=(12,7))
ax2 = sns.barplot(x = labels, y = dados['Percentual'], hue = (dados['Percentual'] * 100).round(2) )
ax2.set_ylim((0, 1))
ax2.set_title('Média das tendências étnicas calculadas - {} amostras'.format(len(myDATA)), fontsize = 20)
ax2.set_xlabel('Raças/Etnias', fontsize = 14)
ax2.set_ylabel('Porcentagem', fontsize = 14)
plt.legend( bbox_to_anchor = (1.08, 0.8), loc = 'center' )
plt.show()