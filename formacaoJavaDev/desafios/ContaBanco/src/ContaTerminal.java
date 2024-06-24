
import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        String nomeCliente;
        int numeroConta;
        String agenciaBancaria;
        Double saldo;

        System.out.print("\nDigite seu nome: ");
        nomeCliente = leitor.nextLine();

        System.out.print("\nDigite a agência: ");
        agenciaBancaria = leitor.nextLine();

        System.out.print("\nDigite a conta: ");
        numeroConta = leitor.nextInt();

        System.out.print("\nDigite seu saldo: ");
        saldo = leitor.nextDouble();


        System.out.printf("\nOlá %s, obrigado por criar uma conta em nosso banco, sua agência é %s, conta %d e seu saldo R$ %.2f já está disponível!\n", nomeCliente, agenciaBancaria, numeroConta, saldo);

    }

}
