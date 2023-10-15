import requests


def urlacesso(url):
	try:
		get = requests.get(url)
		print(f'Consegui acessar \'{url}\' com sucesso!')
	except:
		print('Não consegui acessar o site informado')


urlacesso('http://pudim.com.br/')
