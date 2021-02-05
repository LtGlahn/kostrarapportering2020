
# Kostra-leveranse 2020 - et markert BRUDD med tidligere års rapportering

Årets KOSTRA-rapport fra Nasjonal vegdatabank (NVDB) er i svært liten grad direkte sammenlignbar med tidligere rapporter. At vi har fått nye fylker er for så vidt håndterbart. Verre er det at tallverdiene spriker på måter vi ikke klarer forklare. Dette ser vi tydelig på de nasjonale tallene, eller for de fylkene som ikke har endret seg etter 2019. Dette gjelder ikke alle rapporttypene, men mange av dem. 

Derfor bruker vi anledningen i 2021 til å erklære at vi nå starter en ny tidslinje med rapportering, og at direkte sammenligning med tidligere år kan gi svært misvisende konklusjoner. 

Fokus for årets rapportproduksjon er at rapportene nå er 
  * Dokumentert 
  * Etterprøvbare (reproduserbare) - andre skal kunne ta våre regler og implementere dem. 
  * Riktige, dvs at tallene gir en riktig oppsummering av datagrunnlaget.  

Det er fremdeles fallgruver knyttet til sammenstilling av data fra NVDB. I tillegg blir oppsummeringene aldri bedre enn datagrunnlaget. Vi må derfor fremdeles ta forbehold om feil, både i datagrunlag og implementasjon.

# Hvorfor har vi brudd?

