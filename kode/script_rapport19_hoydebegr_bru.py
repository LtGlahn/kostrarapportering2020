from datetime import datetime 
from copy import deepcopy 

import geopandas as gpd 
import pandas as pd
import numpy as np

import STARTHER
import lastnedvegnett  
import skrivdataframe
import nvdbapiv3
import nvdbgeotricks

t0 = datetime.now()
mittfilter = lastnedvegnett.kostraFagdataFilter( { 'egenskap' : ' 5277 < 4 AND ( 5270=8168 OR 5270=8149 ) ', 'overlapp' : '60(1263=7304)'} )
# mittfilter = lastnedvegnett.kostraFagdataFilter( { 'overlapp' : '591(5277 < 4 AND ( 5270=8168 OR 5270=8149 ) ) ', 'egenskap' : '1263=7304'} )
sok = nvdbapiv3.nvdbFagdata( 591 )
sok.filter( mittfilter  ) 
myGdf = nvdbgeotricks.records2gdf( sok.to_records( ) )

# telling = myGdf.groupby( ['fylke' ]).agg( { 'nvdbId': 'nunique' } ).reset_index()
# telling = myGdf.groupby( ['fylke' ]).agg( { 'nvdbId': 'nunique', 'segmentlengde' : 'sum'} ).reset_index()
# telling.rename( columns={ 'nvdbId' : 'Antall', 'segmentlengde' : 'Lengde (m)' }, inplace=True )

# Henter bruer
myGdf['stedfesting'] = myGdf['startposisjon'].astype(str) + '-' + myGdf['sluttposisjon'].astype(str) + '@' + myGdf['veglenkesekvensid'].astype(str)
stedfesting = ','.join( list( set( list( myGdf['stedfesting'] ))) )
brusok = nvdbapiv3.nvdbFagdata(60 )
brufilter = lastnedvegnett.kostraFagdataFilter( { 'egenskap' : '1263=7304',  'veglenkesekvens' : stedfesting }  )
brusok.filter( brufilter )
bruGdf = nvdbgeotricks.records2gdf( brusok.to_records()  )

bruGdf.to_file( 'brudebug.gpkg', layer='bru_u_4m', driver='GPKG')
myGdf.to_file( 'brudebug.gpkg', layer='hoydebegrensning', driver='GPKG')

# Oppsummerer bru. Alle bruene her har verdi for egenskapen Lengde, så dropper dem som er delt i flere segmenter. 
bruGdf = bruGdf.drop_duplicates( subset='nvdbId')
telling = bruGdf.groupby( ['fylke' ]).agg( { 'nvdbId': 'nunique', 'Lengde' : 'sum'} ).reset_index()
telling.rename( columns={ 'nvdbId' : 'Antall', 'lengde' : 'Lengde (m)' }, inplace=True )

brufilter['egenskapfilter_bru'] = brufilter.pop( 'egenskap' )
brufilter['overlapp fra søk etter høydebegrensning'] = brufilter.pop( 'veglenkesekvens' )
brufilter
samlafilter = { **mittfilter, **brufilter }

skrivdataframe.skrivdf2xlsx( telling, 'Kostra 19 - Bruer hoyde mindre enn 4m.xlsx', 
                                sheet_name='Bru høydebegrensning under 4m', metadata=samlafilter)

tidsbruk = datetime.now() - t0 