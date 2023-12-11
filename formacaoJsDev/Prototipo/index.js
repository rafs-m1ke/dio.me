// const lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// lista.forEach((value, i) => {
//     console.log(value + i);
// })

// const listaDeNumerosPares = lista.filter((element) => {
//     return element % 2 === 0;
// })

// console.log(listaDeNumerosPares);

// class Pessoa {
//     constructor(name) {
//         this.name = name;
//     }
// }

// const lista = [new Pessoa('João'), new Pessoa('Maria'), new Pessoa('José')];

// const listaNomes = lista.map((value) => {
//     return `
//         <li>${value.name}</li>
//     `
// })

// console.log(listaNomes);


// const lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// const somaDeTodosOsNumros = lista.reduce((previous, current) => {
//     console.log(previous, current);
//     return previous + current;
// })

// console.log(somaDeTodosOsNumros);

const lista = [{nome: 'João', idade: 20}, {nome: 'Maria', idade: 30}, {nome: 'José', idade: 40}];

const elementosEmHtml = lista
    .filter((e) => e.nome.startsWith('J'))
    .map((e) => {
        return `
            <li>${e.nome}</li>
        `
    })
    .join('');


console.log(elementosEmHtml);