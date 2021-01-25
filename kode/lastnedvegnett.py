"""
Div kjekke funksjoner for nedlasting av data til KOSTRA-rapportering
"""
from copy import deepcopy

import STARTHER 
import nvdbgeotricks  
import skrivdataframe


def vegnetthelelandet( mittfilter={} ):
    mittfilter = filtersjekk( mittfilter )

    myGdf = nvdbgeotricks.vegnett2gdf( mittfilter=mittfilter )
    return myGdf


def rapport01_gdf2excel( mygdf, filnavn='vegnettkostra.xlsx', sheet_prefiks='', metadata=None ): 
    """
    Lager excel-oppsummering av lengde vegnett per fylke, kommune og vegkategori
    """

    # Konverterer lengde til km
    mygdf = deepcopy( mygdf ) 
    mygdf['lengde'] = mygdf['lengde'] / 1000 

    # t1 = mygdf.groupby( [ 'fylke' ]).agg({ 'lengde' : 'sum' }).reset_index()
    t2 = mygdf.groupby( [ 'fylke', 'vegkategori' ]).agg({ 'lengde' : 'sum' }).reset_index()
    t3 = mygdf.groupby( [ 'fylke', 'kommune' ]).agg({ 'lengde' : 'sum' }).reset_index()
    t4 = mygdf.groupby( [ 'fylke', 'kommune', 'vegkategori' ]).agg({ 'lengde' : 'sum' }).reset_index()

    t2 = skrivdataframe.fylkesnr2fylkesnavn( t2 )

    t2_transponert = skrivdataframe.transponerFylkePerVegkategori( t2 )
    t2_transponert['Riksveg (E+R)'] = t2_transponert['E'] + t2_transponert['R']

    t2_transponert = t2_transponert[['Riksveg (E+R)', 'E', 'R', 'F', 'K', 'P', 'S' ]]

    # # Skal ha med formattering fra xlsxwriter, men ikke tilgjengelig akkurat nu... 
    # t2.to_excel( filnavn, sheet_name=sheet_prefiks + 'Fylke per vegkategori' )
    # t3.to_excel( filnavn, sheet_name=sheet_prefiks +'per kommune')
    # t4.to_excel( filnavn, sheet_name=' per kommune og vegkategori')

    navneliste = [  sheet_prefiks+'Fylkesvis tabell',
                    sheet_prefiks+'radvis per fylke og vegkat', 
                    sheet_prefiks+'radvis per kommune', 
                    sheet_prefiks+'radvis per kommune og vegkat'  ]

    skrivdataframe.skrivdf2xlsx([t2_transponert, t2, t3, t4], filnavn=filnavn, sheet_name=navneliste, metadata=metadata )



def filtersjekk( mittfilter={} ):
    """
    Beriker et filter med vegnett-spesifikke standardverdier for kostra-søk 
    """

    if not 'kryssystem' in mittfilter.keys():
        mittfilter['kryssystem'] = 'false' 

    if not 'sideanlegg' in mittfilter.keys():
        mittfilter['sideanlegg'] = 'false' 

    # Kun kjørende, og kun øverste topologinivå, og ikke adskiltelop=MOT
    mittfilter['trafikantgruppe'] = 'K'
    mittfilter['detaljniva']      = 'VT,VTKB'
    mittfilter['adskiltelop']     = 'med,nei' 
    mittfilter['typeveg']         = 'kanalisertVeg,enkelBilveg' 
    mittfilter['historisk']       = 'true'
    mittfilter['tidspunkt']       = '2020-12-31'

    return mittfilter



