# importação do webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import wget


# cria um dataframe vazio com as colunas relacionadas com os dados coletados do site
planilha = pd.DataFrame(columns=['Numero', 'Nome', 'Altura', 'Imagem'])

# criar um objeto para manipular o navegador
chrome = webdriver.Chrome()

# abrir uma página no Chrome

contador = 0
chrome.get("https://sg.portal-pokemon.com/play/pokedex/0001")

while contador < 10:

    # procurar pelo elemento que possui o codigo do pokemon
    elementNumero = chrome.find_element(By.CLASS_NAME, 'pokemon-slider__main-no')

    # procurar pelo elemento que possui o nome do pokemon
    elementNome = chrome.find_element(By.CLASS_NAME, 'pokemon-slider__main-name')

    # procura pela altura do pokemon
    elementAltura = chrome.find_element(By.CSS_SELECTOR, '.pokemon-info__height .pokemon-info__value')

    # procurar pela imagem
    elementImage = chrome.find_element(By.CLASS_NAME, "pokemon-img__front")
    endercoImage = elementImage.get_attribute('src')

    # cria um novo nome para a imagem
    urlNavegador = chrome.current_url
    numeroPokemonVersao = urlNavegador.split('/')[-1]
    extensaoImg = endercoImage.split('.')[-1]
    nomeImagem = numeroPokemonVersao + "." + extensaoImg
    ondeSalvar = "aula04\\img\\" + nomeImagem

    wget.download(endercoImage, ondeSalvar)

    print("Número:", elementNumero.text)
    print("Nome:", elementNome.text)
    print("Altura:", elementAltura.text)

    # adiciona os dados na planilha
    planilha.loc[contador] = [elementNumero.text, elementNome.text,  elementAltura.text, nomeImagem]

    # seleciona o botao para o proximo pokemon
    btnNext = chrome.find_element(By.CSS_SELECTOR, ".pokemon-slider__wrapper--right >  a")
    chrome.execute_script('arguments[0].click()', btnNext)
    
    contador += 1

# salva a planilha em formato de excel
planilha.to_excel('pokemons.xlsx', index=False)

# mantem a página aberta
input()
