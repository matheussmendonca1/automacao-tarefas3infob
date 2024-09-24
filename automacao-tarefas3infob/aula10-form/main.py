import pyautogui as ptg
import time

def preencher(atleta, modalidade, medalha, comite):

    campoAtleta = ptg.locateCenterOnScreen("aula10-form/atleta.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoAtleta, duration=0.7)
    ptg.write(atleta)

    campoModalidade = ptg.locateCenterOnScreen("aula10-form/modalidade.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoModalidade, duration=0.7)
    ptg.write(modalidade)

    campoMedalha = ptg.locateCenterOnScreen("aula10-form/medalha.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoMedalha, duration=0.7)
    ptg.write(medalha)

    campoComite = ptg.locateCenterOnScreen("aula10-form/comite.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoComite, duration=0.7)
    ptg.write(comite)

    campoEnviar = ptg.locateCenterOnScreen("aula10-form/enviar.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoEnviar, duration=0.7)

    time.sleep(2)

    campoOutra = ptg.locateCenterOnScreen("aula10-form/outra.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoOutra, duration=0.7)
