![](media/image1.png){width="3.75in" height="3.75in"}

**Utvikling av et Python-basert beslutningsverktøy for rute-reallokering
i globale forsyningskjeder**

Hajar Al-Mohannah, Sanosh Senthilkumar

Totalt antall sider inkludert forsiden: 17

Molde, 1. juni 2026

![](media/image2.jpeg){width="2.0in" height="1.2430555555555556in"}

**Sammendrag**

Forsyningskjeder er i dag svært sårbare for forstyrrelser som
geopolitisk risiko, værhendelser og logistiske avvik. Dette prosjektet
utvikler et Python-basert beslutningsverktøy som analyserer risiko og
foreslår alternative logistiske løsninger for å minimere
restitusjonstiden. Ved bruk av omfattende datasett har vi identifisert
kritiske faktorer som påvirker forsyningskjedens robusthet, inkludert
effekten av backup-leverandører og alvorlighetsgraden av disrupsjoner.
Modelleringen viser at proaktive beslutninger kan redusere ledetiden
betydelig, selv om det medfører økte transportkostnader. En avansert
sanntidsmodul integrerer nå vær, nyheter, skipstrafikk (AIS) og
oljepriser for å gi dynamisk beslutningsstøtte.

**Abstract**

Supply chains are currently highly vulnerable to disruptions such as
geopolitical risks, weather events, and logistical deviations. This
project develops a Python-based decision-making tool that analyzes risk
and proposes alternative logistical solutions to minimize recovery time.
Using extensive datasets, we have identified critical factors affecting
supply chain resilience, including the impact of backup suppliers and
disruption severity. The modeling demonstrates that proactive decisions
can significantly reduce lead times, despite increasing transportation
costs. An advanced real-time module now integrates weather, news, ship
traffic (AIS), and oil prices to provide dynamic decision support.

# 1.0 Innledning

Globale forsyningskjeder har de siste årene blitt stadig mer komplekse
og sårbare. Hendelser som pandemier, geopolitisk uro og logistiske
flaskehalser har vist hvor raskt en forstyrrelse kan spre seg gjennom
hele verdikjeden. Dette har økt behovet for bedre verktøy som kan
identifisere risiko og støtte beslutninger i situasjoner der leveranser
står i fare. Formålet med dette prosjektet er å undersøke hvordan
datadrevne metoder kan brukes til å styrke robustheten i
forsyningskjeder. 

## 1.1 Problemstilling

Hvordan kan vi utvikle et Python-basert beslutningsverktøy som
automatisk foreslår re-allokering av varer og alternative
transportløsninger når en kritisk transportrute eller leverandør
svikter, og hvordan påvirker dette forsyningskjedens totale
restitusjonstid?

## 1.2 Forskningsspørsmål (Delproblemer)

For å besvare hovedproblemstillingen har vi formulert følgende delproblemer:
1. I hvilken grad kan faktorer som disrupsjonstype, geografisk lokasjon og industrisektor fungere som pålitelige indikatorer for å predikere restitusjonstid i en global forsyningskjede?
2. Hvordan presterer en Random Forest-algoritme sammenlignet med tradisjonelle gjennomsnittsberegninger når det gjelder å estimere restitusjonstid under høy usikkerhet?
3. Hva er de kritiske terskelverdiene for "Total Risk Index" og kostnad-nytte-forholdet som rettferdiggjør overgang til dyrere logistikkalternativer som flyfrakt?

## 1.3 Prosjektets mål

Det overordnede målet med dette prosjektet er å utvikle en funksjonell modell for beslutningsstøtte som kan redusere restitusjonstiden i en forsyningskjede gjennom proaktive tiltak. Ved å kombinere maskinlæring og regelbasert logikk undersøker vi hvordan virksomheter kan reagere raskere og mer strukturert på komplekse forstyrrelser.

## 1.4 Avgrensinger

Prosjektet fokuserer på risikostyring og robusthet i en forenklet
forsyningskjede. Analysen baseres på åpne datasett som beskriver
logistiske avvik og historisk restitusjonstid. Prosjektet er avgrenset
til vareflyten mellom ett sentrallager og et begrenset antall
distribusjonspunkter, med fokus på eksterne risikohendelser.

## 1.4 Antagelser

