
function applyAlgorithm(caminhoModeloTreinado, caminhoPastaParaAplicar){
    const { PythonShell } = require('python-shell');

    const path = require('path');
    console.log('ENTROU APPLY JS')
    // var elementoHTML = document.getElementById("elemento").value;

    const config = {
        script: path.join(__dirname, '/engine/applyAlgorithm.py'),
        options: {
            args: [caminhoModeloTreinado, caminhoPastaParaAplicar]
        }
    }

    const variavel = new PythonShell(config.script, config.options);

    variavel.on('message', function(message){
        console.log(message);
    })
}