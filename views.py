from flask import request, jsonify
from ClienteDAO import ClienteDAO
from Cliente import Cliente
from app import db, app


cliente_dao = ClienteDAO(db)

@app.route("/cliente", methods=['POST'])
def inserir():
    data = request.json
    cliente = Cliente(data['nome'], data['email'], data['cpf'], data['dtNascimento'])
    if cliente_dao.inserir(cliente):
        return jsonify("cliente cadastrado"), 200
    else:
        return jsonify("erro ao cadastrar cliente"), 404

@app.route("/cliente")
def listar():
    rows = cliente_dao.listar()
    clientes = []
    for row in rows:
        clientes.append({'id': row[0], 'nome': row[1], 'email': row[2], 'cpf':row[3], 'dtNascimento': row[4]})
    return jsonify(clientes)

@app.route("/cliente/<int:id>")
def listarId(id):
    clientes = cliente_dao.listarId(id)
    if clientes is None:
        return jsonify("cliente inexistente"), 404
    else:
        return jsonify(clientes), 200

@app.route("/cliente/<int:id>", methods=['DELETE'])
def excluir(id):
    if cliente_dao.listarId(id) is None:
        return jsonify("cliente inexistente"), 404
    else:
        cliente_dao.excluir(id)
        return jsonify({"cliente": id})

@app.route("/cliente/<int:id>", methods=['PUT'])
def atualizar(id):
    data = request.json
    cliente = Cliente(data['nome'], data['email'], data['cpf'], data['dtNascimento'])
    if cliente_dao.listarId(id):
        cliente_dao.atualizar(id, cliente)
        return jsonify("cliente atualizado com sucesso"), 200
    else:
        return jsonify("error"), 404
