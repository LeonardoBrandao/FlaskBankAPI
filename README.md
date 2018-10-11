# API de contas bancárias

Uma api simples para interagir com um array de contas.

# Instalação dos requisitos e configurações

Observação: Esse tutorial é feito com base em sistemas unix

O projeto usa Python com o framework [Flask](http://flask.pocoo.org/).
  - Verificar que tenha Python 3.4 ou superior instalado. 
```sh
    $ python --version
```
  - Caso não tenha, você pode baixá-lo [aqui](https://www.python.org/downloads/release/python-370/)

Agora devemos usar o package manager do python (pip) para instalar o virtualenv e isolar as dependências do nosso projeto

```sh
    $ sudo pip install virtualenv
```

Pronto, agora podemos clonar o projeto e criar nosso ambiente virtual

```sh
    $ git clone https://github.com/LeonardoBrandao/FlaskBankAPI.git
    $ cd FlaskBankAPI
    $ sudo virtualenv venv
    $ source ./venv/bin/activate
```
Com o ambiente criado e ativado, vamos instalar suas dependências

```sh    
    $ pip install -r requirements.txt
```

# Rodando o servidor local

Iniciando o servidor local

```sh
    $ python ./server.py
```

Pronto, agora já podemos fazer requisições para a API. 

Verifique se o servidor está rodando na url

```sh
    127.0.0.1:5000
```

# Fazendo requisições

### Usando ```client.py```

Para fazer uma requisição, podemos rodar o arquivo ```client.py``` com os seguintes parametros.

```sh
    $ python ./client.py <host> <porta> <operacao> <parametros da operacao>
```

| Parâmetros |  |
| ------ | ------ |
| host | url do servidor |
| porta | porta que o serviço está rodando |
| operacao | consultar a tabela abaixo |
| parametros da operacao | consultar a tabela abaixo |

| Operação | Parâmetros da operação |
| ------ | ------ |
| saldo | id_conta |
| saque | id_conta valor |
| deposito | id_conta valor |
| transferencia | id_conta_origem id_conta_destino valor |

Lembrando que os parametros devem ser separados por espaço

Assim, podemos fazer a seguinte requisição

```sh
    $ python ./client.py localhost 5000 transferencia 1 2 350
```

Para usar o arquivo .sh de testes, rodar

```sh
    $ sudo sh ./script.sh
```

### Usando Postman

Postman é uma ferramenta para fazer requisições à API's.

Caso deseje ver o JSON de resposta, é necessário usar o Postman ou alguma ferramenta similar para realizar as requisições, já que o arquivo ```client.py``` faz a tratativa dos resultados das requisições.

# Documentação
Para consultar a documentação da API abra o arquivo ```api_doc.html``` localizado na pasta docs

# Integrantes

Leonardo L. R. T. Brandão - 31633528
Felipe Estrela Cardoso - 31618375
