class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    
    def __str__(self):
        return f"Animal com {self.nro_patas} patas, cor {self.cor_pelo}, cor do bico {self.cor_bico}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass

gato = Gato(nro_patas=4, cor_pelo='preto')
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo='Vermelho', cor_bico='Laranja')

print(gato)
print(ornitorrinco)