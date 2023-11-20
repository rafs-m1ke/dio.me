/* 
    IMC = peso / (altura * altura)

    Elaborar um algoritimo que calcule o IMC e informe exemplo tabela abaixo:

    Abaixo de 18.5 > Abaixo do peso;
    Entre 18.5 e 25 > Peso normal;
    Entre 25 e 30 > Acima do peso;
    Entre 30 e 40 > Obeso;
    Acima de 40 > Obesidade mórbida;
*/

const peso = 80;
const altura = 1.75;

const imc = peso / (altura**2);

console.log(`IMC = ${imc.toFixed(2)}`)

if (imc > 40) {
    console.log(`Obediade Mórbida!`)
} else if (imc >= 30) {
    console.log(`Obeso!`)
} else if (imc >= 25) {
    console.log(`Acima do peso!`)
} else if (imc >= 18.5) {
    console.log(`Peso normal!`)
} else {
    console.log(`Abaixo do peso!`)
}
