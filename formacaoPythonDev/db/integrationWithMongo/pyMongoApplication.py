import pymongo as pyM
import datetime
from pprint import pprint

connection = 'mongodb+srv://rafs:teste@cluster0.855lfrf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = pyM.MongoClient(connection, tls=True, tlsAllowInvalidCertificates=True)

db = client.test
collection = db.test_collection
print(db.list_collection)

post = {
    "author": "Mike",
    "text": "My first mongodb post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(datetime.timezone.utc)
}

posts = db.posts

post_id = posts.insert_one(post).inserted_id
print(post_id)
print(db.list_collection_names())

pprint(db.posts.find_one())

# bulk inserts
new_posts = [
    {
        "author": "Mike",
        "text": "Another post!",
        "tags": ["bulk", "insert", "post"],
        "date": datetime.datetime.now(datetime.timezone.utc)
    },
    {
        "author": "Joao",
        "text": "Post from Joao. New post available",
        "title": "Mongo is fun",
        "date": datetime.datetime.now(datetime.timezone.utc)
    }
]

result = posts.insert_many(new_posts)

print(result.inserted_ids)

pprint(db.posts.find_one({"author": "Joao"}))

# Documentos presentes na coleção posts
for post in posts.find():
    pprint(post,)
    print()
    