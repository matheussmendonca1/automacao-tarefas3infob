# importando as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# cria um objeto webDriver que vai manipular o Chrome
chrome = webdriver.Chrome()

# abre um endereço no navegador = get
chrome.get('http://google.com')


# procura um elemento comum ID - Caixa de pesquisa
campo_pesquisa = chrome.find_element(By.ID, 'APjFqb')

# digita um texto no campo de pesquisa
campo_pesquisa.send_keys('como utilizar o selenium')

# pressiona a tecla enter
# campo_pesquisa.send_keys(Keys.ENTER)

# procura o botão "estou com sorte"
btn_estouComSorte = chrome.find_elements(By.NAME, 'btnI')
btn_estouComSorte[1].click()

# executa um script no Chrome
# chrome.execute_script("document.body.style.backgroundColor = '#f45a44';")

# executa um script no Chrome 2ª Forma - Retorno de Valor
# variavel = chrome.execute_script('return document.title')
# print('O titulo da pagina é:  ', variavel)

#  executa um script no Chrome 3ª Forma - Retorno de Valor
# chrome.execute_script('arguments[0].click()', btn_estouComSorte)

# atividade - mudar a cor do botão para vermelho
# chrome.execute_script("arguments[0].style.backgroundColor = '#f45a44';", btn_estouComSorte)





# esperar digitar algo para fechar o navegador
input('Aperte enter para terminar')