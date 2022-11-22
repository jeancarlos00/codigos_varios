import bs4
import requests

resultado = requests.get('https://escueladirecta.com/bog/260007/encapsulamiento')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title'))
