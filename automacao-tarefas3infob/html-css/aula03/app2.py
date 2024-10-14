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
# campo_pesquisa.send_keys('como utilizar o selenium')

# pressiona a tecla enter
# campo_pesquisa.send_keys(Keys.ENTER)

# procura o botão "estou com sorte"
btn_estouComSorte = chrome.find_elements(By.NAME, 'btnI')
chrome.execute_script("arguments[0].value = 'Estava com azar';", btn_estouComSorte[1])
# btn_estouComSorte[1].click()

input('aperte enter para terminar...   ')
