# Prosjektrapport: LOG650 - G07 Dream Team

**Tittel:** Utvikling av et Python-basert beslutningsverktøy for rute-reallokering i globale forsyningskjeder  
**Forfattere:** Hajar Al-Mohannah, Sanosh Senthilkumar  
**Molde, 29. april 2026**

---

## Sammendrag
Forsyningskjeder er i dag svært sårbare for forstyrrelser som geopolitisk risiko, værhendelser og logistiske avvik. Dette prosjektet utvikler et Python-basert beslutningsverktøy som analyserer risiko og foreslår alternative logistiske løsninger for å minimere restitusjonstiden. Ved bruk av omfattende datasett har vi identifisert kritiske faktorer som påvirker forsyningskjedens robusthet, inkludert effekten av backup-leverandører og alvorlighetsgraden av disrupsjoner. Modelleringen viser at proaktive beslutninger kan redusere ledetiden betydelig, selv om det medfører økte transportkostnader.

---

## Abstract
Supply chains are currently highly vulnerable to disruptions such as geopolitical risks, weather events, and logistical deviations. This project develops a Python-based decision-making tool that analyzes risk and proposes alternative logistical solutions to minimize recovery time. Using extensive datasets, we have identified critical factors affecting supply chain resilience, including the impact of backup suppliers and disruption severity. The modeling demonstrates that proactive decisions can significantly reduce lead times, despite increasing transportation costs.

---

# 1.0 Innledning
Globale forsyningskjeder har de siste årene blitt stadig mer komplekse og sårbare. Hendelser som pandemier, geopolitisk uro og logistiske flaskehalser har vist hvor raskt en forstyrrelse kan spre seg gjennom hele verdikjeden. Dette har økt behovet for bedre verktøy som kan identifisere risiko og støtte beslutninger i situasjoner der leveranser står i fare. Formålet med dette prosjektet er å undersøke hvordan datadrevne metoder kan brukes til å styrke robustheten i forsyningskjeder.

## 1.1 Problemstilling
Hvordan kan vi utvikle et Python-basert beslutningsverktøy som automatisk foreslår re-allokering av varer og alternative transportløsninger når en kritisk transportrute eller leverandør svikter, og hvordan påvirker dette forsyningskjedens totale restitusjonstid?

## 1.2 Prosjektets mål
Ved å kombinere maskinlæring og regelbasert beslutningslogikk undersøker vi hvordan virksomheter kan reagere raskere og mer strukturert på forstyrrelser. Prosjektet tar utgangspunkt i sentrale prinsipper innen logistikk og supply chain management, hvor det er en kontinuerlig avveining mellom kostnadseffektivitet og leveringssikkerhet.

# 2.0 Omfang og prosjektbeskrivelse
Prosjektet er avgrenset til analyse av vareflyt mellom ett sentrallager og et begrenset distribusjonsnettverk. Fokus er rettet mot eksterne risikohendelser som påvirker transport og leverandørtilgang.

Det utviklede beslutningsverktøyet er designet for å håndtere situasjoner der forsyningskjeden blir forstyrret, og skal kunne foreslå tiltak som valg av alternative transportruter, bruk av backup-leverandører og re-allokering av varer mellom distribusjonspunkter. Prosjektet er gjennomført som et forskningsprosjekt basert på åpne datasett og simulert data, noe som gir et generelt bilde av hvordan slike modeller kan fungere i praksis.

## 2.1 Antagelser
- Vi antar at historiske data for restitusjonstid er representative for fremtidige hendelser.
- Vi antar at flyfrakt i gjennomsnitt reduserer ledetiden med 60% sammenlignet med sjøfrakt.
- Vi antar at kostnadene for flyfrakt er ca. 7 ganger høyere enn sjøfrakt per enhet.

