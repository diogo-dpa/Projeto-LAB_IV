# Projeto da disciplina Laboratório de Projetos 4 - UFMG
O projeto desenvolvido tem como objetivo auxiliar na classificação étnica por meio das tecnologias de aprendizado de máquina e reconhecimento facial.<br/> 
### Tecnologias utilizadas
Foi utilizado a linguagem Python para o desenvolvimento do algoritmo de aprendizado de máquina e para a GUI utilizou-se o framework Electron.

## 📚 Instruções de uso
- A interface gráfica é bem intuitiva e é composta por 4 abas: <br/>
    1- Início: Esta parte tem como responsabilidade escolher o vídeo do candidato a ser avaliado, designar sua etnia escolhida, além de escolher o número X de imagens que serão geradas a partir do vídeo.
    <br/>*Resposta esperada*: Uma pasta com o mesmo nome do vídeo, contendo X capturas faciais.
    <br/>
    2- Treinamento: Esta parte serve para escolher a pasta no qual o modelo de treinamento será criado, além de escolher a pasta com as imagens de treinamento da rede.
    <br/>
    *Resposta esperada:* Uma pasta "modelo" será criada no diretório onde foi escolhido.
    <br/>
    3- Execução: Esta parte é responsável por aplicar o modelo treinado nas pasta inicialmente gerada. É necessário escolher a pasta "modelo" gerada, além da pasta inicial do vídeo.
    <br/>
    4- Resposta: Aqui são mostrados os resultados do algoritmo aplicado na pasta inicial. Há duas imagens, no qual a primeira é uma prévia das amostras rotuladas e a segunda é o gráfico final, contendo as porcentagens étnicas aferidas nas amostras.

## 🧠 Observações importantes
Utilizou-se uma base de dados não brasileira, com cerca de 20 mil imagens para treinar a rede neural. Primeiramente, a base de dados possui 5 classificações:
- Branco
- Negro
- Amarelo
- Latino
- Asiático

Para se adaptar ao nosso contexto étnico, utilizamos 4 classes, agrupando Amarelo e Latino na classificação Pardo. Dessa forma, nossas classes são:
- Branco
- Negro
- Ásiatico
- Pardo