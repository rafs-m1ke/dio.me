const entradas = [5, 11, 4, 9, 10, 8, 7, 26, 33];
let i = 0;

function gets() {
    const valor = entradas[i];
    i++;
    return valor;

}

function print(texto) {
    console.log(texto);
}

module.exports = {
    gets,
    print
}