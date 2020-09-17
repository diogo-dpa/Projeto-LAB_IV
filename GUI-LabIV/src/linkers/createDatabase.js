
function createDatabase(){
    const { PythonShell } = require('python-shell');
    const  path = require('path');

    console.log('ENTROU CREATE DATABASE')
    
    
    // var elementoHTML = document.getElementById("elemento").value;
    const options = {
        script: path.join(__dirname, '/engine/createDatabase.py'),
        // args: [elementoHTML]
    }
    console.log(options.script)
    // const variavel = new PythonShell('C:\\Users\\diogo\\OneDrive\\Área de Trabalho\\ENGENHARIA DE SISTEMAS\\10º PERÍODO\\LAB. IV\\Projeto-LAB_IV\\GUI-LabIV\\src\\engine\\createDatabase.py');
    const variavel = new PythonShell(options.script);
        
    variavel.on('message', function(message){
        console.log(message);
    });
}


