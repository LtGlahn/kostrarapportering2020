from datetime import datetime 

import geopandas as gpd 

import STARTHER
import lastnedvegnett  
import skrivdataframe
import nvdbgeotricks

t0 = datetime.now()

mittfilter = lastnedvegnett.filtersjekk(  )
mittfilter['vegsystemreferanse'] = 'Fv'
# mittfilter.pop( 'kryssystem', None )
mittfilter.pop( 'sideanlegg', None )

myGdf = nvdbgeotricks.firefeltrapport( mittfilter=mittfilter, felttype='K' )
myGdf['Lengde kollektivfelt'] = myGdf['kollektivfelt_antsider'] * myGdf['lengde']
# statistikk = myGdf.groupby( ['fylke'] ).agg( { 'lengde' : 'sum', 'Lengde kollektivfelt' : 'sum' } )
statistikk = myGdf.groupby( ['fylke'] ).agg( { 'Lengde kollektivfelt' : 'sum' } ).reset_index()
skrivdataframe.skrivdf2xlsx( statistikk, 'Kostra 25 - Fylkesveg med kollektivfelt.xlsx', sheet_name='Fylkesveg med kollektivfelt', metadata=mittfilter)


# myGdf.to_file( 'kostraleveranser.gpkg', layer='kollektivfelt', driver='GPKG')
# myGdf  = gpd.read_file( 'kostraleveranser.gpkg', layer='kollektivfelt')
# lastnedvegnett.rapport01_gdf2excel( myGdf, filnavn='../kostraleveranse2020/Kostra 01 - Vegnett hele landet.xlsx', metadata=mittfilter)


# Kontrolldatasett, brukes for å etterprøve hva vi får fra NVDB rapporter.  
kontrollfilter = lastnedvegnett.filtersjekk(  )
kontrollfilter['vegsystemreferanse'] = 'Fv'
kontrollfilter.pop( 'kryssystem', None )
kontrollfilter.pop( 'sideanlegg', None )

kontrollGdf = nvdbgeotricks.firefeltrapport( mittfilter=kontrollfilter, felttype='K' )
kontrollGdf['Lengde kollektivfelt'] = kontrollGdf['kollektivfelt_antsider'] *kontrollGdf['lengde']


tidsbruk = datetime.now() - t0 