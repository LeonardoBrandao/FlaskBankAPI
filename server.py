import os

from flask import Flask, request, jsonify

project_dir = os.path.dirname(os.path.abspath(__file__))

class Conta:
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo

    def saldo(self):
        return self.saldo

    def deposito(self, saldo):
        self.saldo += saldo

    def saque(self, saldo):
        self.saldo -= saldo

    def __str__(self):
        return 'id: {} - saldo: {}'.format(self.id, self.saldo)

contas = []
for i in range(10):
    contas.append(Conta(i, 1000))

app = Flask(__name__)

@app.route("/")
def hello():
    return "Servidor rodando! Agora, consulte a documentação."

@app.route("/contas/<id>", methods=['GET'])
def get_saldo_conta(id):
    try:
        id = int(id)
        if id < 0:
            return jsonify({"status": 'FAIL', 'mensagem': 'Conta inexistente.'}), 404
    except:
        return jsonify({"status": 'FAIL', 'mensagem': 'Conta inexistente.'}), 404
    try:
        conta = contas[id]
        return jsonify({"id": conta.id, "saldo": conta.saldo})
    except Error:
        return jsonify({"status": 'FAIL', 'mensagem': 'Conta Inexistente.'}), 404

@app.route("/contas/<id>", methods=['POST'])
def put_deposito_saldo_conta(id):
    try:
        id = int(id)
        if id < 0:
            return jsonify({"status": 'FAIL', "valor_depositado": 0, 'mensagem': 'Conta inexistente.'}), 404
    except:
        return jsonify({"status": 'FAIL', "valor_depositado": 0, 'mensagem': 'Conta inexistente.'}), 404
    try:
        valor = float(request.form['valor'])
    except ValueError:
        return jsonify({"status": 'FAIL', "valor_depositado": 0, 'mensagem': 'Valor deve ser um número e maior que 0.'}), 500
    if valor > 0:
        valor = float(request.form['valor'])
        try:
            if id > 0:
                conta  = contas[id]
            else:
                return jsonify({"status": 'FAIL', "valor_depositado": 0, 'mensagem': 'Conta inexistente.'}), 404
        except:
            return jsonify({"status": 'FAIL', "valor_depositado": 0, 'mensagem': 'Conta inexistente.'}), 404
        conta.deposito(valor)
        return jsonify({"id": conta.id, "saldo": conta.saldo})
    else:
        return jsonify({"status": 'FAIL', "valor_depositado": 0, 'mensagem': 'Valor deve ser um número e maior que 0.'}), 406
   

@app.route("/contas/<id>", methods=['PUT'])
def put_saque_saldo_conta(id):
    try:
        id = int(id)
        if id < 0:
            return jsonify({"status": 'FAIL', "valor_sacado": 0, 'mensagem': 'Conta inexistente.'}), 404
    except:
        return jsonify({"status": 'FAIL', "valor_sacado": 0, 'mensagem': 'Conta inexistente.'}), 404
    try:
        valor = float(request.form['valor'])
        conta  = contas[id]
        if valor <= conta.saldo and valor > 0:
            conta.saque(valor)
            return jsonify({"id": conta.id, "saldo": conta.saldo})
        return jsonify({"status": 'FAIL', "valor_sacado": 0, 'mensagem': 'Saldo Insuficiente.'}), 406
    except ValueError:
        return jsonify({"status": 'FAIL', "valor_sacado": 0, 'mensagem': 'Valor deve ser um número e maior que 0.'}), 500
    except IndexError:
        return jsonify({"status": 'FAIL', "valor_sacado": 0, 'mensagem': 'Conta inexistente.'}), 404


@app.route("/contas/transferencia/<conta_origem>/<conta_destino>", methods=['POST'])
def post_transferencia_contas(conta_origem, conta_destino):
    try:
        conta_origem = int(conta_origem)
        if conta_origem < 0:
            return jsonify({"status": 'FAIL', "valor_transferido": 0, 'mensagem': 'Conta inexistente.'}), 404
    except:
        return jsonify({"status": 'FAIL', "valor_transferido": 0, 'mensagem': 'Conta inexistente.'}), 404
    try:
        conta_destino = int(conta_destino)
        if conta_destino < 0:
            return jsonify({"status": 'FAIL', "valor_transferido": 0, 'mensagem': 'Conta inexistente.'}), 404
    except:
        return jsonify({"status": 'FAIL', "valor_transferido": 0, 'mensagem': 'Conta inexistente.'}), 404
    try:
        valor = float(request.form['valor'])
    except:
        return jsonify({"status": 'FAIL', "valor_transferido": 0, 'mensagem': 'Valor deve ser um número e maior que 0.'}), 500
    if contas[conta_origem].saldo >= valor and valor > 0:
        contas[conta_origem].saldo -= valor
        contas[conta_destino].saldo += valor
        return jsonify({'status': 'OK', 'valor_transferido': valor})
    return jsonify({"status": 'FAIL', "valor_transferido": 0, 'mensagem': 'Saldo Insuficiente.'}), 406


if __name__ == "__main__":
    app.run(debug=True)