class Bicicletaria:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('Bi Bi')
    
    def parar(self):
        print('Parando')
        print('Bicicleta parou')
    
    def correr(self):
        print('Correndo')
    
    # def __str__(self):
    #     return f'Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: {self.valor}'
    
    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"

# b1 = Bicicletaria('vermelha', 'Caloi', 2020, 500.00)

# b1.buzinar()
# b1.correr()
# b1.parar()

# print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicletaria('verde', 'Monark', 2021, 600.00)
print(b2)