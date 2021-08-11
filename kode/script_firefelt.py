import STARTHER
import nvdbgeotricks


firefeltfilter = { 'vegsystemreferanse' : 'Ev,Rv', 'tidspunkt' : '2020-12-31'}

firefeltGDF = nvdbgeotricks.firefeltrapport( mittfilter=firefeltfilter, felttype='firefelt' )

print('Lengde firefelt riksveg (vegkategori E+R',   round( firefeltGDF['lengde'].sum() / 1000), '[km]' )
# Lengde firefelt riksveg (vegkategori E+R 842 [km]


# firefeltGDF.to_file( 'ekstratall.gpkg', layer='firefelt_e_r', driver='GPKG' )