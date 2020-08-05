# Projeto da disciplina Laboratório de Projetos 4 - UFMG
O projeto desenvolvido tem como objetivo auxiliar na classificação étnica por meio das tecnologias de aprendizado de máquina e reconhecimento facial.

## 📚 Instruções de uso
1. O arquivo input.txt contém os nomes dos arquivo de vídeo (.mp4) que servirão para criar a base de dados para análise

2. O arquivo createDatabase.ipynb criará a base de dados de acordo com o nome do vídeo escrito no código. Isso se dára da seguinte forma:
- O código lê os nomes dos vídeos contidos em input.txt, no qual é necessário ter arquivos de vídeo com os mesmos nomes na pasta, e cria uma pasta, com o nome do arquivo de video, contendo várias capturas de imagem que serão utilizadas no algoritmo de classificação.

3. Já o arquivo ethnicityClassification.ipynb utiliza uma base de dados, contida na pasta UTKFACE (que não pôde ser colocada no GitHub), para realizar o treinamento da sua rede neural para posteormente aplicar o aprendizado de máquina.
- Após o treinamento da rede, o código utiliza a pasta com as capturas de imagens, criada anteriormente com o createDatabase, para aplicar seus padrões e classificar as imagens individualmente. 
- O resultado final é a média das porcentagens de cada foto, mostrada em um gráfico de barras

## 🧠 Observações importantes
Utilizou-se uma base de dados não brasileira, com cerca de 20 mil imagens para treinar a rede neural. Primeiramente, a base de dados possui 5 classificações:
- Branco
- Preto
- Amarelo
- Latino
- Asiático

Para se adaptar a nossa escala ética, utilizamos 4 classes, agrupando Amarelo e Latino na classificação Pardo. Dessa forma, nossas classes são:
- Branco
- Preto
- Ásiatico
- Pardo 