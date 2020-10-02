
function createDatabase(caminho, arquivo, quantidadeImagensIniciais){
    const { PythonShell } = require('python-shell');
    const  path = require('path');

    // console.log('ENTROU CREATE DATABASE')
    // console.log(`${caminho}`)
    // console.log(`${arquivo}`)
    
    const config = {
        script: path.join(__dirname, '/engine/createDatabase.py'),
        options:{
            args: [caminho, arquivo, quantidadeImagensIniciais]
        }
    }
    // const variavel = new PythonShell('C:\\Users\\diogo\\OneDrive\\Área de Trabalho\\ENGENHARIA DE SISTEMAS\\10º PERÍODO\\LAB. IV\\Projeto-LAB_IV\\GUI-LabIV\\src\\engine\\createDatabase.py');
    const variavel = new PythonShell(config.script, config.options);
        
    let teste = []
    
    variavel.on('message', function(message) {
        teste.push(message);
    });

    // variavel.end(function (err,code,signal) {
    //     if (err) throw err;
    //     // console.log('The exit code was: ' + code);
    //     // console.log('The exit signal was: ' + signal);
    //     console.log('finished');
    //   })
    console.log(teste)
    return teste;
}


