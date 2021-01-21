"""
Div kjekke funksjoner for nedlasting av data til KOSTRA-rapportering
"""


import STARTHER 
import nvdbgeotricks  


def vegnetthelelandet( mittfilter={} ):
    mittfilter = filtersjekk( mittfilter )

    return nvdbgeotricks.vegnett2gdf( mittfilter=mittfilter )


def gdf2excel( mygdf, filnavn='vegnettkostra.xlsx', sheet_prefiks='Lengde vegnett ' ): 
    """
    Lager excel-oppsummering av lengde vegnett per fylke, kommune og vegkategori
    """

    # t1 = mydf.groupby( [ 'fylke' ]).agg({ 'lengde' : 'sum' }).reset_index()
    t2 = mydf.groupby( [ 'fylke', 'vegkategori' ]).agg({ 'lengde' : 'sum' }).reset_index()
    t3 = mydf.groupby( [ 'fylke', 'kommune' ]).agg({ 'lengde' : 'sum' }).reset_index()
    t4 = mydf.groupby( [ 'fylke', 'kommune', 'vegkategori' ]).agg({ 'lengde' : 'sum' }).reset_index()


    # Skal ha med formattering fra xlsxwriter, men ikke tilgjengelig akkurat nu... 
    t2.to_excel( filnavn, sheet_name=sheet_prefiks + 'Fylke per vegkategori' )
    t3.to_excel( filnavn, sheet_name=sheet_prefiks +'per kommune')
    t4.to_excel( filnavn, sheet_name=' per kommune og vegkategori')


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



