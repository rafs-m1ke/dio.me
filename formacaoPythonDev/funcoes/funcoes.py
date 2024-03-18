def exibir_mensagem():
    print('Olá, mundo!')

def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo {nome}!")
    
def exibir_mensagem_3(nome='Fulano'):
    print(f"Seja bem-vindo {nome}!")

def calcular_total(numeros):
    return sum(numeros)

def salvar_carro(marca, modelo, ano, placa):
    print(f"Salvando carro {marca} {modelo} {ano} {placa}")

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

#exibir_poema("Zen of Python", "Beauti ul is better than ugly.", author="Tim Peters", year="1999")

salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")
    
    salario += bonus
    return salario

# lista = [1]
# salario_com_bonus = salario_bonus(500, lista)
# print(salario_bonus)
# print(lista)

# T = int(input())

# for i in range(T):
#     N = int(input())
#     K = int(input())
#     garrafas = (N % K) + (N / K)
#     print(int(garrafas))

T = int(input())

for i in range(T):
  N, K = int(input().split(" "))
  N = int(N)
  K = int(K)
  garrafas = ((N % K) + (N / K))
  print(int(garrafas))