Vi antar at historiske data for restitusjonstid er representative for
fremtidige hendelser.

Vi antar at flyfrakt i gjennomsnitt reduserer ledetiden med 60% sammenlignet med sjøfrakt. Denne antagelsen er basert på generelle logistiske benchmarks for interkontinentale ruter (f.eks. fra World Bank Logistics Performance Index).

Vi antar at kostnadene for flyfrakt er ca. 7 ganger høyere enn sjøfrakt per enhet. Gitt den høye usikkerheten i transportrater under kriser, anerkjenner vi behovet for sensitivitetsanalyse av disse parametrene for å sikre modellens pålitelighet i ulike markedssituasjoner.

# 2.0 Litteratur

Gjennomgangen av litteratur de siste fem årene viser en økende trend mot
bruk av digitale tvillinger og maskinlæring for å håndtere disrupsjoner
i forsyningskjeder. Ivanov (2021) understreker at "viability"
(levedyktighet) i en forsyningskjede avhenger av evnen til rask
re-konfigurering og adaptiv planlegging. Vårt prosjekt bygger videre på dette ved å implementere en sanntidsmodul som muliggjør nettopp slik rask re-konfigurering.

Sentralt i moderne forskning står også teorien om "The Ripple Effect" (Ivanov et al., 2014), som beskriver hvordan en lokal forstyrrelse kan spre seg og skape systemiske feil i hele kjeden. Mens mye av den eksisterende litteraturen fokuserer på statiske risikoanalyser, bidrar dette prosjektet med en dynamisk tilnærming som kobler sanntids risikosignaler direkte til operative beslutningsregler. Dette bygger bro mellom teoretisk robusthetsanalyse og praktisk krisehåndtering.

Forskning av Hosseini et al. (2019) peker på at
backup-leverandører er den mest effektive strategien for å redusere
restitusjonstid, noe som understøttes av våre simuleringsresultater i kapittel 9.0. Videre har studier av Choi (2020) vist at sanntids
beslutningsstøtte kan redusere økonomiske tap med opptil 30% under
globale kriser. Dette prosjektet adresserer det praktiske gapet ved å kombinere prediktive modeller med operative beslutningsregler som kan automatiseres.

## 2.1 Begrunnelse for modellvalg

Valget av **Random Forest Regressor** som hovedmodell fremfor enklere modeller som lineær regresjon eller mer komplekse metoder som Deep Learning er strategisk:
1. **Ikke-lineære sammenhenger:** Restitusjonstid påvirkes ofte av komplekse interaksjoner mellom disrupsjonstype, geografi og industri som enkle lineære modeller har vanskelig for å fange opp.
2. **Datatilgjengelighet og kompleksitet:** Deep Learning krever ofte ekstremt store og homogene datamengder for å konvergere. Random Forest er langt mer effektiv på tabulære data med moderate mengder støy, noe som er typisk for logistiske datasett.
3. **Robusthet:** Random Forest er en ensemble-metode som er mindre følsom for ekstremverdier (outliers) og "overfitting" sammenlignet med beslutningstrær eller nevrale nettverk.
4. **Feature Importance (Forklarbarhet):** Algoritmen gir innsikt i hvilke variabler som er viktigst for prediksjonen. I en logistisk kontekst er det avgjørende at en beslutningstaker forstår *hvorfor* verktøyet varsler høy risiko (XAI - Explainable AI).

**Regelbasert beslutningslogikk** (If-Then-Else) er valgt for å komplementere maskinlæringsmodellen. Mens Random Forest predikerer *hva* som vil skje (restitusjonstid), sørger den regelbaserte logikken for *hvordan* man skal reagere (beslutningsstøtte). Dette sikrer deterministiske og forutsigbare handlinger på kritiske terskelverdier, noe som reduserer den kognitive belastningen for beslutningstakere i en krisesituasjon preget av "Bounded Rationality".

# 3.0 Teori

Risikostyring i forsyningskjeder handler om å identifisere, analysere og
håndtere hendelser som kan påvirke flyten av varer og tjenester. I
litteraturen skilles det ofte mellom to hovedtyper risiko: disruption
risk og operational risk. Prosjektet bygger på teorien om Supply Chain
Resilience (forsyningskjederobusthet), som defineres som evnen til å
motstå, tilpasse seg og komme seg etter forstyrrelser (Ponomarov &
Holcomb, 2009).

