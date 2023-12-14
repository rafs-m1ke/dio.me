// Crie uma função que receba dois números com oparâmetros

function compare(num1, num2) {
    var compResult = null
    var soma = null
    var compSoma = null
    if (num1 == num2) {
        compResult = `Os números ${num1} e ${num2} são iguais!`
    } else {
        compResult = `Os números ${num1} e ${num2} não são iguais!`
    }

    soma = num1 + num2

    if (soma > 10 && soma < 20) {
        compSoma = `Sua soma é ${soma}, que é maior que 10 e menor que 20.`
    } else if (soma < 10) {
        compSoma = `Sua soma é ${soma}, que é menos que 10 e menor que 20.`
    } else {
        compSoma = `Sua soma é ${soma}, que é maior que 10 e maior que 20.`
    }

    console.log(compResult, compSoma)

}


compare(10, 10)