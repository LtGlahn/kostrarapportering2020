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

# Lagrer data for midtrekkverk
sterkfilter = lastnedvegnett.kostraFagdataFilter( mittfilter={ 'egenskap' : '1248=11789'} )
sok = nvdbapiv3.nvdbFagdata( 5 )
sok.filter( sterkfilter ) 
myrecords = sok.to_records( )
mydf = pd.DataFrame( myrecords )

nvdbgeotricks.records2gpkg( myrecords, 'vegoppmerking.gpkg', 'vegoppmerking' )
# vegmerklendge = vegmerk.groupby( ['fylke' ]).agg( { 'nvdbId': 'nunique', 'segmentlengde' : 'sum' } ).reset_index()
# vegmerklendge.rename( columns={ 'nvdbId' : 'Antall', 'segmentlengde' : 'Lengde (m)' }, inplace=True )
# skrivdataframe.skrivdf2xlsx( vegmerklendge, '../../output/Kostra 20 - Midtrekkverk 2 eller 3 felt.xlsx', 
#                                 sheet_name='FV med forsterket vegmerking', metadata=sterkfilter)

tidsbruk = datetime.now() - t0 