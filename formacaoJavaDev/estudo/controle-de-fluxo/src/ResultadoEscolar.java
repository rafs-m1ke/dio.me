

public class ResultadoEscolar {
    public static void main(String[] args) {
        int nota = 7;

        String situacao = nota >= 7 ? "Aprovado" : nota >= 5 ? "Recuperação" : "Reprovado";

        System.out.println(situacao);
    }

}
