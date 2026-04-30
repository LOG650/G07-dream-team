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
Introduksjonen beskriver bakgrunnen for prosjektet og behovet for mer robuste beslutningsverktøy i moderne logistikk.

## 1.1 Problemstilling
Hvordan kan vi utvikle et Python-basert beslutningsverktøy som automatisk foreslår re-allokering av varer og alternative transportløsninger når en kritisk transportrute eller leverandør svikter, og hvordan påvirker dette forsyningskjedens totale restitusjonstid?

## 1.3 Avgrensinger
Prosjektet fokuserer på risikostyring og robusthet i en forenklet forsyningskjede. Analysen baseres på åpne datasett som beskriver logistiske avvik og historisk restitusjonstid. Prosjektet er avgrenset til vareflyten mellom ett sentrallager og et begrenset antall distribusjonspunkter, med fokus på eksterne risikohendelser.

## 1.4 Antagelser
- Vi antar at historiske data for restitusjonstid er representative for fremtidige hendelser.
- Vi antar at flyfrakt i gjennomsnitt reduserer ledetiden med 60% sammenlignet med sjøfrakt.
- Vi antar at kostnadene for flyfrakt er ca. 7 ganger høyere enn sjøfrakt per enhet.

# 2.0 Litteratur
*(Dette kapittelet vil diskutere de viktigste bidragene de 5 siste årene innen forsyningskjederobusthet og risikostyring.)*

# 3.0 Teori
*(Her beskrives teoretisk perspektiv på risikostyring, restitusjonstid og beslutningsteori i logistikksammenheng.)*

# 4.0 Casebeskrivelse
Casestudien tar utgangspunkt i en global forsyningskjede som frakter varer fra Asia til Europa og Amerika via kritiske ruter som Suez-kanalen og Stillehavet. Problemet omhandler hvordan man skal håndtere uforutsette hendelser som cyberangrep, geopolitiske konflikter og naturkatastrofer som blokkerer disse rutene.

# 5.0 Metode og data
## 5.1 Metode
Prosjektet benytter en kvantitativ metode basert på case-studie design.
- **Forskingsperspektiv:** Deskriptiv og prediktiv analyse.
- **Analysemetoder:** Statistisk regresjon for prediksjon og regelbaserte algoritmer for beslutningsstøtte.
- **Verktøy:** Python med biblioteker som Pandas, Scikit-learn, Matplotlib og Seaborn.

## 5.2 Data
Datasettet består av 100 000 observasjoner av logistiske hendelser.
- **Datakilder:** Syntetiske og åpne datasett for supply chain disruption.
- **Cleaning:** Data er renset for manglende verdier og inkonsistente rutenavn.
- **Feature Engineering:** Det er opprettet nye variabler som `Delay Ratio`, `Total Risk Index` og `Recovery Speed`.
- **Separering:** Data er delt i et treningssett (80%) og et testsett (20%).

# 6.0 Modellering
## 6.1 Terskelverdier (Thresholds)
Modellen opererer med tre risikonivåer basert på `Total Risk Index`:
- **Lav risiko (< 0.4):** Ingen umiddelbare tiltak.
- **Moderat risiko (0.4 - 0.7):** Overvåking.
- **Høy risiko (> 0.7):** Automatisk utløsning av tiltak.

## 6.2 Algoritme for Rute-reallokering
Algoritmen foreslår optimale løsninger som "Switch to Air (Priority)" for tidskritiske bransjer og "Reroute via Atlantic/Cape" ved blokkering av Suez.

## 6.4 Prediksjonsmodell (2.2.3)
En Lineær Regresjonsmodell er trent for å predikere restitusjonstid.
- **MAE:** 31.56 dager.
- **R2:** 0.3859.

# 7.0 Analyse
## 7.1 Stresstesting (2.3.2)
Simulering av en total Suez-blokkering (Risiko = 0.95).

![Figur 2: Skifte i beslutningsstrategier ved normal drift vs. global Suez-blokkering.](005 report/figures/stress_test_comparison.png)

## 7.2 Evaluering av Målfunksjon (2.3.3)
Sammenligning av kostnad vs. tidsbesparelse.

![Figur 3: Forholdet mellom økte transportkostnader og oppnådd tidsbesparelse.](005 report/figures/cost_leadtime_tradeoff.png)

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
Analysen viser en klar trade-off mellom kostnad og ledetid. En "Efficiency Ratio" på 0.2423 antyder at tidsbesparelsen kommer med en betydelig kostnad, men for kritiske bransjer som farmasi er dette ofte akseptabelt for å unngå "stock-outs".

# 10.0 Konklusjon
Beslutningsverktøyet fungerer etter hensikten og gir proaktive råd under kriser. Fremtidig arbeid bør inkludere mer detaljerte kostnadsdata og integrasjon av sanntids-værdata.

# 11.0 Bibliografi
*(Referanser i APA 7th stil vil bli lagt til her.)*

# 12.0 Vedlegg
*(Eventuelle kildekoder eller utvidede tabeller.)*