## 3.1 Restitusjonstid (Recovery Time)

Teoretisk sett følger en disrupsjon en "triangel-modell" hvor ytelsen
faller brått og gradvis stiger tilbake til normalen. Vår modell
predikerer varigheten av denne stigningen (full_recovery_days).

## 3.2 Beslutningsteori under usikkerhet

Vi benytter Bounded Rationality (begrenset rasjonalitet) som teoretisk
rammeverk, hvor algoritmen hjelper beslutningstakere med å navigere i
komplekse valgmuligheter basert på objektive terskelverdier for risiko
og kostnad. Dette danner grunnlag for prioritering av tiltak.

# 4.0 Casebeskrivelse

Casestudien tar utgangspunkt i en global forsyningskjede som frakter
varer fra Asia til Europa og Amerika via kritiske ruter som Suez-kanalen
og Stillehavet. Problemet omhandler hvordan man skal håndtere
uforutsette hendelser som cyberangrep, geopolitiske konflikter og
naturkatastrofer som blokkerer disse rutene.

# 5.0 Metode og data

## 5.1 Metode

Prosjektet benytter en kvantitativ metode basert på case-studie design.
Det er utviklet en strukturert databehandlings- og modellpipeline i
Python:

-   Forskingsperspektiv: Deskriptiv og prediktiv analyse.
-   Analysemetoder: Statistisk regresjon for prediksjon og regelbaserte
    algoritmer for beslutningsstøtte.
-   Verktøy: Python med biblioteker som Pandas, Scikit-learn, Matplotlib
    og Seaborn.
-   Pipeline: Datarensing (clean_data.py), Feature Engineering
    (feature_engineering.py), Modellutvikling
    (recovery_prediction_model.py) og Evaluering (stress_test.py).

## 5.2 Data

Datasettet består av 100 000 observasjoner av logistiske hendelser.

-   **Datakilder:** Modellen bygger på to åpne datasett hentet fra
    plattformen Kaggle (Gedipudi, 2026; Uskono, 2026). Disse inneholder informasjon om henholdsvis disrupsjonshendelser og historiske restitusjonstider.
-   **Cleaning:** Data er renset for manglende verdier og inkonsistente
    rutenavn via `clean_data.py`.
-   **Feature Engineering:** Nye variabler er konstruert i `feature_engineering.py` for å styrke modellens prediksjonskraft:
    -   **Total Risk Index:** Beregnes som en vektet sum: `(Geopolitisk risiko * 0.6) + (Væralvorlighet * 0.04)`. Vektingen reflekterer at geopolitisk risiko (skalert 0-1) veier tyngre enn værhendelser (skalert 0-10) i vårt case. Ved å bruke 0.04 som vekt for vær, sikrer vi at begge faktorene bidrar balansert til en samlet indeks mellom 0 og 1.
    -   **Recovery Speed:** Beregnes som `Antall dager for full restitusjon / Disrupsjonsalvorlighet`. Dette gir et mål på hvor effektivt en forsyningskjede henter seg inn sett i forhold til sjokkets styrke.
-   **Sammenslåing (Merging):** Siden datasettene fra Kaggle manglet en felles unik identifikator, ble det utviklet en mapping-logikk i Python som koblet produktkategorier (fra disrupsjonsdata) til industrisektorer (fra restitusjonsdata). For eksempel ble "Electronics" mappet til "Technology"-sektoren, og "Pharmaceuticals" til "Healthcare". Denne statistiske sammenslåingen gjør det mulig å analysere hvordan generelle risikohendelser i en spesifikk industri direkte påvirker restitusjonstiden for relaterte produktgrupper.
-   **Separering:** Data er delt i et treningssett (80%) og et testsett (20%) for å sikre en objektiv evaluering av modellens generaliseringsevne.

# 6.0 Modellering

## 6.1 Terskelverdier (Thresholds)

Modellen opererer med tre risikonivåer basert på Total Risk Index:

-   Lav risiko (\< 0.4): Ingen umiddelbare tiltak.
-   Moderat risiko (0.4 - 0.7): Overvåking og forberedelse av backup-løsninger.
-   Høy risiko (\> 0.7): Automatisk utløsning av tiltak som omruting eller bytte til flyfrakt.

