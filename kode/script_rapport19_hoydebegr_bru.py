from datetime import datetime 
from copy import deepcopy 

import geopandas as gpd 
import pandas as pd
import numpy as np

import STARTHER
import lastnedvegnett  
import skrivdataframe
import nvdbapiv3

t0 = datetime.now()
mittfilter = lastnedvegnett.kostraFagdataFilter( { 'egenskap' : ' 5277 < 4 AND ( 5270=8168 OR 5270=8149 ) ', 'overlapp' : '60'} )
sok = nvdbapiv3.nvdbFagdata( 591 )
sok.filter( mittfilter  ) 
mydf = pd.DataFrame( sok.to_records( ) )
telling = mydf.groupby( ['fylke' ]).agg( { 'nvdbId': 'nunique', 'segmentlengde' : 'sum'} ).reset_index()
telling.rename( columns={ 'nvdbId' : 'Antall', 'segmentlengde' : 'Lengde (m)' }, inplace=True )


skrivdataframe.skrivdf2xlsx( telling, 'Kostra 19 - Bruer hoyde mindre enn 4m.xlsx', 
                                sheet_name='Bru høydebegrensning under 4m', metadata=mittfilter)

tidsbruk = datetime.now() - t0 