Vi har hatt store omlegginger i NVDB, med både regionreform og nytt [referansesystem](https://www.vegdata.no/ofte-stilte-sporsmal/hva-ma-jeg-vite-om-vegsystemreferanse/) i Nasjonal vegdatabank. Tidligere rapportering er gjort med verktøyene  _"NVDB 123"_ og _"NVDB studio"_. Disse verktøyene bruker fremdeles 2019-fylkene, og saneres om noen måneder. 

Vi har bygget opp metodikk for å levere de samme rapporttypene som før, men ser at tallmaterialet for i år avviker til dels mye med  forrige års rapport. Dette skyldes flere forhold: 
  * håndteringen av _EnvegMed/EnvegMot_ i det gamle systemet er bare delvis er kompatibelt med _adskilte løp = Nei, Med_ eller _Mot_ i det nye.
  * Det er krevende å skille ut kryssdeler og sideanlegg på en robust måte i det gamle systemet.
  * Det gamle systemet gir få og svært begrensede muligheter til å grave i datagrunnlaget som inngår. Dermed er det vanskelig å få presis innsikt i hva som egentlig telles med i summeringene. 
  * Vi måtte jobbe internt med presise definsijoner på hva som regnes med av vegnettet.  

I stedet for å prøve å gjenskape de samme tallverdiene som før så har vi fokusert på å bygge nye metoder som teller _riktig, er godt dokumentert, etterprøvbart og reproduserbart_. Disse metodene bygger på styrkene til det nye referansesystemet og NVDB api versjon 3. 

Vi tester ut og ettergår et [nytt produksjonssystem](https://www.vegdata.no/produkter-og-tjenester/nvdb-rapporter/) for leveranse av KOSTRA-rapporter fra NVDB. På grunn av begrensede ressurser har vi ikke kommet så langt med dette systemet som vi ønsker. Kun én rapport (Kostra 04 Fylkesveg med fire felt) er laget med det nye systemet. For de øvrige rapportene har vi ikke rukket justere rapportproduskjon i tråd med de nyeste definisjonene. Vi har heller ikke fått ettergått de øvrige rapporttypene grundig nok til at vi føler oss trygge på dem. 

I stedet har vi brukt moderne analyseverktøy (python, pandas, geopandas) og implementert rapporteringene der. Dette var egentlig tenkt som verktøy for å teste det nye systemet, men det har vist seg godt egnet for rapportproduksjon. I tillegg byr disse verktøyene på kraftfulle metoder for å grave oss ned i datagrunnlaget, kartproduksjon / GIS analyse med mere. 

# Nedlasting, årets leveranse

Årets leveranse publiseres på github på adressen [https://github.com/LtGlahn/kostrarapportering2020](https://github.com/LtGlahn/kostrarapportering2020). På github kan du lettvint laste ned data med den grønne knappen _"Code" -> "Download ZIP"_ , plassert oppe til høyre. 

![Nedlasting, hele arkivet](./bilder/lastnedrepos.png)

Nedlasting av enkeltrapporter er ørlite grann mer plundrete. 
  * Gå til mappen [kostraleveranse2020](https://github.com/LtGlahn/kostrarapportering2020/tree/main/kostraleveranse2020)
  * Klikk på en fil, for eksempel [Kostra 16 - tunnel u 4m.xlsx](https://github.com/LtGlahn/kostrarapportering2020/blob/main/kostraleveranse2020/Kostra%2016%20-%20tunnell%20u%204m.xlsx)
  * Klikk på _Download_ - knappen 

![Nedlasting, enkelt fil](./bilder/lastnedfil.png)  

# Årets versus fjorårets leveranse


| Navn formell bestilling 							|  Nummer i 2019-leveransen    			| Navn 2019-leveransen / NVDB rapporter				| ID nytt system | Status 2020  | Filnavn 2020	|
|---------------------------------------------------|:-------------------------------------:|---------------------------------------------------|:--------------:|--------------|---------------|
| Riks-, fylkes-, kommune-, privat- og skogsbilveg 	|   	  	  1 						|  Vegnett - sum hele landet 					 	|  		15001 	 |	OK			| Kostra 01 - Vegnett hele landet.xlsx			|
| 													|   	  	  2 						| Fylkesveg med motorveger og motortrafikkveger  	| 		15002	 |	OK			| Kostra 02 - Fylkesveg med motorveg og motortrafikkveg.xlsx |
| Fylkesveg uten fast dekke 						|   	  	  3 						| Fylkesveg uten fast dekke					 		| 		15003	 |	OK          | Kostra 03 - Fylkesveg uten fast dekke.XLSX |
| Fylkesveg med 4 felt 								|   	  	  4 						| Fylkesveg med 4 felt 								| 		15004	 |	OK 			| Kostra 04 - Fylkesveg med 4 felt.XLSX |
| Fylkesvei med tillatt aksellast <10 tonn 			|   	  	  5 						| Fylkesveg aksellast mindre enn 10 tonn 			| 		15005	 |	OK			| Kostra 05 - Fylkesveg aksellast u 10t.xlsx |
| Fylkesvei med begrensning på totalvekt <50 tonn 	|   	  	  6							| Fylkesveg med begrensning på totalvekt mindre enn 50 tonn | 15006	 |	OK			| Kostra 06 - Fylkesveg totalvekt u 50t.xlsx |
| Fylkesveg med fartsgrense 50 eller lavere 		|   	  	  7 						| Fylkesveg med fartsgrense 50 eller lavere 		| 		15007	 |	OK			| Kostra 07 - Fylkesveg maks 50kmt.xlsx | 
| Fylkesvei med begrensning på kj.t.lengde <19,5m 	|   	  	  8 						| Fylkesveg med begrensning på kjøretøylengde mindre enn 19,5 meter | 15008 | OK	| Kostra 08 - maks lengde u 19m.xlsx |
| Underganger på fylkesveg med høydebegrensning lavere enn 4 m 	| 9              			| Fylkesveg undergang med høyde mindre enn 4 meter 	| 		15009	 |	OK			| Kostra 09 - Undergang lavere enn 4m.xlsx |
| Fylkesveg med dårlig eller svært dårlig dekketilstand | 	  	 10 						| N/A  _(separat leveranse)_						|  		 -		 |	-			|	-			|
| Fylkesveg uten fast dekke >5000 ÅDT 				|			 11 						| Fylkesveg uten fast dekke over 5000 ÅDT 			| 		15011	 |	OK			| Kostra 11 - Fylkesveg uten fast dekke AADT over 5000.xlsx |
| Fylkesveg i alt >5000 ÅDT 						|  			 12 						| Fylkesveg i alt mer enn 5000 ÅDT 					|		15012 	 |	OK			| Kostra 12 - Fylkesveg AADT over 5000.xlsx |
| Tunneler på fylkesveg. Lengde 					|   		 13 						| Fylkesveg med lengde tunnel 						| 		15013	 |	OK			| Kostra 13 og 14 - tunnell fylkesveg.xlsx |
| Tunneler på fylkesveg. Antall 					|   		 14 						| Fylkesveg med antall tunnel 						| 		15014	 |	OK (samme som  13)	|  Kostra 13 og 14 - tunnell fylkesveg.xlsx |
| Tunneler på fylkesveg med lengde 500 m og over 	|   		 15 						| Fylkesveg med tunneler over 500 meter 			| 		15015	 |	OK			| Kostra 15 - tunnell fylkesveg lengre enn 500m.xlsx |
| Tunneler på fylkesveg med høydebegrensning <4m    |           16				            | Fylkesveg_tunneler med høyde lavere enn 4 meter 	| 		15016	 |	OK			| Kostra 16 - tunnell u 4m.xlsx    |
| Vegbruer på fylkesveg 							|   		 17 						| Fylkesveg_antall bruer 							| 		15017	 |	OK			| Kostra 17 - Bruer fylkesveg.xlsx |
| Bruer på fylkesvei med tillatt aksellast <10 tonn |   		 18 						| Fylkesveg_bruer under 10 tonn 					| 		15018	 |	OK			| Kostra 18 - Bruer under 10t.xlsx |
| Bruer på fylkesvei med høydebegrensning <4m 		|   		 19 						| Fylkesveg_bruer_høyde mindre enn 4 meter 			| 		15019	 |	OK			| Kostra 19 - Bruer hoyde mindre enn 4m.xlsx |
| Midtrekkverk på to og trefelts fylkesveger 		|   		 20 						| Fylkesveg_midtrekkverk 2-3 felter 				|		15020	 |	OK			| Kostra 20 - Midtrekkverk på to og trefelts Fv.xlsx |
| Gang- og sykkelveger (statlig eller fylkeskommunalt ansvar) langs fylkesveg | 21 			| Gang-og sykkelveger 								|		15021 	 |	OK			| Kostra 21 gang og sykkelveg.xlsx |
| Gang- og sykkelveg i byer/tettsteder >5000 innbyggere (SOSI format) | 		22  		|  													|			 	 | Ikke sosi, men geojson | Kostra 22 - sykkelveger_fylkesveg.zip |
| Forsterket midtoppmerking (rumlefelt), på fylkesveg |   		 23 						| Fylkesveg_forsterket vegoppmerking midt 			|		15023	 |	OK			| Kostra 23 - Fylkesveg med forsterket midtoppmerking.xlsx |
| Støyskjermer og voller langs fylkesvei 			|   		 24 						| Fylkesveg med støyskjerm og voll 					|		15024	 |	OK			| Kostra 24 - Fylkesveg med stoyskjerm og voll.xlsx |
| Kollektivfelt langs fylkesveg 					|   		 25 						| Fylkesveg med kollektivfelt 						|		15025	 |	OK      	| Kostra 25 - Fylkesveg med kollektivfelt.xlsx |



# Merknader til de enkelte rapportene 

Konnekteringslenker knytter sammen en sideveg og en hovedveg i et kryss, og utgjør typisk 5-15 meter mellom det punktet der sideveg møter hovedvegenes vegkant og senterlinja på hovedveg. Disse 5-15 metrene skal ikke regnes med når vi teller veglenger. De utgjør i snitt mindre enn 0.05% av vegnettet, men de er ujevnt fordelt. Konnekteringslenker inngår ikke når vi teller lengder av vegnett, men noen av lengdene nedenfor er opptelling av såkalte _fagdata_, dvs NVDB objekttyper som er _"limt oppå"_ vegnettet i NVDB. For disse klarer vi p.t. ikke skille ut konnekterinngslenkene når vi jobber med fagdata. 

### Kostra 01 - Vegnett hele landet

Rapport nummer 1, _"Vegnett hele landet"_, teller lengden av kjørbart vegnet i Norge. Merk at lengdene her oppgis i kilometer, til forskjell fra øvrige rapporter, som har meter som lengdeenhet. 

Her teller vi ikke gang- og sykkelveger, kun trafikantgruppe K (kjørende). Av typeVeg så teller vi med verdiene _kanalisertVeg, enkelBilveg, rampe, rundkjøring_ og _gatetun_ Vi teller ikke med sideanlegg, strekninger med _adskilte løp=Mot_ og konnekteringslenker. Derimot teller vi alle kryssdeler. 

### Kostra 02 - Fylkesveg med motorveg og motortrafikkveg

Her teller vi lengden av objektet _Motorveg (595)_ langs fylkesvegnettet. Det er såpass få (4 strekninger) at vi ramser dem opp per fylke og vegnummer. Vi teller med eventuelle kryssdeler, men ikke med sideanlegg eller strekninger med _adskilte løp=Mot_. 

### Kostra 03 - Fylkesveg uten fast dekke

Her finner vi lengden av objekttypen _Vegdekke (241)_ langs fylkesveg med egenskapfilteret _massetype = Grus_, og skiller tall for vanlig bilveg (trafikantgruppe K) fra tall for gående og syklende (trafikantgruppe G) i egne faner. Vi teller ikke med sideanlegg og _adskilte løp = Mot_. 

### Kostra 04 - Fylkesveg med 4 felt

Her teller vi lengden av vegnett som har fire eller flere felt. Vi regner ikke med kjørefelt av typene sykkelfelt, fergeoppstillingsplass og ekstra felt ved bomstasjoner. Vi teller heller ikke med kryssdeler, sideanlegg og konnekteringslenker, og heller ikke _adskilte løp = Mot_. 

### Kostra 05 Fylkesveg med maks aksellast under 10 tonn

Her finner vi lengden av objekttypen _Bruksklasse, normaltransport (904)_ med de egenskapverdiene som tilsier maks aksellast under 10 tonn, langs fylkesveg for trafikantgruppe _kjørende_. Vi tar ikke med data for sideanlegg og _adskilte løp = Mot_. 

### Kostra 06 Fylkesveg med maks totalvekt under 50 tonn

Her finner vi lengden av _Bruksklasse, normaltransport (904)_ langs fylkesveg med de egenskapverdiene som tilsier maks totalvekt under 50 tonn, for trafikantgruppe _kjørende_. Vi tar ikke med data for sideanlegg og _adskilte løp = Mot_.


### Kostra 07 Fylkesveg med fartsgrense under 50 km/t. 

Her finner vi lengden av _Fartsgrense (105)_ langs fylkesveg med de egenskapverdiene som tilsier maks kjøretøylengde kortere enn 1.5 meter, for trafikantgruppe _kjørende_. Vi tar ikke med data for sideanlegg og _adskilte løp = Mot_.


### Kostra 08 Fylkesveg med begrensing på kjøretøylengde mindre enn 19,5 meter

Her finner vi lengden av _Bruksklasse, normaltransport (904)_ langs fylkesveg med de egenskapverdiene som tilsier maks kjøretøylengde kortere enn 19.5 meter, for trafikantgruppe _kjørende_. Vi tar ikke med data for sideanlegg og _adskilte løp = Mot_. 

### Kostra 09 Undergang med høyde lavere enn 4 meter. 

Her teller vi antall av _Høydebegrensning (591)_ med egenskapsfilteret _Type Hinder = Undergang/bru_ og _Skilta høyde < 4_ langs fylkesveg.

### Kostra 10 - IKKE I DENNE LEVERANSEN (fylkesveg med dårlig dekketilstand)

_Disse dataene finnes ikke i nasjonal vegdatbank, men i eget system for forvaltning av vegdekke. Vi forstår at dette er en separat leveranse; denne leveransen har kun data fra NVDB._

### Kostra 11 Fylkesveg uten fast dekke med ÅDT høyere enn 5000 kjøretøy per døgn 

Vi har ingen forekomster med fylkesveger uten fast gresse (dvs objekttypen _Vegdekke (241)_ med egenskapfilteret _Massetype = Grus_) som overlapper med objekttypen  _Trafikkmende (540)_ med egenskapen  _ÅDT, total_ større enn 5000 kjøretøy per døgn. (I NVDB vil du sagtens finne et par hundre meter med den metoden vi har brukt, men det er datafeil). 

### Kostra 12

Her teller vi objekttypen _Trafikkmengde (540)_ med egenskapverdien _ÅDT, total_ større enn 5000 kjøretøy per døgn langs fylkesveger. 

### Kostra 13 og 14 Tunneller på fylkesveg, antall og lengde

Her teller vi antall og samlet lengde for tunneler på fylkesveg. Analysen er en sammenstilling av objekttypene _Tunnelløp (67)_ og _Tunnel (581)_. Hvis _tunnel_ - objektet har egenskapen _Lengde, offisiell_ så bruker vi denne for å regne ut lengdene. Hvis ikke henter vi lengden fra tunnelløpet, enten fra tunnelløpets egenskap _Lengde_ eller fra tunnelløpets utstrekning langs vegnettet. 

### Kostra 15 Tunneller lengre enn 500 meter på fylkesveg 

Samme metodikk som for kostra 13 og 14, men nå teller vi kun antall og lengde for de tunnellene som er lengre enn 500 meter.

### Kostra 16 Tunneller på fylkesveg med høyde under 4 meter

Her finner vi objekttypene _Tunnel (581)_ og _Tunnelløp (67)_ som overlapper med objekttypen _Høydebegrensning (591)_ som har egenskapverdi _Skilta høyde_ lavere enn 4 meter. For å finne lengden av tunneller bruker vi samme metode som Kostra 13, 14 og 15. 

### Kostra 17 Bruer langs fylkesveg

Her finner vi antall og lengde av objekttypen _Bru (60)_ som har egenskap _Brukategori = Vegbru_ eller  _Bru i fylling_. 

### Kostra 18 - Bruer under 10t langs fylkesveg

Her finner vi antall og lengde langs fylkesveg av objekttypen _Bru (60)_ som har egenskap _Brukategori = Vegbru_ og overlapper med objekttypen _Brukslasse, normaltransport (904)_ med egenskapverdier som angir tillatt aksellast lavere enn 10 tonn. 


### Kostra 19 - Bruer med høydebegrensning lavere enn 4 meter

Her finner vi antall og lengde langs fylkesveg av objekttypen _Bru (60)_ som har egenskap _Brukategori = Vegbru_ og overlapper med objekttypen _Høydebegrensning (591)_ med egenskapverdi _Skilta høyde_ lavere enn 4 meter.

### Kostra 20 Mindtrekkverk på to og trefelts fylkesveger

Objekttypen _Rekkverk (5)_ med egenskapen _Bruksområde = Midtrekkverk_ eller _Midtdeler_  langs fylkesveger der vi har to eller tre kjørefelt. Det er littegrann komplisert å koble sammen antall kjørefelt fra vegnettet med data om midtrekkverk, men nå har vi laget gode, gjenbrukbare oppskrifter. 

Antall kjørefelt klassifiseres som en av _EttFelt, 2-3felt_ eller _mangefelt_, samt _ukjent_ for de veglenkene som mangler egenskapen _feltoversikt_. I rapporten angir vi først det som etterspørres: Lengde midtrekkverk og midtdeler på to- og trefeltsveg (fanen _"Midtrekkverk 2-3felt"_). I tillegg angir vi lengden av alle midtrekkverk og -delere i fanen _"Alle midtrekkverk"_. 

Den versjonen vi synes får best frem intensjonen bak spørsmålet er fanen _"Midtrekkverk per vegnummer"_, der lengden også er gruppert per vår kjørefelt-gruppering (kolonnen _"kjfelt"_), i tillegg til per vegnummer og fylke. Her får vi tydelig fram hvilke veger som har lengre, sammenhengende strekninger med midtrekkverk (for eksempel Fv44 i Rogaland), og hvilke som kun har rekkverk knyttet til kryss, busslommer etc (for eksempel Fv113 i Viken, med 5 meter). 

Videre er det en utfordring med _overlapp_: Det kan være satt opp mange rekkverk, for eksempel ett på hver side av en midtrabatt, eller mellom busslomme og hovedveg. Dette gir selvsagt "dobbelttelling" langs de delene av vegen der det finnes mer enn ett midtrekkverk eller midtdeler. 

### Kostra 21 gang og sykkelveg langs fylkesveg

Her henter vi vegnett for vegkategorien "Fylkesveg" og  trafikantgruppe "G" (gående og syklende). 

### Kostra 22 Gang og sykkelveg langs fylkesveg i tettsteder med mer enn 5000 innbyggere

Dette er samme datagrunnlag som rapport 21, men i stedet for å oppsummere lengder per fylke så lagrer vi dataene på et GIS-vennlig format. Strengt tatt er vi forpliktet til å levere på SOSI-format for denen typen datautveksling. Dessverre er vi pga tidsnød ikke i stand til å løse gjenværende hindringer for lettvint produksjon av sosifiler med vegnett på det nye vegreferansesystemet. I stedet mener vi geojson er et greit alternativ. Vi kan også levere på andre formater - også sosi, gitt mere tid - bare si ifra.

Den opprinnelige bestillingen er "gang- og sykkelveger innenfor tettsteder med mer enn 5000 innbyggere". Ettersom tettsteder er et datasett som ajourholdes av SSB ser vi det som mest hensiktsmessig at SSB selv gjør analysen med å finne hvor stor del av gang- og sykkelvegene som er innafor disse tettstedene. Dette er en triviell geografisk analyse. Hvis dette ikke er tilfredsstillende så ta kontakt, så skal vi ordne det. I så fall må vi få oversendt ferske data for tettsteder, evt få avklart at vi skal bruke siste gjeldende (per 31.12.2019, så vidt vi ser). 

### Kostra 23 - Fylkesveg med forsterket midtoppmerking.xlsx 

Dette er telling av objekttypen "Vegoppmerking, forsterket" med egenskapsfilteret _Type = Forsterket midtoppmerking_ langs fylkesveg. 

### Kostra 24 - Fylkesveg med støyskjerm og voll.xlsx 

Dette er telling av objekttypene _Skjerm (3)_ med  egenskapen _Bruksområde = Stæyskjerm_ og _Voll (234)_ med egenskapen  _Bruksområde = Støyskjerming_ langs fylkesveg.

### Kostra 25 - Fylkesveg med kollektivfelt

Her teller vi lengde av vegnettet for kjørende, slik som i rapporten Kostra 01 vegnett, men her teller vi kun med de strekningene der det finnes kollektivfelt.  

Vi ser at de eldre versjonene av Rapport nummer 25, _"Fylkesveg med kollektivfelt"_, så er det telt to ganger veglengden der kollektivfelt finnes på begge sider av vegen. Vi er usikre på hva som foretrekkes, og oppgir derfor begge deler, henholdsvis  _"Lengde en retning (m)"_ hvor vi kun teller hvorvidt det finnes kollektivfelt på strekningen, likegyldig hvor mange, og kolonnen _"Lengde per kollektivfelt (m)"_, hvor vi teller dobbelt opp hvis det finnes kollektivfelt på begge sider av vegen (dvs for begge retninger). 

