import requests
import json


print("COTATION OF THE USD, EURO, BITCOIN IN RELATION WITH THE BRAZILIAN REAL")
try:
    cotation = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
except (urllib3.exceptions.NewConnectionError, socket.gaierror, urllib3.exceptions.MaxRetryError, requests.exceptions.ConnectionError):
    print("Couldn't get the response: Error 404")
cotation = cotation.json()
print(f'US$ = R$ {cotation["USDBRL"]["bid"]}\n€ = R$ {cotation["EURBRL"]["bid"]}\n₿ = R$ {cotation["BTCBRL"]["bid"]}')
