# API de contas bancárias

Uma api simples para interagir com um array de contas.

# Instalação dos requisitos e configurações

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

Pronto, agora podemos criar nosso ambiente virtual

```sh
    $ sudo virtualenv venv
    $ source venv/bin/activate
```
Com o ambiente criado e ativado, vamos clonar nosso projeto e instalar suas dependências

```sh
    $ git clone https://github.com/LeonardoBrandao/FlaskBankAPI.git
    $ cd FlaskBankAPI
    $ pip install -r requirements.txt
```

# Rodando o servidor local e fazendo requisições

Iniciando o servidor local

```sh
    $ python ./server.py
```

Pronto, agora já podemos fazer requisições para a API. 

Verifique se o servidor está rodando na url

```sh
    127.0.0.1:5000
```

Caso deseje usar o arquivo .sh de testes, rodar

```sh
    $ sudo sh ./script.sh
```

# Documentação
Para consultar a documentação da API abra o arquivo ```api_doc.html``` localizado na pasta docs
