class Pessoa {
    nome;
    peso;
    altura;

    constructor(nome, peso, altura) {
        this.nome = nome;
        this.peso = peso;
        this.altura = altura;
    }

    calcImc() {
        return this.peso / Math.pow(this.altura, 2);
        // console.log(`O IMC de ${this.nome} é de ${imc.toFixed(2)}`);
    }

    classificarImc() {
        if (this.calcImc() > 40) {
            return `Obediade Mórbida!`;
        } else if (this.calcImc() >= 30) {
            return `Obeso!`;
        } else if (this.calcImc() >= 25) {
            return `Acima do peso!`;
        } else if (this.calcImc() >= 18.5) {
            return `Peso normal!`;
        } else {
            return `Abaixo do peso!`;
        }
    }
}

const rafael = new Pessoa("Rafael", 40, 1.7);

console.log(rafael.classificarImc());