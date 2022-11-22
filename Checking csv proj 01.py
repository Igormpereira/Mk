import pandas as pd

# reading df skipping bad lines and showing errors on initial read
csv1 = pd.read_csv(r'C:\Users\Andrea\Desktop\IGOR\Verificação critérios csv\TOTVS_ART_2022_09_20221014_1700.csv', delimiter=';',error_bad_lines=False, warn_bad_lines=True)

# replacing NAN
csv1 = csv1.fillna('0')
#print(csv1.columns)
#exit()


# checking the csv according to the parameters - iterating line by line in specific column

for indice, linha in csv1.iterrows():
    #print(list(str((linha['upc']))))

    if linha['vazio'] != '0':
        raise Exception(Exception, "Coluna 0 'Vazio', linha:", indice+2)
    if indice + 1 != linha['seq']:
        raise Exception(Exception, "Primeira  coluna 'seq', linha:", indice+2)
    if len(linha['data']) != 8:
        raise Exception(Exception, "Segunda  coluna 'data', linha:", indice+2)
    if len(linha['mes_pagamento']) != 10:
        raise Exception(Exception, "Terceira   coluna 'mes_pagamento', linha:", indice+2)
    if linha['data_referencia'] != '0':
        raise Exception(Exception, "Quarta coluna 'data_referencia', linha:", indice+2)
    if len(linha['isrc']) != 12:
        raise Exception(Exception, "Quinta coluna 'isrc', linha:", indice+2)
    if linha['iswc'] != '0':
        raise Exception(Exception, "Sexta coluna 'iswc', linha:", indice+2)
    if len(str((linha['upc']))) != 15 and linha['upc'] != "0":
        raise Exception(Exception, "Sétima coluna 'upc', linha:", indice+2)
    if linha['valor_total'] != '0' and '.' not in list(str(linha['valor_total'])):
        raise Exception(Exception, "Oitava coluna 'valor_total', linha:", indice+2)
    if '.' in list(str(linha['qtd'])):
        raise Exception(Exception, "Nona coluna 'qtd', linha:", indice+2)
    if len(str(linha['tipo'])) > 3:
        raise Exception(Exception, "Decima coluna  coluna 'tipo', linha:", indice+2)
    if len(str(linha['parceiro'])) > 3:
        raise Exception(Exception, "Decima primeira coluna  'parceiro', linha:", indice+2)
    if linha['art_ou_aut'] != 'ART':
        raise Exception(Exception, "Décima segunda coluna 'art_ou_aut' , linha:", indice+2)
    if linha['regra'] != 'DD':
        raise Exception(Exception, "Décima terceira coluna 'regra' , linha:", indice+2)
