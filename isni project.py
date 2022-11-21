import json
import requests
import pandas as pd

# importing csv for crossover
cringer = pd.read_csv('C:\Igor\Arquivos base joao\Consulta-Cringer tabela MK - MK (1).csv')
# removing the duplicates
cringer = cringer.drop_duplicates(subset='artist_name')
# Splitting columns to enter each part of the name separately
base = cringer["artist_name"].str.split(" ", n=6, expand=True)
cringer["nome"] = base[0]
cringer["sobrenome"] = base[1]
cringer["terceironome"] = base[2]
cringer["quartonome"] = base[3]
cringer["quintonome"] = base[4]
cringer["sextonome"] = base[5]
# extracting artist names
# cringer['artist_name'].to_csv('Artistas.csv', index=False)

# loop to iterate name by name
for indice, linha in cringer.iterrows():

    nome = str(linha['nome'])
    sobrenome = str(linha['sobrenome'])
    terceironome = str(linha['terceironome'])
    quartonome = str(linha['quartonome'])
    quintonome = str(linha['quintonome'])
    sextonome = str(linha['sextonome'])

   
def isni():
    if str(linha['sobrenome'])==str(None):
        requestisni= requests.get('http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-jsonld&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(nome))
        print(requestisni.content)
    elif str(linha['terceironome'])==str(None):
        requestisni= requests.get('http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}+{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-jsonld&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(nome,sobrenome))
        print(requestisni.content)
    elif str(linha['quartonome'])==str(None):
        requestisni= requests.get('http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}+{}+{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-jsonld&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(nome,sobrenome,terceironome))
        print(requestisni.content)
    elif str(linha['quintonome'])==str(None):
        requestisni= requests.get('http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}+{}+{}+{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-jsonld&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(nome,sobrenome,terceironome,quartonome))
        print(requestisni.content)
    elif str(linha['sextonome'])==str(None):
        requestisni= requests.get('http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}+{}+{}+{}+{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-jsonld&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(nome,sobrenome,terceironome,quartonome,quintonome))
        print(requestisni.content)
    elif str(linha['sextonome'])!=str(None):
        requestisni= requests.get('http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}+{}+{}+{}+{}+{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-jsonld&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(nome,sobrenome,terceironome,quartonome,quintonome,sextonome))
        print(requestisni.content)

def musica():
    if str(linha['sobrenome']) == str(None):
        requestisni = requests.get(
            'http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-b&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(
                nome))
        print(requestisni.content)
    elif str(linha['terceironome']) == str(None):
        requestisni = requests.get(
            'http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}+{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-b&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(
                nome, sobrenome))
        print(requestisni.content)

    elif str(linha['quartonome']) == str(None):
        requestisni = requests.get(
            'http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}+{}+{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-b&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(
                nome, sobrenome, terceironome))
        print(requestisni.content)
    elif str(linha['quintonome']) == str(None):
        requestisni = requests.get(
            'http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}+{}+{}+{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-b&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(
                nome, sobrenome, terceironome, quartonome))
        print(requestisni.content)
    elif str(linha['sextonome']) == str(None):
        requestisni = requests.get(
            'http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}+{}+{}+{}+{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-b&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(
                nome, sobrenome, terceironome, quartonome, quintonome))
        print(requestisni.content)
    elif str(linha['sextonome']) != str(None):
        requestisni = requests.get(
            'http://isni.oclc.org/sru/DB=1.2/?query=pica.na+%3D+%22{}+{}+{}+{}+{}+{}%22&version=1.1&operation=searchRetrieve&stylesheet=http%3A%2F%2Fisni.oclc.org%2Fsru%2FDB%3D1.2%2F%3Fxsl%3DsearchRetrieveResponse&recordSchema=isni-b&maximumRecords=10&startRecord=1&recordPacking=xml&sortKeys=none&x-info-5-mg-requestGroupings=none'.format(
                nome, sobrenome, terceironome, quartonome, quintonome, sextonome))
        print(requestisni.content)
def nome():
    # importando csv para cruzamento
    cringer = pd.read_csv('T:\Publico\Igor_Maier\\Consulta-Cringer tabela MK - MK 2.csv')
    # Tirando as duplicatas
    cringer = cringer.drop_duplicates(subset='artist_name')
    # Gerando arquivo txt
    cringer['artist_name'].to_csv("Nomes.txt", index=False, encoding="utf-8")



isni()
musica()
nome()
   

