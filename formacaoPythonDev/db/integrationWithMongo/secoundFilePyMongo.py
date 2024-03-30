import pymongo as pyM
from pprint import pprint

connection = 'mongodb+srv://rafs:teste@cluster0.855lfrf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = pyM.MongoClient(connection, tls=True, tlsAllowInvalidCertificates=True)
db = client.test
posts = db.posts

for post in posts.find():
    pprint(post)
    print()
    
print(posts.count_documents({"tags": "python"}))