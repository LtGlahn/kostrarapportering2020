# Kode for kostraleveranse 2020

Her er kode for [kostraleveransen 2020](https://github.com/LtGlahn/kostrarapportering2020)

# Installasjon 

Filen `conda_environment.txt` og `spec-file.txt` inneholder navn og versjonsnummer på de programpakkene som er brukt. Vi krysser fingrene for at den fungerer til å opprette virituelt Conda-miljø etter oppskriften https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html. 


Det aller meste bør fungere fint med nyere versjoner - det mest plagsomme er skriving til excel med pen formattering. Nåværende oppskrift er låst til `xlsxwriter versjonn 1.3.7`. Heldigvis tilbyr nyere versjoner langt oppskrifter enn det som er brukt. 

# Organisering og dataflyt

Jeg gjør tung bruk av [`nvdbapi-V3`](https://github.com/LtGlahn/nvdbapi-V3), mitt egenutviklede bibliotek for å laste ned data fra [NVDB api V3](https://nvdbapiles-v3.atlas.vegvesen.no/dokumentasjon/), inklusive metoder for paginering og for å _"pakke om"_ data til lister med _"flat"_ dictionary-struktur - som igjen fôres direkte inn i (geo)dataframes fra [pandas](https://pandas.pydata.org/) og [geopandas](https://geopandas.org/) - bibliotekene. For å sikre reproduserbarhet er dette biblioteket lagt in som en egen mappe i reposet. Filen `STARTHER.py` føyer denne mappen til søkestien. 

Jeg har laget 20 ulike script som lager de ulike rapportene. Ett av dem lager rapporttype 13, 14 og 15, som er nesten identiske opptellinger av tunnel. 

For rapporttype 24, _Fylkesveg med 4 felt_, har jeg ikke noe skript, men derimot en helt egen funksjon `firefeltrapport` i fila `nvdbapi-V3/nvdgeotricks.py`. Denne returnerer en geodataframe for firefelt i hele Norge, og ble brukt til en tidligere rapportering av nettopp dét. Kostra-rapportering for fylkesveg blir da 
```
myGdf = nvdbgeotricks.firefeltrapport( mittfilter={'vegsystemreferanse' : 'Fv',  'tidspunkt' : '2020-12-31' })
myGdf.groupby( 'fylke' ).agg( { 'lengde' : 'sum' } ).astype('int')
```

Resultatene herfra samsvamsvarer rimelig godt med data fra vårt nye produksjonssystem ["NVDB rapporter"](https://www.vegdata.no/produkter-og-tjenester/nvdb-rapporter/), som er det vi har brukt i leveransen av rapport nummer 24. 





