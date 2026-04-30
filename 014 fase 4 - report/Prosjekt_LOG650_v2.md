![](media/image1.png){width="3.75in" height="3.75in"}

**Utvikling av et Python-basert beslutningsverktøy for rute-reallokering
i globale forsyningskjeder**

Hajar Al-Mohannah, Sanosh Senthilkumar

Totalt antall sider inkludert forsiden: 14

Molde, 30. april 2026

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

## 1.2 Delproblemer

Ved å kombinere maskinlæring og regelbasert beslutningslogikk undersøker
vi hvordan virksomheter kan reagere raskere og mer strukturert på
forstyrrelser. Prosjektet tar utgangspunkt i sentrale prinsipper innen
logistikk og supply chain management, hvor det er en kontinuerlig
avveining mellom kostnadseffektivitet og leveringssikkerhet.

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
re-konfigurering. Forskning av Hosseini et al. (2019) peker på at
backup-leverandører er den mest effektive strategien for å redusere
restitusjonstid. Videre har studier av Choi (2020) vist at sanntids
beslutningsstøtte kan redusere økonomiske tap med opptil 30% under
globale kriser som COVID-19.

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

-   Datakilder: Modellen bygger på to åpne datasett hentet fra
    plattformen Kaggle (Gedipudi, 2026; Uskono, 2026).
-   Cleaning: Data er renset for manglende verdier og inkonsistente
    rutenavn via clean_data.py.
-   Feature Engineering: Nye variabler som Total Risk Index og Recovery
    Speed er konstruert i feature_engineering.py.
-   Separering: Data er delt i et treningssett (80%) og et testsett
    (20%).

# 6.0 Modellering

## 6.1 Terskelverdier (Thresholds)

Modellen opererer med tre risikonivåer basert på Total Risk Index:

-   Lav risiko (\< 0.4): Ingen umiddelbare tiltak.
-   Moderat risiko (0.4 - 0.7): Overvåking.
-   Høy risiko (\> 0.7): Automatisk utløsning av tiltak.

## 6.2 Algoritme for Rute-reallokering

Algoritmen foreslår optimale løsninger som "Switch to Air (Priority)"
for tidskritiske bransjer og "Reroute via Atlantic/Cape" ved blokkering
av Suez.

## 6.3 Prediksjonsmodell

En Random Forest Regressor er trent for å predikere restitusjonstid
basert på 17 variabler.
-   MAE: 32.89 dager.
-   R2: 0.3356.

## 6.4 Sanntids Risikointegrasjon (Ny funksjon)

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
-   Efficiency Ratio: 0.0605

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

Et sentralt funn er effekten av backup-leverandører. Resultatene viser en betydelig reduksjon i restitusjonstid for selskaper som har alternative leverandører tilgjengelig. En "Efficiency Ratio" på 0.0605 (oppdatert med sanntidsdata) antyder at tidsbesparelsen kommer med en betydelig kostnad, hovedsakelig grunnet flyfrakt og høye drivstoffpriser. For kritiske bransjer som farmasi og luftfart (Aerospace) er dette ofte akseptabelt for å unngå produksjonsstans, mens det for "Consumer Goods" kan være mer lønnsomt å akseptere forsinkelser.

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
