import pandas
import pandas as pd
import os
import pandas as pd
import numpy as np

dfcriger=pd.read_csv('C:\Igor\Arquivos base joao/Consulta-Cringer tabela MK - MK.csv',low_memory=False)
youtubeasset=pd.read_csv('C:\Igor\Arquivos base joao\Youtube.csv',low_memory=False)
df1=pd.read_csv('C:\Igor\Arquivos base joao\\Big Query.csv',low_memory=False)


#filtering
Comisrccomupcsemasset1=df1.query("s_isrc!=' ' and s_upc!=' ' and s_assetid==' '")
Comisrccomupccomasset2=df1.query("s_isrc!=' ' and s_upc!=' ' and s_assetid!=' '")
Comisrcsemupcsemasset3=df1.query("s_isrc!=' ' and s_upc==' ' and s_assetid==' '")
Comisrcsemupccomasset4=df1.query("s_isrc!=' ' and s_upc==' ' and s_assetid!=' '")
Comupcsemisrcsemasset5=df1.query("s_isrc==' ' and s_upc!=' ' and s_assetid==' '")
Comupcsemisrccomasset6=df1.query("s_isrc==' ' and s_upc!=' ' and s_assetid!=' '")
ComAssetsemupcsemisrc7=df1.query("s_isrc==' ' and s_upc==' ' and s_assetid!=' '")
testenov1=Comisrccomupcsemasset1.append([Comisrccomupccomasset2,Comisrcsemupcsemasset3,Comisrcsemupccomasset4,Comupcsemisrcsemasset5,Comupcsemisrccomasset6,ComAssetsemupcsemisrc7])

#merging tables with cringer

dfcriger['s_upc'] = dfcriger['s_upc'].astype(str)
#dfcomisrcsemupc['s_upc'] = dfcomisrcsemupc['s_upc'].astype(str)

mescomisrccomupcsemasset1=pd.merge(Comisrccomupcsemasset1, dfcriger,how='left',on = ['s_isrc','s_upc'])
mesComisrccomupccomasset2=pd.merge(Comisrccomupccomasset2, dfcriger,how='left',on = ['s_isrc','s_upc'])
mesComisrcsemupcsemasset3=pd.merge(Comisrcsemupcsemasset3, dfcriger,how='left',on = ['s_isrc','s_upc'])
mesComisrcsemupccomasset4=pd.merge(Comisrcsemupccomasset4, dfcriger,how='left',on = ['s_isrc','s_upc'])
mesComupcsemisrcsemasset5=pd.merge(Comupcsemisrcsemasset5, dfcriger,how='left',on = ['s_isrc','s_upc'])
mesComupcsemisrccomasset6=pd.merge(Comupcsemisrccomasset6, dfcriger,how='left',on = ['s_isrc','s_upc'])
mesComAssetsemupcsemisrc7=pd.merge(ComAssetsemupcsemisrc7, youtubeasset ,how='left',on = ['s_assetid','s_upc','s_isrc'])



mesComAssetsemupcsemisrc7.drop(['approx_daily_views', 's_assetid', 'asset_type', 'status', 'metadata_origination',
                                'custom_id', 's_isrc', 'grid', 's_upc', 'artist_name',  'label',
                                'constituent_asset_id', 'active_reference_id', 'inactive_reference_id', 'match_policy',
                                'is_merged', 'ownership', 'conflicting_country_code', 'embedded_asset_id', 'asset_label',
                                'active_claims'],axis=1, inplace=True)
final=mescomisrccomupcsemasset1.append([mesComisrccomupccomasset2,mesComisrcsemupcsemasset3,mesComisrcsemupccomasset4,mesComupcsemisrcsemasset5,mesComupcsemisrccomasset6,mesComAssetsemupcsemisrc7])


print(final)
