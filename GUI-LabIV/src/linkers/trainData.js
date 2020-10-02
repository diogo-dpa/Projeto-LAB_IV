
function trainData(treinamento, caminhoPastaSalvaModelo){
    const { PythonShell } = require('python-shell');

    const path = require('path');

    console.log('ENTROU TRAIN DATA JS')
    console.log(treinamento)
    // var elementoHTML = document.getElementById("elemento").value;

    const config = {
        script: path.join(__dirname, '/engine/trainData.py'),
        options: {
            args: [treinamento, caminhoPastaSalvaModelo]
        }
    }

    const variavel = new PythonShell(config.script, config.options);

    // treinamento? variavel = new PythonShell(opcoes.script):
    //     variavel = new PythonShell(opcoes.script);
    
    let teste = []

    variavel.on('message', function(message){
        // console.log(message);
        teste.push(message)
    })

    return teste;
}