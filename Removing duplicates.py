import pandas as pd

# importing dataframe
duplicado=pd.read_csv('C:\Igor\Comparando arquivos\Projeto remover duplicatas\\Agosto - Ebooks verificar - Página2.csv', delimiter= ',')

# removing duplicates
semdupl=duplicado.drop_duplicates()
#transformando em lista
duplicado=duplicado.values.tolist()
semdupl=semdupl.values.tolist()


#'Subtracting' one df from the other
for i in semdupl:
    duplicado.remove(i)

# returning to df
extraído=pd.DataFrame(duplicado)
semdupl=pd.DataFrame(semdupl)
extraído.columns = ['DATA VENDA', 'DATA RECEBIMENTO', 'LIVRO', 'LOJA', 'VL. UNIT. MÉDIO',
       'QT. VENDIDA', 'VALOR TOTAL','']
semdupl.columns = ['DATA VENDA', 'DATA RECEBIMENTO', 'LIVRO', 'LOJA', 'VL. UNIT. MÉDIO',
       'QT. VENDIDA', 'VALOR TOTAL','']



# csv
extraído.to_csv('extraído.csv',index=False,sep=',')
semdupl.to_csv('semdupl.csv',index=False,sep=',')






