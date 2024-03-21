class Pessoa:
    def __init__(self, nome, ano_nasc):
        self._nome = nome
        self._ano_nasc = ano_nasc
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nasc

pessoa = Pessoa('Rafael', 2000)

print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")