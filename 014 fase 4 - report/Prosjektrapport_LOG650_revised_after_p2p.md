![](media/image1.png){width="3.75in" height="3.75in"}

**Utvikling av et Python-basert beslutningsverktøy for rute-reallokering
i globale forsyningskjeder**

Hajar Al-Mohannah, Sanosh Senthilkumar

Totalt antall sider inkludert forsiden: 17

Molde, 24. mai 2026

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
oljepriser for å gi dynamiske beslutningsstøtte.

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
1. Hvilke risikofaktorer (f.eks. disrupsjonstype, geografi, industri) har størst statistisk påvirkning på forsyningskjedens restitusjonstid?
2. Hvordan kan en Random Forest-modell brukes til å predikere restitusjonstid basert på historiske og sanntidsbaserte risikosignaler?
3. Under hvilke spesifikke betingelser (risikonivå, kostnadstoleranse, tidsnød) bør modellen anbefale alternative transportruter som flyfrakt eller omruting via Atlantic/Cape?

## 1.3 Avgrensinger

Prosjektet fokuserer på risikostyring og robusthet i en forenklet
forsyningskjede. Analysen baseres på åpne datasett som beskriver
logistiske avvik og historisk restitusjonstid. Prosjektet er avgrenset
til vareflyten mellom ett sentrallager og et begrenset antall
distribusjonspunkter, med fokus på eksterne risikohendelser.

## 1.4 Antagelser

Vi antar at historiske data for restitusjonstid er representative for
fremtidige hendelser.

Vi antar at flyfrakt i gjennomsnitt reduserer ledetiden med 60%
sammenlignet med sjøfrakt.

Vi antar at kostnadene for flyfrakt er ca. 7 ganger høyere enn sjøfrakt
per enhet.

# 2.0 Litteratur

Gjennomgangen av litteratur de siste fem årene viser en økende trend mot
bruk av digitale tvillinger og maskinlæring for å håndtere disrupsjoner
i forsyningskjeder. Ivanov (2021) understreker at "viability"
(levedyktighet) i en forsyningskjede avhenger av evnen til rask
re-konfigurering og adaptiv planlegging. Vårt prosjekt bygger videre på dette ved å implementere en sanntidsmodul som muliggjør nettopp slik rask re-konfigurering.

Forskning av Hosseini et al. (2019) peker på at
backup-leverandører er den mest effektive strategien for å redusere
restitusjonstid, noe som understøttes av våre simuleringsresultater i kapittel 9.0. Videre har studier av Choi (2020) vist at sanntids
beslutningsstøtte kan redusere økonomiske tap med opptil 30% under
globale kriser. Dette prosjektet adresserer det praktiske gapet ved å kombinere prediktive modeller med operative beslutningsregler som kan automatiseres.

## 2.1 Begrunnelse for modellvalg

Valget av **Random Forest Regressor** som hovedmodell er basert på flere faktorer:
1. **Ikke-lineære sammenhenger:** Restitusjonstid påvirkes ofte av komplekse interaksjoner mellom disrupsjonstype, geografi og industri som enkle lineære modeller har vanskelig for å fange opp.
2. **Robusthet:** Random Forest er mindre følsom for ekstremverdier (outliers) og støy i datasettet sammenlignet med alternative algoritmer som nevrale nettverk.
3. **Feature Importance:** Algoritmen gir innsikt i hvilke variabler som er viktigst for prediksjonen, noe som er kritisk for å gi forklarlig beslutningsstøtte (XAI).

**Regelbasert beslutningslogikk** er valgt for å komplementere maskinlæringsmodellen. Dette sikrer at verktøyet kan handle umiddelbart på terskelverdier (thresholds) for risiko, noe som gir den nødvendige hastigheten i en krisesituasjon der "Bounded Rationality" ofte begrenser menneskelige beslutningstakere.

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
    -   **Total Risk Index:** Beregnes som en vektet sum: `(Geopolitisk risiko * 0.6) + (Væralvorlighet * 0.04)`. Vektingen reflekterer at geopolitisk risiko ofte har en mer langvarig og systemisk påvirkning på rutevalg i vårt case.
    -   **Recovery Speed:** Beregnes som `Antall dager for full restitusjon / Disrupsjonsalvorlighet`. Dette gir et mål på hvor effektivt en forsyningskjede henter seg inn sett i forhold til sjokkets styrke.
-   **Sammenslåing (Merging):** Siden datasettene mangler en felles unik identifikator, ble de slått sammen statistisk ved å mappe produktkategorier til industrisektorer. Dette muliggjør en analyse av hvordan generelle disrupsjonsmønstre i en industri påvirker spesifikke restitusjonstider.
-   **Separering:** Data er delt i et treningssett (80%) og et testsett
    (20%).

