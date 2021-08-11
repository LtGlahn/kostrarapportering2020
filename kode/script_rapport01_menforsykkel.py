from datetime import datetime 

import pandas as pd
import geopandas as gpd 
import numpy as np
from shapely import wkt

import STARTHER
import lastnedvegnett  
import skrivdataframe
import nvdbgeotricks
import nvdbapiv3


def fiksfeltoversikt( feltoversikt ):

    if isinstance( feltoversikt, float ):
        feltoversikt =  ''
    else: 
        feltoversikt = '#'.join( feltoversikt )

    return feltoversikt 

t0 = datetime.now()

# Det vanlige filteret for kjørbar veg:
# mittfilter = lastnedvegnett.filtersjekk(  )
# Det vanlige filteret ser slik ut: 
# {'sideanlegg': 'false',
#  'trafikantgruppe': 'K',
#  'detaljniva': 'VT,VTKB',
#  'adskiltelop': 'med,nei',
#  'typeveg': 'kanalisertVeg,enkelBilveg,rampe,rundkjøring,gatetun',
#  'historisk': 'true',
#  'tidspunkt': '2020-12-31',
#  'veglenketype': 'hoved'}


mittfilter = { 'historisk': 'true', 'tidspunkt': '2020-12-31'   }
# mittfilter['vegsystemreferanse'] = 'Ev,Rv,Fv,Kv,Sv,Pv'
mittfilter['vegsystemreferanse'] = 'Ev,Rv'
mittfilter['trafikantgruppe'] = 'G'

sok = nvdbapiv3.nvdbVegnett()
sok.filter( mittfilter )
mindf = pd.DataFrame( sok.to_records( ))
mindf['feltoversikt'] = mindf['feltoversikt'].apply( lambda x : fiksfeltoversikt( x ))
mindf['geometry'] = mindf['geometri'].apply( wkt.loads )
mindf.drop( columns=[ 'geometri', 'href', 'kortform', 'veglenkenummer', 'segmentnummer', 'startnode', 'sluttnode', 'referanse', 'målemetode', 'måledato' ], inplace=True  )
minGdf = gpd.GeoDataFrame( mindf, geometry='geometry', crs=5973 ) 


# minGdf = nvdbgeotricks.vegnett2gdf( mittfilter=mittfilter )
minGdf.to_file( 'ekstratall.gpkg', layer='sykkel_e_r', driver='GPKG')


# minGdf  = gpd.read_file( 'ekstratall.gpkg', layer='sykkel_e_r')
# lastnedvegnett.rapport01_medsykkel_gdf2excel( myGdf, filnavn='../kostraleveranse2020/Kostra 01 sykkel hele landet.xlsx', metadata=mittfilter)

minGdf['lengde'] = minGdf['lengde'] / 1000
lengdeCol = 'Lengde gang og sykkel (km)'
minGdf.rename( columns = {'lengde' :  lengdeCol }, inplace=True )


tellingFylke            = minGdf.groupby( ['fylke', 'trafikantgruppe' ]).agg( { lengdeCol : 'sum'} ).astype(int).reset_index()
tellingVegtype          = minGdf.groupby( ['trafikantgruppe', 'typeVeg' ]).agg( { lengdeCol : 'sum'} ).astype(int).reset_index()
tellingFylkeVegtype     = minGdf.groupby( ['fylke', 'trafikantgruppe', 'typeVeg' ]).agg( { lengdeCol : 'sum'} ).astype(int).reset_index()
tellingKommune          = minGdf.groupby( ['kommune', 'trafikantgruppe' ]).agg( { lengdeCol : 'sum'} ).astype(int).reset_index()
 

skrivdataframe.skrivdf2xlsx(  [ tellingFylke,   tellingVegtype,         tellingFylkeVegtype,        tellingKommune  ], '../Lengde gang og sykkelveg E R.xlsx', 
                sheet_name=[ 'G og S per fylke', 'G og S per vegtype', 'G og S per fylke og vegtype', 'G og S per kommune'  ], metadata=mittfilter)


tidsbruk = datetime.now() - t0 
print( "Tidsbruk:", tidsbruk, "sekund" )

print( "Lengde gang og sykkel", round( minGdf[lengdeCol].sum()), 'km'  )
# Lengde gang og sykkel 1572 km