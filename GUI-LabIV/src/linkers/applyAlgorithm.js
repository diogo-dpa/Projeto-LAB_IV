
function applyAlgorithm(){
    const { PythonShell } = require('python-shell');

    const path = require('path');
    console.log('ENTROU APPLY JS')
    // var elementoHTML = document.getElementById("elemento").value;

    const opcoes = {
        script: path.join(__dirname, '/engine/applyAlgorithm.py'),
        // args: [elementoHTML]
    }

    const variavel = new PythonShell(opcoes.script);

    variavel.on('message', function(message){
        swal(message);
    })
}