/* 
    Escrever um algoritmo que calcule o valor a ser pago pelo produto de acordo
    com as formas de pagamento abaixo:

    1 - À vista Débito, recebe 10% de desconto;
    2 - À vista Dinheiro ou PIX, recebe 15% de desconto;
    3 - Em duas vezes, preço normal da etiqueta do produto;
    4 - Acima de duas vezes, preço normal mais 10% de juros;
*/

function aplicarDesconto(valor, desconto){
    return (valor - (valor * (desconto / 100)))
}

function aplicarJuros(valor, juros){
    return (valor + (valor * (juros / 100)))
}

const precoProduto = 100;

const pagamento = 2;

function juros(forma, valor){
    if (forma === 1) {
        return aplicarDesconto(valor, 10);
    } else if (forma === 2) {
        return aplicarDesconto(valor, 15);
    } else if (forma === 3) {
        return valor;
    } else {
        return aplicarJuros(valor, 10);
    }
}

console.log(`Valor a ser pago: ${juros(pagamento, precoProduto).toFixed(2)}`)