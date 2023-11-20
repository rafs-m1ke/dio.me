const precoGasolina = 5.25;
const precoEtanol = 4.1;
const isGasolina = true;
const gastoMedioGas = 16;
const gastoMedioEtanol = 14;
const distanciaViagem = 400;
let valor;

if (isGasolina) {
  valor = (distanciaViagem / gastoMedioGas) * precoGasolina;
} else {
  valor = (distanciaViagem / gastoMedioEtanol) * precoEtanol;
}

console.log(valor.toFixed(2));