## 6.2 Antagelser og overførbarhet

Modellen bygger på operative antagelser om at flyfrakt reduserer ledetid med 60% til en 7x høyere kostnad enn sjøfrakt. Disse verdiene er hentet fra generelle logistiske benchmarks og rapporter fra organisasjoner som World Bank og IATA. Valget av disse parameterne er gjort for å illustrere de dramatiske avveiningene (trade-offs) logistikkansvarlige står overfor under en krise. 

Siden rapporten delvis benytter syntetiske og simulerte data, er det viktig å understreke at de nøyaktige tallverdiene (som MAE og R2) er mest relevante for å illustrere *potensialet* i metoden. En reell implementering krever en omfattende sensitivitetsanalyse for å avdekke hvordan modellens anbefalinger endres dersom kostnadsdifferansen mellom fly og sjø varierer (f.eks. ved ekstreme rater på sjøfrakt som sett under COVID-19). Overførbarhet til reelle forsyningskjeder krever integrasjon med virksomhetsspesifikke ERP-data og mer presise kostnadsparametere.

## 6.3 Algoritme for Rute-reallokering

Algoritmen foreslår optimale løsninger som "Switch to Air (Priority)"
for tidskritiske bransjer og "Reroute via Atlantic/Cape" ved blokkering
av Suez.

## 6.4 Prediksjonsmodell og kritisk evaluering

En Random Forest Regressor er trent for å predikere restitusjonstid
basert på 17 variabler.
-   **MAE (Mean Absolute Error):** 32.89 dager. Dette innebærer at modellens prediksjoner i gjennomsnitt bommer med ca. en måned. For svært lange disrupsjoner (flere hundre dager) kan dette være akseptabelt for grovplanlegging, men for kortsiktige operative valg er usikkerheten foreløpig for høy.
-   **R² (Determinasjonskoeffisient):** 0.3356. Dette betyr at modellen kun forklarer ca. 34% av variasjonen i restitusjonstid. Dette understreker at forsyningskjeder er ekstremt komplekse systemer hvor mange uforutsette faktorer (som politiske beslutninger eller lokale kapasitetsproblemer) ikke fanges opp av de tilgjengelige variablene.

Konklusjonen er at modellen fungerer godt som en *indikator* og retningsgivende beslutningsstøtte, men at den ikke bør brukes til autonom beslutningstaking uten menneskelig overstyring.

## 6.5 Sanntids Risikointegrasjon (Ny funksjon)

En av prosjektets mest innovative utvidelser er integrasjonen av **NewsAPI**, **OpenWeatherMap API**, **AlphaVantage** og **AISStream**. Verktøyet henter nå automatisk sanntidsdata for å identifisere trusler før de påvirker forsyningskjeden:

-   Global nyhetsovervåking: Analyserer nyhetsstrømmer for geopolitisk uro, streik og blokkeringer.
-   Meteorologisk overvåking: Henter faktiske værdata for kritiske logistiske knutepunkter.
-   Maritime Bevegelser (AIS): Overvåker skipstrafikk i sanntid via **AISStream**. Per 30. april 2026 ble det registrert kritisk lav trafikk i Hormuzstredet (0 skip funnet), noe som utløser maksimal risiko for ruter i Midtøsten.
-   Energi og Råvarer: Henter sanntids oljepriser (Brent Crude). Den nåværende prisen på **$110.83/fat** har ført til at modellen automatisk legger til et **15% drivstofftillegg** på alle transportberegninger.

# 7.0 Analyse

## 7.1 Stresstesting

Simulering av en total Suez-blokkering (Risiko = 0.95) viser at andelen ordrer som må omrutes øker drastisk for å opprettholde leveringsdyktighet.

![Figur 1: Skifte i beslutningsstrategier ved normal drift vs. global Suez-blokkering.](005 report/figures/stress_test_comparison.png)

## 7.2 Evaluering av målfunksjon

Med sanntidsdata integrert (per 30. april 2026), inkludert den ekstreme oljeprisen og Hormuz-situasjonen, viser modellen en mer proaktiv, men kostbar tilnærming:

-   Kostnadsøkning: 209.64% (drevet av flyfrakt og 15% drivstofftillegg)
-   Reduksjon i Ledetid: 12.68%
-   **Efficiency Ratio: 0.0605**

