from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Rafael', idade=24)
    print(pessoa)
    pessoa.save()

def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = pessoa.query,filter_by(nome='Rafael')
    print(pessoa)


if __name__ == "__main__":
    consulta()