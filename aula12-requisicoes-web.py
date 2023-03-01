import requests as rq
# Biblioteca alternativa - Beautiful Soup 4 BS4 - pip install bs4

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com.br'}
cookies = {'Ultima-visita': '17-02-2023'}
dados = {'username': 'guigui',
         'password': 'guigui123'}
texto = None

try:
    requisicao = rq.post('https://putsreq.com/3hCyDD1Y8a1OnLESXxHb',
                         headers=cabecalho,
                         cookies=cookies,
                         data=dados)
    texto = requisicao.text
except Exception as e:
    print('REQUISIÇÃO DEU ERRO:', e)

print(texto)