**Begrepet "Efficiency Ratio"** er i dette prosjektet definert som:
`Efficiency Ratio = % Reduksjon i Ledetid / % Kostnadsøkning`.

Dette forholdstallet angir hvor mange prosent ledetid som spares for hver prosent økning i transportkostnader. En verdi på 0.0605 indikerer at tidsbesparelsen er svært kostbar; vi må akseptere en betydelig kostnadsøkning for å oppnå en relativt liten reduksjon i ledetid. I en logistisk kontekst betyr dette at strategien primært er egnet for "High-Value, Low-Weight"-produkter eller tidskritiske varer der forsinkelser fører til eksponensielle tap (f.eks. medisinske forsyninger eller produksjonsstopp).

![Figur 2: Forholdet mellom økte transportkostnader og oppnådd tidsbesparelse.](005 report/figures/cost_leadtime_tradeoff.png)

# 8.0 Resultat

Resultatene viser at modellen effektivt identifiserer kritiske ordrer og reagerer på sanntidssignaler. Fordelingen av beslutninger for det analyserte testsettet er som følger:

| Strategi | Andel (%) |
| :--- | :--- |
| Maintain Current Route | 43.3% |
| Reroute via Atlantic/Cape | 19.2% |
| Switch to Air (Priority) | 18.6% |
| Manual Review Required | 10.4% |
| Switch to Air (Express) | 8.5% |

![Figur 3: Fordeling av restitusjonstid på tvers av ulike industrier.](005 report/figures/recovery_by_industry.png)

# 9.0 Diskusjon

Funnene i analysen viser tydelig hvordan ulike typer forstyrrelser påvirker restitusjonstid. Spesielt fremstår cyberangrep og naturkatastrofer som hendelser med høy restitusjonstid, noe som indikerer at disse typene risiko er vanskeligere å håndtere operasjonelt.

Et sentralt funn er effekten av backup-leverandører. Resultatene viser en betydelig reduksjon i restitusjonstid for selskaper som har alternative leverandører tilgjengelig. En "Efficiency Ratio" på 0.0605 (oppdatert med sanntidsdata) antyder at tidsbesparelsen kommer med en betydelig kostnad, hovedsakelig grunnet flyfrakt og høye drivstoffpriser. 

**Kritisk refleksjon rundt kost/nytte:**
Det må stilles spørsmål ved om en reduksjon i ledetid på ca. 12% forsvarer en kostnadsøkning på over 200%. For lavmargin-produkter som "Consumer Goods" vil dette i de fleste tilfeller ikke være økonomisk bærekraftig. Modellen bør derfor videreutvikles til å inkludere en "Profit-at-Risk"-modul som stopper dyre tiltak dersom de overskrider varens marginer.

**Svakheter ved sanntidsdata:**
Selv om integrasjonen av sanntidsdata er en styrke, innebærer det også nye sårbarheter:
-   **API-latens og feil:** Forsinkelser i oppdatering av nyhets- eller vær data kan føre til at modellen reagerer på utdatert informasjon.
-   **Datakvalitet (AIS):** Skipstranspondere kan skrus av eller manipuleres (spoofing), noe som kan gi et falskt bilde av trafikktetthet i kritiske områder som Hormuzstredet.
-   **Modellbias:** Prediksjonsmodellen (Random Forest) er trent på historiske data som kanskje ikke fanger opp de unike dynamikkene i en helt ny global krise.

## 9.1 Sensitivitetsanalyse

For å validere modellens robusthet har vi gjennomført en sensitivitetsanalyse av de logistiske parametrene. Ved å variere kostnadsmultiplikatoren for flyfrakt (fra 3x til 12x) og tidsreduksjonen (fra 20% til 60%), ser vi hvordan modellens lønnsomhet påvirkes:

| Flyfrakt-kostnad | Tidsreduksjon | Kostnadsøkning (Tot) | Efficiency Ratio |
| :--- | :--- | :--- | :--- |
| 3.0x | 60% | 71.26% | 0.1779 |
| 7.0x (Base) | 60% | 209.64% | 0.0605 |
| 12.0x | 60% | 382.61% | 0.0331 |
| 7.0x | 20% | 209.64% | 0.0114 |

