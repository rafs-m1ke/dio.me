/*
    Crie uma classe para representar carros.
    Os carros possuem uma marca, uma cor e uma gasto médio de combustível por Km rodado.
    Crie um método que dado a quantidade de quilometros e o preço do combustível, nos dê o
    valor gasto em reais para realizar este percurso.
*/

class Carro {
    marca;
    cor;
    gastoMedioKm;

    constructor(a, b, c) {
        this.marca = a;
        this.cor = b;
        this.gastoMedioKm = c;
    }

    valorAutonomia(dist, valorGas) {
        const valor = dist * valorGas * this.gastoMedioKm;
        console.log(`Para realizar um percurso de ${this.dist} Km, com o ${this.marca} ${this.cor} será, gasto R$ ${valor.toFixed(2)} com combustível!`);
    }
}

const mobi = new Carro("Fiat", "Branco", 1/16);

mobi.valorAutonomia(200, 5.25);