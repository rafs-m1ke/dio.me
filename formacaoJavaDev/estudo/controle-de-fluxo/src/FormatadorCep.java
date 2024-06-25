public class FormatadorCep {
    public static void main(String[] args) {
        try {
            String cepFormatado = formatarCep("12345678");
            System.out.println(cepFormatado);
        } catch (CepInvalidException ex) {
            ex.printStackTrace();
        }
    }

    static String formatarCep(String cep) throws CepInvalidException {
        if(cep.length() != 8) {
            throw new CepInvalidException();
        }

        return "23.765-064";
    }
}