Analysen viser at "Efficiency Ratio" er ekstremt følsom for både kostnadsnivå og faktisk oppnådd tidsbesparelse. Ved en kostnadsmultiplikator på 12x faller Efficiency Ratio til 0.0331, noe som betyr at hver prosent tidsbesparelse koster over 30 ganger mer i transport. Dette bekrefter at modellen må kalibreres kontinuerlig mot reelle fraktrater for å unngå suboptimale beslutninger.

Modellen har likevel begrensninger. Den er basert på historiske og delvis simulerte data. I virkelige forsyningskjeder vil beslutninger ofte være påvirket av faktorer som kontraktsforhold og politiske forhold. 


# 10.0 Konklusjon

Dette prosjektet har demonstrert utviklingen av et datadrevet beslutningsverktøy for risikostyring i globale forsyningskjeder. Basert på våre forskningsspørsmål kan vi konkludere med følgende:

1. **Prediktive indikatorer:** Analysen bekrefter at disrupsjonstype og geografisk lokasjon er de sterkeste indikatorene for restitusjonstid, men at industrisektor også spiller en modererende rolle. 
2. **Modellprestasjon:** Random Forest-algoritmen gir mer nyanserte estimater enn tradisjonelle gjennomsnitt, men en R2 på 0.3356 understreker at betydelig usikkerhet gjenstår i komplekse globale systemer.
3. **Beslutningsterskler:** Vi har identifisert at en "Total Risk Index" over 0.7 fungerer som et effektivt beslutningspunkt for proaktiv omruting, men at den økonomiske bærekraften avhenger kritisk av varens verdi og tidsnød.

Oppsummert fungerer verktøyet som en effektiv indikator og støtte under krisehåndtering, men bør suppleres med menneskelig ekspertise. Fremtidig arbeid bør fokusere på å inkludere mer detaljerte kostnadsdata og dypere integrasjon av sanntids-værdata for enda mer presise prediksjoner.

# 11.0 Bibliografi

Choi, T. M. (2020). Innovative "bring-service-near-to-customer" operations under Corona-Virus (COVID-19) crisis: Lessons from Hong Kong. Annals of Operations Research, 1-25.

Gedipudi, L. (2026). Supply Chain Disruption and Recovery Dataset [Data set]. Kaggle. https://www.kaggle.com/datasets/likithagedipudi/supply-chain-disruption-and-recovery-dataset

Hosseini, S., Ivanov, D., & Dolgui, A. (2019). Review of quantitative methods for supply chain resilience analysis. Transportation Research Part E: Logistics and Transportation Review, 125, 285-307.

IATA. (2024). Air Cargo Market Analysis: Benchmarking Air vs. Sea Freight Costs and Lead Times.

Ivanov, D. (2021). Supply chain viability and the post-pandemic digital twin. International Journal of Production Research, 59(12), 3530-3542.

Ivanov, D., Sokolov, B., & Dolgui, A. (2014). The Ripple effect in supply chains: trade-off ‘efficiency-flexibility-resilience’ in disruption management. International Journal of Production Research, 52(7), 2154-2172.

Ponomarov, S. Y., & Holcomb, M. C. (2009). Understanding the concept of supply chain resilience. The International Journal of Logistics Management, 20(1), 124-143.

Uskono, B. M. (2026). Global Supply Chain Disruption & Resilience [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/14387044

World Bank. (2023). Logistics Performance Index (LPI) 2023: Connecting to Compete. https://lpi.worldbank.org/

# 12.0 Vedlegg

Følgende Python-skript utgjør kildekoden for beslutningsverktøyet:

-   real_time_risk_monitor.py: Henter sanntidsdata fra NewsAPI, OpenWeatherMap, AISStream og AlphaVantage.
-   decision_model.py: Hovedalgoritme som integrerer sanntidssignaler og foreslår logistiske tiltak.
-   recovery_prediction_model.py: Trener Random Forest-modellen for prediksjon av restitusjonstid.
-   evaluate_objective.py: Beregner KPI-er som Efficiency Ratio og kostnadsøkning.
-   visualize_results.py: Genererer alle figurer brukt i analysen.
-   clean_data.py / feature_engineering.py: Skript for databehandling og klargjøring.

Fullstendig kildekode og datasett er tilgjengelig i prosjektets GitHub-depot.
