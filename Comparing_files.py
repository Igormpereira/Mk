
import pandas as pd


# importing dataframe
csv1=pd.read_csv('C:\Igor\Comparando arquivos\\out_autoral-14-04-2022.csv', delimiter= ';')
csv2=pd.read_csv('T:\Publico\Igor_Maier\\out-autoral-20-10-2022.csv', delimiter= ';')
csvbase=pd.read_csv('C:\Igor\Comparando arquivos\\out_autoral_30_05_2022.csv', delimiter= ';')

#adding more '|' With info until hitting 30

csv1["Nova"]='|t'*40
csv2["Nova"]='|t'*40
csv1["related_isrc"]=csv1["related_isrc"]+csv1["Nova"]
csv2["related_isrc"]=csv2["related_isrc"]+csv2["Nova"]

#Dropping New
csv1=csv1.drop(["Nova"], axis=1)
csv2=csv2.drop(["Nova"], axis=1)

#split das colunas com barras
related_isrcnov1=csv1["related_isrc"].str.split("|", n = 30 , expand = True)
writersnov1=csv1["writers"].str.split("|", n = 5, expand = True)
related_isrcnov2=csv2["related_isrc"].str.split("|", n = 30, expand = True)
writersnov2=csv2["writers"].str.split("|", n = 5, expand = True)

#dropping
related_isrcnov1=related_isrcnov1.drop(30, axis=1)
#dropando
related_isrcnov2=related_isrcnov2.drop(30, axis=1)

x=1
i=1
z=1
a=1

# iterating to generate new columns
for related1 in related_isrcnov1.columns:
    csv1['related_isrcnov1' + str(i)] = related_isrcnov1[related1]
    i = i + 1

for writer1 in writersnov1.columns:
    csv1['writers1' + str(x)] = writersnov1[writer1]
    x = x + 1

for related2 in related_isrcnov2.columns:
    csv2['related_isrcnov1' + str(z)] = related_isrcnov2[related2]
    z = z + 1

for writer2 in writersnov2.columns:
    csv2['writers1' + str(a)] = writersnov2[writer2]
    a = a + 1


# dropping old columns
csv1.drop(columns =["related_isrc","writers"], inplace = True)
csv2.drop(columns =["related_isrc","writers"], inplace = True)

csv1=csv1.fillna ('t')
csv2=csv2.fillna ('t')

# transforming into a list
cabelçalho1=csv1.columns.values.tolist()
body1=csv1.values.tolist()
cabelçalho2=csv2.columns.values.tolist()
body2=csv2.values.tolist()
body1.insert(0,cabelçalho1)
body2.insert(0,cabelçalho2)
csv1=body1
csv2=body2

# Comparing two lists
diferença=[]
for elemento1 in csv2:
    if elemento1 not in csv1:
        diferença.append(elemento1)

# converting back to df
diferença= pd.DataFrame(diferença)

# renaming all columns
diferença.columns=['custom_id', 'asset_id', 'related_asset_id', 'iswc', 'title', 'add_asset_labels', 'hfa_song_code', 'match_policy', 'publisher_name', 'sync_ownership_share', 'sync_ownership_territory', 'sync_ownership_restriction', 'mechanical_ownership_share', 'mechanical_ownership_territory', 'mechanical_ownership_restriction', 'performance_ownership_share', 'performance_ownership_territory', 'performance_ownership_restriction', 'lyric_ownership_share', 'lyric_ownership_territory', 'lyric_ownership_restriction', 'related_isrcnov11', 'related_isrcnov12', 'related_isrcnov13', 'related_isrcnov14', 'related_isrcnov15', 'related_isrcnov16', 'related_isrcnov17', 'related_isrcnov18', 'related_isrcnov19', 'related_isrcnov110', 'related_isrcnov111', 'related_isrcnov112', 'related_isrcnov113', 'related_isrcnov114', 'related_isrcnov115', 'related_isrcnov116', 'related_isrcnov117', 'related_isrcnov118', 'related_isrcnov119', 'related_isrcnov120', 'related_isrcnov121', 'related_isrcnov122', 'related_isrcnov123', 'related_isrcnov124', 'related_isrcnov125', 'related_isrcnov126', 'related_isrcnov127', 'related_isrcnov128', 'related_isrcnov129', 'related_isrcnov130', 'writers11', 'writers12', 'writers13', 'writers14', 'writers15', 'writers16']


#iterate to return to initial form
diferença["related_isrc"] = diferença['related_isrcnov11']
diferença["writers"]=diferença["writers11"]
a=2
b=2

while a <= 30:
    diferença["related_isrc"] = diferença['related_isrc'] + '|' + diferença['related_isrcnov1' + str(a)]
    a=a+1


while b <= 6:
        diferença["writers"] = diferença["writers"] + '|' + diferença["writers1" + str(b)]
        b=b+1

# deleting columns
diferença.drop( ['related_isrcnov11', 'related_isrcnov12', 'related_isrcnov13', 'related_isrcnov14', 'related_isrcnov15', 'related_isrcnov16', 'related_isrcnov17', 'related_isrcnov18', 'related_isrcnov19', 'related_isrcnov110', 'related_isrcnov111', 'related_isrcnov112', 'related_isrcnov113', 'related_isrcnov114', 'related_isrcnov115', 'related_isrcnov116', 'related_isrcnov117', 'related_isrcnov118', 'related_isrcnov119', 'related_isrcnov120', 'related_isrcnov121', 'related_isrcnov122', 'related_isrcnov123', 'related_isrcnov124', 'related_isrcnov125', 'related_isrcnov126', 'related_isrcnov127', 'related_isrcnov128', 'related_isrcnov129', 'related_isrcnov130', 'writers11', 'writers12', 'writers13', 'writers14', 'writers15', 'writers16']
, axis=1, inplace=True)

#reorganizing df
diferença = diferença.reindex(columns=['custom_id', 'asset_id', 'related_isrc', 'related_asset_id', 'iswc', 'title', 'add_asset_labels', 'hfa_song_code', 'writers', 'match_policy', 'publisher_name', 'sync_ownership_share', 'sync_ownership_territory', 'sync_ownership_restriction', 'mechanical_ownership_share', 'mechanical_ownership_territory', 'mechanical_ownership_restriction', 'performance_ownership_share', 'performance_ownership_territory', 'performance_ownership_restriction', 'lyric_ownership_share', 'lyric_ownership_territory', 'lyric_ownership_restriction'])

# clearing column
#diferença['related_isrc']=diferença['related_isrc'].str.replace('|t|','')
#diferença['writers']=diferença['writers'].str.rstrip('|')
diferença['related_isrc']=diferença['related_isrc'].str.rstrip('|t|')
diferença['related_isrc']=diferença['related_isrc'].str.rstrip('ERRO X')
diferença['writers']=diferença['writers'].str.rstrip('|t|')
diferença=diferença.replace('t','')
diferença=diferença.replace(',',';')

#diferença.to_csv('diferença.csv',index=False,)
print(diferença)
diferença.to_csv('diferença.csv',index=False,sep=';')
exit()

print(diferença)

exit()