# 6.0 Modellering

## 6.1 Terskelverdier (Thresholds)

Modellen opererer med tre risikonivåer basert på Total Risk Index:

-   Lav risiko (\< 0.4): Ingen umiddelbare tiltak.
-   Moderat risiko (0.4 - 0.7): Overvåking og forberedelse av backup-løsninger.
-   Høy risiko (\> 0.7): Automatisk utløsning av tiltak som omruting eller bytte til flyfrakt.

## 6.2 Antagelser og overførbarhet

Modellen bygger på operative antagelser om at flyfrakt reduserer ledetid med 60% til en 7x høyere kostnad enn sjøfrakt. Disse verdiene er hentet fra generelle logistiske benchmarks (f.eks. World Bank Logistics Performance Index), men bør i en reell implementering verifiseres gjennom en sensitivitetsanalyse tilpasset spesifikke kontrakter.

Siden rapporten delvis benytter syntetiske og simulerte data, er det viktig å understreke at de nøyaktige tallverdiene (som MAE og R2) er mest relevante for å illustrere *potensialet* i metoden. Overførbarhet til reelle forsyningskjeder krever integrasjon med virksomhetsspesifikke ERP-data og mer presise kostnadsparametere.

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
| Reroute via Atlantic/Cape | 24.7% |
| Switch to Air (Priority) | 13.1% |
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
-   **API-latens og feil:** Forsinkelser i oppdatering av nyhets- eller værdata kan føre til at modellen reagerer på utdatert informasjon.
-   **Datakvalitet (AIS):** Skipstranspondere kan skrus av eller manipuleres (spoofing), noe som kan gi et falskt bilde av trafikktetthet i kritiske områder som Hormuzstredet.
-   **Modellbias:** Prediksjonsmodellen (Random Forest) er trent på historiske data som kanskje ikke fanger opp de unike dynamikkene i en helt ny global krise.

Modellen har likevel begrensninger. Den er basert på historiske og delvis simulerte data. I virkelige forsyningskjeder vil beslutninger ofte være påvirket av faktorer som kontraktsforhold og politiske forhold. 


# 10.0 Konklusjon

Beslutningsverktøyet fungerer etter hensikten og gir proaktive råd under kriser. Ved å kombinere risikoanalyse med konkrete tiltak kan virksomheter redusere konsekvensene av forstyrrelser. Fremtidig arbeid bør inkludere mer detaljerte kostnadsdata, flere nivåer i forsyningskjeden og dypere integrasjon av sanntids-værdata for enda mer presise prediksjoner.

# 11.0 Bibliografi

Choi, T. M. (2020). Innovative "bring-service-near-to-customer" operations under Corona-Virus (COVID-19) crisis: Lessons from Hong Kong. Annals of Operations Research, 1-25.

Gedipudi, L. (2026). Supply Chain Disruption and Recovery Dataset [Data set]. Kaggle. https://www.kaggle.com/datasets/likithagedipudi/supply-chain-disruption-and-recovery-dataset

Hosseini, S., Ivanov, D., & Dolgui, A. (2019). Review of quantitative methods for supply chain resilience analysis. Transportation Research Part E: Logistics and Transportation Review, 125, 285-307.

Ivanov, D. (2021). Supply chain viability and the post-pandemic digital twin. International Journal of Production Research, 59(12), 3530-3542.

Ponomarov, S. Y., & Holcomb, M. C. (2009). Understanding the concept of supply chain resilience. The International Journal of Logistics Management, 20(1), 124-143.

Uskono, B. M. (2026). Global Supply Chain Disruption & Resilience [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/14387044

# 12.0 Vedlegg

Følgende Python-skript utgjør kildekoden for beslutningsverktøyet:

-   real_time_risk_monitor.py: Henter sanntidsdata fra NewsAPI, OpenWeatherMap, AISStream og AlphaVantage.
-   decision_model.py: Hovedalgoritme som integrerer sanntidssignaler og foreslår logistiske tiltak.
-   recovery_prediction_model.py: Trener Random Forest-modellen for prediksjon av restitusjonstid.
-   evaluate_objective.py: Beregner KPI-er som Efficiency Ratio og kostnadsøkning.
-   visualize_results.py: Genererer alle figurer brukt i analysen.
-   clean_data.py / feature_engineering.py: Skript for databehandling og klargjøring.

Fullstendig kildekode og datasett er tilgjengelig i prosjektets GitHub-depot.
