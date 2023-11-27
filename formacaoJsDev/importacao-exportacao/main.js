const {gets, print} = require('./funcoes-auxiliares');

const numeros = [];

for (let i = 0; i <= 9; i++){
    numeros.push(gets());
}

let maiorPar = 0;
let menorImpar = 3; 

for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] % 2 == 0) {
        if (numeros[i] > maiorPar){
            maiorPar = numeros[i];
        }
    } else {
        if (numeros[i] < menorImpar){
            menorImpar = numeros[i];
        }
    }
    
}

print(`Maior número par: ${maiorPar}`);
print(`Menor número impar: ${menorImpar}`);
