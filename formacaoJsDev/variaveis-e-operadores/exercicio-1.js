/* 
    Faça um algoritimo que dado as 3 notas tiradas por um aluno durante o semestre,
    calcula e imprima sua média e sua classificação conforme a tabela abaixo

    Media = (nota 1 + nota 2 + nota 3) / 3;

    Classificação:
    - Média menor que 5, reprovação;
    - Média entre 5 e 7, recuperação;
    - Média acima de 7, passou de semestre;
*/

let nota1 = 4;
let nota2 = 6;
let nota3 = 4;

const media = (nota1 + nota2 + nota3) / 3;

if (media > 7) {
    console.log(`Média = ${media.toFixed(2)}\nClassificação: Pasou de semestre`)
} else if (media >= 5 ) {
    console.log(`Média = ${media.toFixed(2)}\nClassificação: Recuperação`)
} else {
    console.log(`Média = ${media.toFixed(2)}\nClassificação: Reprovação`)
}
