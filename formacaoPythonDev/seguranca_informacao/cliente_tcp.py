import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!")
        print(f"Erro: {e}")
        sys.exit()
        
    print("Socket criado com sucesso!")

    host_alvo = input("Digite o host ou ip a ser conectado: ")
    porta_alvo = int(input("Digite a porta a ser conectada: "))
    
    try:
        s.connect((host_alvo, porta_alvo))
        print("Cliente TPC conectado com sucesso!")
        print(f"Host alvo {host_alvo}, na porta {porta_alvo}")
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possivel realizar a conexão!")
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()