# 3.0 Litteratur
Gjennomgangen av litteratur de siste fem årene viser en økende trend mot bruk av digitale tvillinger og maskinlæring for å håndtere disrupsjoner i forsyningskjeder. Ivanov (2021) understreker at "viability" (levedyktighet) i en forsyningskjede avhenger av evnen til rask re-konfigurering. Forskning av Hosseini et al. (2019) peker på at backup-leverandører er den mest effektive strategien for å redusere restitusjonstid. Videre har studier av Choi (2020) vist at sanntids beslutningsstøtte kan redusere økonomiske tap med opptil 30% under globale kriser som COVID-19.

# 4.0 Teori
Risikostyring i forsyningskjeder handler om å identifisere, analysere og håndtere hendelser som kan påvirke flyten av varer og tjenester. I litteraturen skilles det ofte mellom to hovedtyper risiko: *disruption risk* og *operational risk*. 

Prosjektet bygger på teorien om *Supply Chain Resilience* (forsyningskjederobusthet), som defineres som evnen til å motstå, tilpasse seg og komme seg etter forstyrrelser (Ponomarov & Holcomb, 2009). 

## 4.1 Restitusjonstid (Recovery Time)
Teoretisk sett følger en disrupsjon en "triangel-modell" hvor ytelsen faller brått og gradvis stiger tilbake til normalen. Vår modell predikerer varigheten av denne stigningen (`full_recovery_days`).

## 4.2 Beslutningsteori under usikkerhet
Vi benytter *Bounded Rationality* (begrenset rasjonalitet) som teoretisk rammeverk, hvor algoritmen hjelper beslutningstakere med å navigere i komplekse valgmuligheter basert på objektive terskelverdier for risiko og kostnad. Dette danner grunnlag for prioritering av tiltak.

# 5.0 Metode og data
## 5.1 Metode
Prosjektet benytter en kvantitativ metode basert på case-studie design. Det er utviklet en strukturert databehandlings- og modellpipeline i Python:
1. **Datarensing og validering:** Gjennomført via `clean_data.py`, `data_check.py` og `consistency_check.py`.
2. **Feature Engineering:** Relevante variabler som `Total Risk Index` konstrueres i `feature_engineering.py`.
3. **Modellutvikling:** Prediksjonsmodell (`recovery_prediction_model.py`) og beslutningsmodell (`decision_model.py`).
4. **Evaluering:** Stresstesting (`stress_test.py`) og måltallsanalyse (`evaluate_objective.py`).

## 5.2 Data
Datasettet består av 100 000 observasjoner av logistiske hendelser. Dataene er delt i et treningssett (80%) og et testsett (20%). Variabler inkluderer forstyrrelsestype, industri, alvorlighetsgrad og geografisk region. 

# 6.0 Modellering
## 6.1 Terskelverdier (Thresholds)
Modellen opererer med tre risikonivåer basert på `Total Risk Index`:
- **Lav risiko (< 0.4):** Ingen umiddelbare tiltak.
- **Moderat risiko (0.4 - 0.7):** Overvåking.
- **Høy risiko (> 0.7):** Automatisk utløsning av tiltak.

## 6.2 Algoritme for Rute-reallokering
Algoritmen foreslår optimale løsninger som "Switch to Air (Priority)" for tidskritiske bransjer og "Reroute via Atlantic/Cape" ved blokkering av Suez.

## 6.4 Prediksjonsmodell (2.2.3)
En Random Forest Regressor er trent for å predikere restitusjonstid basert på 17 variabler.
- **MAE:** 32.89 dager.
- **R2:** 0.3356.

## 6.5 Sanntids Risikointegrasjon (Ny funksjon)
En av prosjektets mest innovative utvidelser er integrasjonen av **NewsAPI** og **OpenWeatherMap API**. Verktøyet henter nå automatisk sanntidsdata for å identifisere trusler før de påvirker forsyningskjeden:
- **Global nyhetsovervåking:** Analyserer nyhetsstrømmer for geopolitisk uro, streik og blokkeringer (f.eks. Suez-kanalen).
- **Meteorologisk overvåking:** Henter faktiske værdata (vindstyrke, ekstremvær) for kritiske logistiske knutepunkter som Panama-kanalen, Shanghai, Rotterdam og Singapore.
- **Dynamisk respons:** Hvis sanntidsrisikoen øker (f.eks. orkanvarsel eller økt konfliktnivå), vil beslutningsmodellen automatisk prioritere proaktive tiltak som omruting eller flyfrakt. Dette flytter verktøyet fra en historisk analysemodell til et proaktivt styringsverktøy.

