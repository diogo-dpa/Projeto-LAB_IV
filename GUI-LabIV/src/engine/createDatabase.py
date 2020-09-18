
# Importa as bibliotecas 
import os
import sys
import numpy as np
import cv2

# Carrega os nomes no arquivo txt dos vídeos a serem "capturados"
def carregaNomesASeremLidos(txt):
    listaNome = []
    pFile = open(txt, "r")
    print('Entrou PYTHON - carregaNomesASeremLidos')
    for line in pFile:
        listaNome.append(line.rstrip())
    return listaNome

# Cria o nome das pastas de acordo com o nome dno arquivo txt
def criaPastaComNomes(listaNomes):
    
    # for nome in listaNomes:
    try:
        nome = listaNomes.split('.')[0]
#         print("Criou pasta " + nome)
        os.mkdir(nome)
        return nome
    except OSError:
        print("Não foi possível criar o diretório ou o mesmo já existe.")

# Realiza a captura das faces no vídeo
def salvaFacesDetectadas(caminho, nome):
    
    pathFile = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    print(caminho)
    print(caminho+nome+'.mp4')
    # pathFile = r"C:\\Users\\diogo\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(pathFile)
    # cap = cv2.VideoCapture(sys.path[0] + "/" + nome + ".mp4") #inicia captura da câmera
    cap = cv2.VideoCapture(caminho + nome + ".mp4") #inicia captura da câmera
    counterFrames = 0
    # Número de amostras
    limitSamples = 100

    while(counterFrames < limitSamples): #quando chegar ao milésimo frame, para
        print(counterFrames)
        ret, img = cap.read()

        #frame não pode ser obtido? entao sair
        if(ret == False):
            cap.release()
            return

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #se nenhuma face for achada, continue
        if not np.any(faces):
            continue

        #achou uma face? recorte ela (crop)
        for (x, y, w, h) in faces:
            rostoImg = img[y:y+h, x:x+w]

        #imagens muito pequenas são desconsideradas
        larg, alt, _ = rostoImg.shape
        if(larg * alt <= 20 * 20):
            continue

        #salva imagem na pasta
        rostoImg = cv2.resize(rostoImg, (255, 255))
        cv2.imwrite(nome + "/" + str(counterFrames)+".jpg", rostoImg)
        counterFrames += 1
            
    cap.release()

#função principal da aplicação
def main(caminho, nome):
    # listaNome = carregaNomesASeremLidos(sys.path[0]+"/nomesDosVideos.txt")
    # listaNome = carregaNomesASeremLidos(sys.path[0]+"/nomesDosVideos.txt")
    os.chdir(caminho)
    arquivo = criaPastaComNomes(nome)
    # sys.stdout.flush()
    
    # for nome in listaNome:
    #     print("Analisando: " + nome)
    salvaFacesDetectadas(caminho, arquivo)


if __name__ == "__main__":
    print('Entrou PYTHON')
    caminhoArquivo = sys.argv[1]
    nomeArquivo = sys.argv[2]
    # print(caminhoArquivo)
    main(caminhoArquivo, nomeArquivo)