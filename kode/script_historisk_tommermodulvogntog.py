from datetime import datetime 

import geopandas as gpd 
import pandas as pd
import numpy as np
from copy import deepcopy

import STARTHER
import lastnedvegnett  
import skrivdataframe
import nvdbapiv3
import nvdbgeotricks

t0 = datetime.now()

#  EnumInSetProvider(904, 10913, 18256, 18254, 18255)
# 
# 19,50 18253 < Ikke denna, men resten
# 15,00 18254
# 12,40 18255
# Spesiell begrensning 18256


gpkgfil = '../data/tidsutvikling_bktommer900.gpkg'


mittfilter = { 'adskiltelop' :  'med,nei', 'sideanlegg' :  'false'  }
# mittfilter['vegsystemreferanse'] = 'Fv24,Fv21,E134,Fv6650'



sok = nvdbapiv3.nvdbFagdata( 900 )
sok.filter( mittfilter )

sok.filter( { 'tidspunkt' : '2020-11-15'} )
sok.refresh()
gdf_nov2020 = nvdbgeotricks.records2gdf( sok.to_records( ) ) 
gdf_nov2020 = gdf_nov2020[ gdf_nov2020['trafikantgruppe'] == 'K'].copy()
gdf_nov2020['tidspunkt'] = 'Nov 2020'
gdf_nov2020.to_file( gpkgfil, layer='bk900_nov2020', driver='GPKG')

sok.filter( { 'tidspunkt' : '2021-01-01'} )
sok.refresh()
gdf_jan2021 = nvdbgeotricks.records2gdf( sok.to_records( ) ) 
gdf_jan2021 = gdf_jan2021[ gdf_jan2021['trafikantgruppe'] == 'K'].copy()
gdf_jan2021['tidspunkt'] = 'Jan 2021'
gdf_jan2021.to_file( gpkgfil, layer='bk900_jan2021', driver='GPKG')

sok.filter( { 'tidspunkt' : '2021-04-02'} )
sok.refresh()
gdf_apr2021 = nvdbgeotricks.records2gdf( sok.to_records( ) ) 
gdf_apr2021 = gdf_jan2021[ gdf_jan2021['trafikantgruppe'] == 'K'].copy()
gdf_apr2021['tidspunkt'] = 'April 2021'
gdf_apr2021.to_file( gpkgfil, layer='bk900_apr2021', driver='GPKG')

myGdf  = pd.concat( [ gdf_nov2020, gdf_jan2021, gdf_apr2021   ])

myGdf.to_file( gpkgfil, layer='alletidspunkt', driver='GPKG')

lengde_alt =  myGdf.groupby( [ 'tidspunkt',  'Tillatt for modulvogntog' ] ).agg( { 'segmentlengde' : 'sum'  } ).reset_index( )
lengde_alt['segmentlengde'] = lengde_alt['segmentlengde'] / 1000
lengde_alt.rename( columns={'segmentlengde' : 'Lengde (km)'}, inplace=True )

lengde_vegkategori =  myGdf.groupby( [ 'tidspunkt', 'vegkategori', 'Tillatt for modulvogntog' ] ).agg( { 'segmentlengde' : 'sum'  } ).reset_index( )
lengde_vegkategori['segmentlengde'] = lengde_vegkategori['segmentlengde'] / 1000
lengde_vegkategori.rename( columns={'segmentlengde' : 'Lengde (km)'}, inplace=True )

lengde_fylke =  myGdf.groupby( [ 'tidspunkt', 'fylke', 'Tillatt for modulvogntog' ] ).agg( { 'segmentlengde' : 'sum'  } ).reset_index( )
lengde_fylke['segmentlengde'] = lengde_fylke['segmentlengde'] / 1000
lengde_fylke.rename( columns={'segmentlengde' : 'Lengde (km)'}, inplace=True )

lengde_fylke_vegkat =  myGdf.groupby( [ 'tidspunkt', 'fylke', 'vegkategori', 'Tillatt for modulvogntog' ] ).agg( { 'segmentlengde' : 'sum'  } ).reset_index( )
lengde_fylke_vegkat['segmentlengde'] = lengde_fylke_vegkat['segmentlengde'] / 1000
lengde_fylke_vegkat.rename( columns={'segmentlengde' : 'Lengde (km)'}, inplace=True )

skrivdataframe.skrivdf2xlsx( [ lengde_alt, lengde_vegkategori, lengde_fylke, lengde_fylke_vegkat  ], 
                            '../data/endringer_tillattmodulvogntog.xlsx', 
                            sheet_name=[ 'Norge', 'Norge per vegkategori', 'Fylke', 'Fylke per vegkategori' ] )

#     # For debugging 
#     lengde = myGdf.groupby( ['fylke', 'vegkategori', 'nummer', 'Tillatt for modulvogntog']).agg( {'segmentlengde' : 'sum' } ).reset_index()

#     lengde['Veg'] = 'FV' + lengde['nummer'].astype(str)
# lengde['Lengde (m)'] = lengde['segmentlengde']
# lengde = lengde[[ 'fylke', 'Veg', 'Lengde (m)']]

# telling = myGdf.groupby( ['fylke' ]).agg( { 'segmentlengde' : 'sum'} ).astype(int).reset_index()  
# telling.rename( columns={ 'segmentlengde' : 'Lengde (m)' }, inplace=True)

# skrivdataframe.skrivdf2xlsx( telling, '../../output/Kostra 08 - maks lengde u 19m.xlsx', sheet_name='Fv lengde u 19,5m', metadata=mittfilter)

# tidsbruk = datetime.now() - t0 