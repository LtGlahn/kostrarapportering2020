from datetime import datetime 

import geopandas as gpd 
import pandas as pd
import numpy as np
from copy import deepcopy

import STARTHER
import lastnedvegnett  
import skrivdataframe
import nvdbapiv3

t0 = datetime.now()

mittfilter = lastnedvegnett.filtersjekk(  )
mittfilter['vegsystemreferanse'] = 'Fv'
junk = mittfilter.pop( 'historisk', None)
mittfilter['egenskap'] = '1216=3615'

sok = nvdbapiv3.nvdbFagdata( 241 )
sok.filter( mittfilter )
data = sok.to_records( )
mydf = pd.DataFrame( data )

lengde = mydf.groupby( ['fylke', 'vegkategori', 'nummer' ]).agg( {'segmentlengde' : 'sum' } ).reset_index()
lengde['Veg'] = 'FV' + lengde['nummer'].astype(str)
lengde['Lengde (m)'] = lengde['segmentlengde']
lengde = lengde[[ 'fylke', 'Veg', 'Lengde (m)']]


# Henter et kontrolldatasett uten "adskilte løp"
filter2 = deepcopy( mittfilter )
filter2.pop( 'adskiltelop', None  )
sok2 = nvdbapiv3.nvdbFagdata( 241 )
sok2.filter( filter2 )
mydf2 = pd.DataFrame( sok2.to_records( ) )



# skrivdataframe.skrivdf2xlsx( lengde, 'Kostra 03 - Fylkesveg uten fast dekke.xlsx', sheet_name='Fv u fast dekkel', metadata=mittfilter)

tidsbruk = datetime.now() - t0 