
function trainData(treinamento){
    const { PythonShell } = require('python-shell');

    const path = require('path');

    console.log('ENTROU TRAIN DATA JS')
    console.log(treinamento)
    // var elementoHTML = document.getElementById("elemento").value;

    const optionsUpper = {
        script: path.join(__dirname, '/engine/trainData.py'),
        options: {
            args: [treinamento]
        }
    }

    const variavel = new PythonShell(optionsUpper.script, optionsUpper.options);

    // treinamento? variavel = new PythonShell(opcoes.script):
    //     variavel = new PythonShell(opcoes.script);
    

    variavel.on('message', function(message){
        console.log(message);
    })
}