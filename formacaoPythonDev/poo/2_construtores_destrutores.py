class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Destruindo a classe...")
    
    def falar(self):
        print("auau")

def criar_cachorro():
    c = Cachorro('Rex', 'Marrom')
    print(c.nome)
    print('Ola Mundo')
    print('Ola Mundo')
    print('Ola Mundo')
    print('Ola Mundo')
    print('Ola Mundo')

criar_cachorro()
