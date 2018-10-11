import os

from flask import Flask, request, jsonify

project_dir = os.path.dirname(os.path.abspath(__file__))

class Conta:
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo

    def deposito(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            return {"status": "FAIL", "valor_depositado": 0, "mensagem": "Valor deve ser um número."}, 500

        if valor > 0:
            self.saldo += valor
            return {"id": self.id, "saldo": self.saldo}, 200
        else:
            return {"status": "FAIL", "valor_depositado": 0, "mensagem": "Valor deve ser maior que 0."}, 500

    def saque(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            return {"status": "FAIL", "valor_depositado": 0, "mensagem": "Valor deve ser um número."}, 500

        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                return {"id": self.id, "saldo": self.saldo}, 200
            else:
                return {"status": "FAIL", "valor_sacado": 0, "mensagem": "Saldo Insuficiente."}, 406
        else:
            return {"status": "FAIL", "valor_sacado": 0, "mensagem": "Valor deve ser maior que 0."}, 500

    def __str__(self):
        return "id: {} - saldo: {}".format(self.id, self.saldo)

contas = []
for i in range(10):
    contas.append(Conta(i, 1000))

def getConta(id):
    try:
        id = int(id)
        if id < 0:
            return None
        return contas[id]
    except:
        return None


app = Flask(__name__)

@app.route("/")
def hello():
    return "Servidor rodando! Agora, consulte a documentação."

@app.route("/contas/<id>", methods=["GET"])
def get_saldo_conta(id):
    conta = getConta(id)
    if conta is not None:
        return jsonify({"id": conta.id, "saldo": conta.saldo})
    else:
        return jsonify({"status": "FAIL", "mensagem": "Conta inexistente."}), 404

@app.route("/contas/<id>", methods=["POST"])
def post_deposito_saldo_conta(id):
    conta = getConta(id)
    if conta is not None:
        valor = request.form["valor"]
        json, error_code = conta.deposito(valor)
        return jsonify(json), error_code
    else:
        return jsonify({"status": "FAIL", "mensagem": "Conta inexistente."}), 404
   

@app.route("/contas/<id>", methods=["PUT"])
def put_saque_saldo_conta(id):
    conta = getConta(id)
    if conta is not None:
        valor = request.form["valor"]
        json, error_code = conta.saque(valor)
        return jsonify(json), error_code
    else:
        return jsonify({"status": "FAIL", "mensagem": "Conta inexistente."}), 404

@app.route("/contas/transferencia/<conta_origem>/<conta_destino>", methods=["POST"])
def post_transferencia_contas(conta_origem, conta_destino):
    conta_origem = getConta(conta_origem)
    conta_destino = getConta(conta_destino)
    if conta_origem is not None and conta_destino is not None:
        valor = request.form["valor"]
        json_origem, error_code_origem = conta_origem.saque(valor)
        if error_code_origem is 200:
            json_destino, error_code_destino = conta_destino.deposito(valor)
            return jsonify(json_destino), error_code_destino
        else:
            return jsonify(json_origem), error_code_origem
    else:
        return jsonify({"status": "FAIL", "valor_transferido": 0, "mensagem": "Conta inexistente."}), 404


if __name__ == "__main__":
    app.run(debug=True)