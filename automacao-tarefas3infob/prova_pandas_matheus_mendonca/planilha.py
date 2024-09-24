import pandas as pd
import time

from main import preencher

plan = pd.read_excel('./planilhaLancamento.xlsx')
# print(plan)

planNome = plan[(plan['Nome'] == 'MATHEUS EVANGELISTA DE SOUZA MENDONçA')]
# print(planNome)

for (i, linha) in planNome.iterrows():
    preencher(linha['Nome'], linha['Atividade'], str(linha['Nota']), linha['Turma'])

    time.sleep(2)

