saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def main():
    menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==>'''
    
    while True:
        opcao = input(menu)
        
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            sacar(valor)
        
        elif opcao == "e":
            mostrar_extrato()
            
        elif opcao == "q":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito: R$ {valor:.2f}\n")
    elif valor <= 0:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
        global saldo, limite, numero_saques, extrato
        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido")

def mostrar_extrato():
    global extrato, saldo
    print("EXTRATO".center(35,"="))
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}".center(35, " "))
    print("=" * 35)

main()