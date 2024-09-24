import pandas as pd
import time
from main import preencher

plan = pd.read_excel('aula10-form/dados.xlsx')

for (i, linha) in plan.iterrows():
    preencher(linha['Atleta'], linha['Modalidade'], linha['Medalha'], linha['Comitê'])

    time.sleep(2)
