import requests
import json

try:
    request = requests.get("https://my-api.rafaelcardozo1.repl.co/pegarvendas")
except:
    print(f'{request}')
else:
    print(request)
    print(f'The total amount of sellings was: R$ {request.json()["total_vendas"]:.2f}')