# 7.0 Analyse
## 7.1 Stresstesting (2.3.2)
...

## 7.2 Evaluering av Målfunksjon (2.3.3)
Med sanntidsdata integrert (per 30. april 2026), viser modellen en mer forsiktig tilnærming med økt fokus på risikoreduksjon:
- **Kostnadsøkning:** 61.09%
- **Reduksjon i Ledetid:** 12.09%
- **Efficiency Ratio:** 0.1979
- **Strategiendring:** Antallet foreslåtte omrutinger via Kapp det gode håp økte betydelig (fra 374 til 2471) som følge av sanntidssignaler om spenninger i Suez-regionen.

# 8.0 Resultat
Resultatene viser at modellen effektivt identifiserer kritiske ordrer.

| Strategi | Andel (%) |
| :--- | :--- |
| Maintain Current Route | 75.4% |
| Switch to Air (Express/Priority) | 17.3% |
| Reroute | 3.8% |
| Manual Review | 3.5% |

![Figur 1: Fordeling av restitusjonstid på tvers av ulike industrier.](005 report/figures/recovery_by_industry.png)

# 9.0 Diskusjon
Funnene i analysen viser tydelig hvordan ulike typer forstyrrelser påvirker restitusjonstid. Spesielt fremstår cyberangrep og naturkatastrofer som hendelser med høy restitusjonstid, noe som indikerer at disse typene risiko er vanskeligere å håndtere operasjonelt. Dette samsvarer med teori hvor eksterne og lite kontrollerbare hendelser gir størst utslag.

Et sentralt funn er effekten av backup-leverandører. Resultatene viser en betydelig reduksjon i restitusjonstid for selskaper som har alternative leverandører tilgjengelig. Dette illustrerer en klassisk avveining i logistikk: balansen mellom kostnadseffektivitet og leveringssikkerhet. En "Efficiency Ratio" på 0.2320 antyder at tidsbesparelsen kommer med en betydelig kostnad, hovedsakelig grunnet flyfrakt. For kritiske bransjer som farmasi og luftfart (Aerospace) er dette ofte akseptabelt for å unngå produksjonsstans.

Modellen har likevel begrensninger. Den er basert på historiske og delvis simulerte data. I virkelige forsyningskjeder vil beslutninger ofte være påvirket av faktorer som kontraktsforhold og politiske forhold. Regresjonsmodellen har også en begrenset forklaringsgrad, noe som tyder på at flere variabler bør inkluderes i fremtidige modeller.

# 10.0 Konklusjon
Beslutningsverktøyet fungerer etter hensikten og gir proaktive råd under kriser. Ved å kombinere risikoanalyse med konkrete tiltak kan virksomheter redusere konsekvensene av forstyrrelser. Fremtidig arbeid bør inkludere mer detaljerte kostnadsdata, flere nivåer i forsyningskjeden og integrasjon av sanntids-værdata for enda mer presise prediksjoner.

# 11.0 Bibliografi
Choi, T. M. (2020). Innovative “bring-service-near-to-customer” operations under Corona-Virus (COVID-19) crisis: Lessons from Hong Kong. *Annals of Operations Research*, 1-25.

Hosseini, S., Ivanov, D., & Dolgui, A. (2019). Review of quantitative methods for supply chain resilience analysis. *Transportation Research Part E: Logistics and Transportation Review*, 125, 285-307.

Ivanov, D. (2021). Supply chain viability and the post-pandemic digital twin. *International Journal of Production Research*, 59(12), 3530-3542.

Ponomarov, S. Y., & Holcomb, M. C. (2009). Understanding the concept of supply chain resilience. *The International Journal of Logistics Management*, 20(1), 124-143.

# 12.0 Vedlegg
*(Eventuelle kildekoder eller utvidede tabeller.)*
