from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__table__)


# Conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Investiga o esquema do banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))

print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    rafael = User(
        name="rafael",
        fullname="rafael m f silva",
        address=[Address(email_address='rafael@email.com')]
    )

    gleize = User(
        name="gleize",
        fullname="gleize c r lemos",
        address=[Address(email_address="gleize@email.com"), Address(email_address="gleize2@email.com")]
    )

    luiz = User(
        name="Luiz", fullname="Luiz Rodrigo M C S"
    )

    # Enviando para o BD (persistência de dados)
    session.add_all([rafael, gleize, luiz])

    session.commit()


stmt = select(User).where(User.name.in_(['rafael', 'gleize']))
print("\nRecuperando usuários a partir de condição de filtragem")
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print("\nRecuperando os endereços de email de Gleize")
for address in session.scalars(stmt_address):
    print(address)

order_stmt = select(User).order_by(User.fullname)
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(order_stmt):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print(results)
print("\nExecutando statement a partir da connection")
for result in results:
    print(result)

stmt_count = select(func.count("*")).select_from(User)
print("\nTotal de instancias em User")
for result in session.scalars(stmt_count):
    print(result)