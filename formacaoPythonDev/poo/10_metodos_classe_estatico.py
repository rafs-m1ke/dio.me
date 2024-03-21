class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        print(cls)
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade > 17

# p = Pessoa("Rafael", 24)
# print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nascimento(1999, 1, 1, "Rafael")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(28))