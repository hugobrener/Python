import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

print('Digite o código do ativo: ')
ativo = input()
cotacao_empresa = web.DataReader(f'{ativo}.SA' , data_source = 'yahoo' , start = '10/01/2021' , end ='12/01/2021')
cotacao_empresa.pop('Adj Close')
cotacao_empresa.pop('High')
cotacao_empresa.pop('Low')
cotacao_empresa.pop('Volume')
df_excel = cotacao_empresa.to_excel(f'Área de Trabalho/cotacao_{ativo}.xlsx')
#cotacao_empresa
