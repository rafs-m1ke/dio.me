import pymongo as pyM
from pprint import pprint

client = pyM.MongoClient("conexão do Atlas")

db = client.client
collection = db.bank

posts = [{
    "name" : "Fulano",
    "cpf": "123456",
    "address": "Rua A",
    "account": "001",
    "agency": "0001",
    "type" : "corrente",
    "value": 0
}, {
    "name" : "Cicrano",
    "cpf": "654321",
    "address": "Rua B",
    "account": "002",
    "agency": "0001",
    "type" : "corrente",
    "value": 0
}, {
    "name" : "Deltrano",
    "cpf": "456123",
    "address": "Rua C",
    "account": "003",
    "agency": "0001",
    "type" : "corrente",
    "value": 0
}, {
    "name" : "Beltrano",
    "cpf": "321654",
    "address": "Rua D",
    "account": "004",
    "agency": "0001",
    "type" : "corrente",
    "value": 0
}]

post = {
    "name" : "John Doe",
    "cpf": "564231",
    "address": "Rua E",
    "account": "005",
    "agency": "0002",
    "type" : "corrente",
    "value": 0
}

pprint(collection.find())
find = collection.find()
for post in find:
    pprint(post)

print(collection.count_documents({}))

print(collection.count_documents({"agency": "0001"}))

for post in collection.find({}).sort("name"):
    pprint(post)
