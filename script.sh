#!/bin/bash

python3 client.py localhost 5000 saldo 1
python3 client.py localhost 5000 saque 1 200
python3 client.py localhost 5000 saldo 1
python3 client.py localhost 5000 deposito 1 500
python3 client.py localhost 5000 saldo 1
python3 client.py localhost 5000 transferencia 1 2 800
python3 client.py localhost 5000 saldo 2
python3 client.py localhost 5000 saque 2 100
python3 client.py localhost 5000 saldo 2
python3 client.py localhost 5000 saldo 9
python3 client.py localhost 5000 saldo -1
python3 client.py localhost 5000 saque 1 -123
python3 client.py localhost 5000 transferencia 1 2 2000
python3 client.py localhost 5000 saldo 1
python3 client.py localhost 5000 saldo 2