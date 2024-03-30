from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select, func
from sqlalchemy.orm import declarative_base, relationship, Session


Base = declarative_base()
engine = create_engine('sqlite:///memory')


class Client(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String(9))
    address = relationship("Conta", back_populates="cliente")


class Account(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    acc_type = Column(String, nullable=True)
    aggency = Column(String)
    num = Column(Integer, nullable=True)
    id_client = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    client = relationship("Cliente", back_populates="endereco")


def create_tables():
    Base.metadata.create_all(engine)


with Session(engine) as session:
    fulano = Client(
        name="Fulano de Tal",
        cpf="123456789",
        address = [Account(agency='0001')]
    )
    sicrano = Client(
        name="Sicrano da Silva",
        cpf="246876543",
        endereco=[Account(agencia='0001')]
    )
    deltrano = Client(
        nome="Deltrano Soares",
        cpf="123786309",
        endereco=[Account(agencia='0001')]
    )

session.add_all([fulano, sicrano, deltrano])

session.commit()

stmt = select(Client)

connection = engine.connect()
results = connection.execute(stmt).fetchall()

for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(Client)
results = connection.execute(stmt_count).fetchall()
for result in results:
    print(result)

stmt_where = select(Client).where(Account.id.in_([2]))
results = connection.execute(stmt_where).fetchall()
for result in results:
    print(result)
    