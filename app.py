from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis a Sociedade do Anel',
        'autor': 'J.R.R. Tolkien',
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling',
    },
    {
        'id': 3,
        'titulo': 'O Hobbit',
        'autor': 'J.R.R. Tolkien',
    },
]

@app.route('/livros', methods=['GET'])
def encontra_livro():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def encontra_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return 

@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)
    return

app.run(port=5000, host='localhost', debug=True)