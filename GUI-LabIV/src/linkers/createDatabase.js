
function createDatabase(caminho, arquivo){
    const { PythonShell } = require('python-shell');
    const  path = require('path');

    console.log('ENTROU CREATE DATABASE')
    console.log(`${caminho}`)
    console.log(`${arquivo}`)
    
    const config = {
        script: path.join(__dirname, '/engine/createDatabase.py'),
        options:{
            args: [caminho, arquivo]
        }
    }
    // const variavel = new PythonShell('C:\\Users\\diogo\\OneDrive\\Área de Trabalho\\ENGENHARIA DE SISTEMAS\\10º PERÍODO\\LAB. IV\\Projeto-LAB_IV\\GUI-LabIV\\src\\engine\\createDatabase.py');
    const variavel = new PythonShell(config.script, config.options);
        
    variavel.on('message', function(message){
        console.log(message);
    });
}


