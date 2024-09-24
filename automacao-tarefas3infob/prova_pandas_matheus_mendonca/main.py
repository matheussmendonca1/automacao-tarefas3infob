import pyautogui as ptg
import time


def preencher(nome, atividade, nota, turma):
    campoRegistrar = ptg.locateCenterOnScreen("./registrar.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoRegistrar, duration=0.7)

    campoNome = ptg.locateCenterOnScreen("./nome-aluno.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoNome, duration=0.7)
    ptg.write(nome)

    campoAtividade = ptg.locateCenterOnScreen("./atividade.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoAtividade, duration=0.7)
    ptg.write(atividade)

    campoNota = ptg.locateCenterOnScreen("./nota.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoNota, duration=0.7)
    ptg.write(nota)

    ptg.scroll(-300)

    campoTurma = ptg.locateCenterOnScreen("./3infob.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoTurma, duration=0.7)
    ptg.write(turma)

    campoEnviar = ptg.locateCenterOnScreen("./enviar.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoEnviar, duration=0.7)

    time.sleep(2)

    campoOutra = ptg.locateCenterOnScreen("./outra.png", 
                                        grayscale=True, 
                                        confidence=0.9)
    ptg.click(campoOutra, duration=0.7)
