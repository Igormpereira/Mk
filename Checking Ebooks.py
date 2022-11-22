import pandas as pd

# reading df skipping bad lines and showing errors on initial read
csv1 = pd.read_csv(r'C:\Users\Andrea\Desktop\IGOR\Verificação critérios csv\TOTVS_EBOOKS_2022_09_20221007_0003.csv', delimiter=';',error_bad_lines=False, warn_bad_lines=True,encoding = 'utf-8', dtype=str)

# replacing NAN
csv1 = csv1.fillna('0')



# checking the csv according to the parameters - iterating line by line in specific column

a=''
a1=''
a2=''
a3=''
a4=''
a5=''
a6=''


i=0
for indice, linha in csv1.iterrows():

    i=i+1


    if  "." in str(linha['livro_id']):#ok
        a =a+"'livro_id', linha:{}, ".format(indice+2)
    else:
        a=a+''
    if "." in str((linha['parceiro'])):#ok
        a1 =a1+"'parceiro' linha:{}, ".format(indice + 2)
    else:
        a1=a1+''
    if len(linha['date']) != 10:#ok
        a2 =a2+"'date' linha:{}, ".format(indice + 2)
    else:
        a2=a2+''
    if len(linha['paydate']) != 10:#ok
        a3 =a3+"'paydate' linha:{}, ".format(indice + 2)
    else:
        a3=a3+''
    #if len(str(linha['isbn'])) != x and  str(linha['isbn'])!=0:#tem tamanho especifico ou so deixo como comentario
    #    a4 =a4+"'data_referencia' linha:{}, ".format(indice + 2)
    #else:
    #    a4=a4+''
    if "." in str(linha['qtd']):#ok
        a5 =a5+"'qtd' linha:{}, ".format(indice + 2)
    else:
        a5=a5+''
    if str(linha['val']) == '0' or str(linha['val']) == "00":#ok
        a6 = a6 + "'val' linha:{}, ".format(indice + 2)
    else:
        a6 = a6 + ''


listaerros=[a,a1,a2,a3,a4,a5,a6]

#print(listaerros)
