import requests
import ast
import sys

def arg_assign(i):    
    try:
        return str(sys.argv[i])
    except:
        return None

ip = arg_assign(1)
porta = arg_assign(2)
op = arg_assign(3)
p1 = arg_assign(4)
p2 = arg_assign(5)
p3 = arg_assign(6)

def run_request():
    if op == 'saldo':
        url = 'http://'+ ip + ':' + porta + '/contas/' + str(p1)
        r = requests.get(url)
        rJson = ast.literal_eval(r.text)
        if r.status_code == 200:
            print('Saldo da conta {}: R${}'.format(p1, rJson['saldo']))
        else:
            print('Falha na operacao {}. {}'.format(op, rJson['mensagem']))

    elif op == 'deposito':
        url = 'http://'+ ip + ':' + porta + '/contas/' + str(p1)
        r = requests.post(url, data={'valor': p2})
        rJson = ast.literal_eval(r.text)
        if r.status_code == 200:
            print('Deposito de R${} na conta {}'.format(p2, p1))
        else:
            print('Falha na operacao {}. {}'.format(op, rJson['mensagem']))

    elif op == 'saque':
        url = 'http://'+ ip + ':' + porta + '/contas/' + str(p1)
        r = requests.put(url, data={'valor': p2})
        rJson = ast.literal_eval(r.text)
        if r.status_code == 200:
            print('Saque de R${} na conta {}.'.format(p2, p1))
        else:
            print('Falha na operacao {}. {}'.format(op, rJson['mensagem']))

    elif op == 'transferencia':
        url = 'http://'+ ip + ':' + porta + '/contas/transferencia/' + str(p1) + '/' + str(p2)
        r = requests.post(url, data={'valor': p3})
        rJson = ast.literal_eval(r.text)
        if r.status_code == 200:
            print('Transferencia de R${} da conta {} para a conta {}.'.format(p3, p1, p2))
        else:
            print('Falha na operacao {}. {}'.format(op, rJson['mensagem']))
    else:
        print('Opcao inválida.')



if __name__ == '__main__':
    run_request()