# importando as bibliotecas
from selenium import webdriver

# cria um objeto webDriver que vai manipular o Chrome
chrome = webdriver.Chrome()

# abre um endereço no navegador = get
chrome.get('http://google.com')

# esperar digitar algo para fechar o navegador
input('Aperte enter para terminar')

