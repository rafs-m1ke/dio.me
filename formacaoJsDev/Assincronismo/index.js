

// const randomNumberPromisse = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         const number = parseInt(Math.random() * 100);
//         resolve(number);
//     }, 1000);
// })

// randomNumberPromisse
//     .then((value) => {
//         console.log(value);
//     })
//     .catch((error) => {
//         console.log(error);
//     })
//     .finally(() => {
//         console.log('Finalizou');
//     })

const fs = require('fs');
const path = require('path');

const filePath = path.resolve(__dirname, 'tarefas.csv')

const readFilePromise = fs.promises.readFile(filePath)

readFilePromise
    .then((arquivo) => {
        console.log(arquivo.toString('utf8'));
    })
    .then((text) => console.log(text))
    .catch((error) => {
        console.log('Deu ruim!', error);
    })