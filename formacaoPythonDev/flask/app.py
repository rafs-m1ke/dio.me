from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/<int:id>")
def pessoas(id):
    return jsonify({"id": id,"nome": "Rafael", "idade": 24})

# @app.route("/soma/<int:a>/<int:b>")
# def soma(a, b):
#     return jsonify({'soma': a + b})

@app.route("/soma", methods=['POST', 'PUT', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 20
    return jsonify({'soma': total})

if __name__ == "__main__":
    app.run(debug=True)