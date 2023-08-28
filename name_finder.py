import os
import pandas as pd

os.system('cls')
pasta_arquivos = r'**********************************************************'
string_procurada = '00000012345667'
coluna_pesquisa = 'CPF / CNPJ'
tipo_arquivo = '.xlsx'

dfs = []    

for arquivo in os.listdir(pasta_arquivos):
    if arquivo.endswith(tipo_arquivo):
        caminho_arquivo = os.path.join(pasta_arquivos, arquivo)
        df = pd.read_excel(caminho_arquivo,header=1)
        df['Origem'] = f'{arquivo}'
        dfs.append(df)

df_final = pd.concat(dfs, ignore_index=True)
df_final = df_final[df_final[coluna_pesquisa] == string_procurada]

print("Resultados da pesquisa:")
if int(len(df_final)) > 0:
    print(df_final[['Origem', coluna_pesquisa]])
else:
    print('Não obteve resultado!')
