# Prosjektrapport: LOG650 - G07 Dream Team

**Gruppe:** G07 Dream Team  
**Medlemmer:** Hajar Al-Mohannah, Sanosh Senthilkumar  
**Dato:** 29. april 2026  

---

## 1. Sammendrag (Abstract)
Forsyningskjeder er i dag svært sårbare for forstyrrelser som geopolitisk risiko, værhendelser og logistiske avvik. Slike hendelser kan føre til forsinkelser, økte kostnader og redusert leveringsgrad. Dette prosjektet utvikler et Python-basert beslutningsverktøy som analyserer risiko og foreslår alternative logistiske løsninger for å minimere restitusjonstiden. Ved bruk av omfattende datasett har vi identifisert kritiske faktorer som påvirker forsyningskjedens robusthet, inkludert effekten av backup-leverandører og alvorlighetsgraden av disrupsjoner.

## 2. Innledning
### 2.1 Problemstilling
Hvordan kan vi utvikle et Python-basert beslutningsverktøy som automatisk foreslår re-allokering av varer og alternative transportløsninger når en kritisk transportrute eller leverandør svikter, og hvordan påvirker dette forsyningskjedens totale restitusjonstid?

### 2.2 Målsetning
Målet med prosjektet er å utvikle en modell som kan analysere risiko i en forsyningskjede og foreslå alternative logistiske løsninger når en forstyrrelse oppstår.

## 3. Omfang og Avgrensning
Prosjektet fokuserer på risikostyring og robusthet i en forenklet forsyningskjede. Analysen baseres på åpne datasett som beskriver logistiske avvik og historisk restitusjonstid. Prosjektet er avgrenset til vareflyten mellom ett sentrallager og et begrenset antall distribusjonspunkter, med fokus på eksterne risikohendelser.

## 4. Metodikk
### 4.1 Databehandling og Sammenslåing (Merging)
For å sikre robustheten i den kvantitative analysen er originaldatasettet (100 000 observasjoner) delt inn i to uavhengige sett:
*   **Treningssett (80%):** 80 000 observasjoner brukt til mønstergjenkjenning og modellutvikling.
*   **Testsett (20%):** 20 000 observasjoner brukt til validering.

Siden prosjektet benytter data fra flere kilder uten en felles unik nøkkel, er det gjennomført en statistisk sammenslåing basert på bransjemapping (`Industry` mot `Product_Category`). Dette muliggjør analyse av sammenhengen mellom logistiske forstyrrelser og produksjonsmessig restitusjonstid innenfor samme sektor.

### 4.2 Feature Engineering
For å forbedre modellens prediksjonsevne har vi utviklet flere nye variabler (features):
*   **Delay Ratio:** Forholdet mellom faktisk forsinkelse og planlagt ledetid, som gir et bilde av den relative påvirkningen på logistikken.
*   **Total Risk Index:** En vektet kombinasjon av geopolitisk risiko (60%) og vær-alvorlighetsgrad (40%).
*   **Recovery Speed:** Beregnet som antall dager til full restitusjon delt på disrupsjonens alvorlighetsgrad. Dette måler effektiviteten i bedriftens krisehåndtering.

### 4.3 Verktøy
- **Python:** For databehandling og utvikling av beslutningsmodellen.
- **Visual Studio Code:** Utviklingsmiljø.
- **GitHub:** Versjonskontroll og samarbeid.
- **MS Project:** Tidsplanlegging og oppfølging.

## 5. Resultater og Analyse
Basert på foreløpig analyse av 100 000 observasjoner har vi funnet følgende:

### 5.1 Restitusjonstid etter Disrupsjonstype (Dager)
| Disrupsjonstype | Gjennomsnittlig Restitusjon | Median | Max | Min |
| :--- | :--- | :--- | :--- | :--- |
| Cyber Attack | 99.62 | 84.0 | 798.0 | 8.0 |
| Factory Incident | 71.27 | 58.0 | 550.0 | 8.0 |
| Geopolitical | 81.17 | 67.0 | 545.0 | 8.0 |
| Labor Strike | 62.77 | 49.0 | 453.0 | 8.0 |
| Natural Disaster | 90.60 | 76.0 | 521.0 | 8.0 |
| Port Congestion | 59.07 | 46.0 | 420.0 | 8.0 |

![Fordeling av restitusjonstid per bransje](005 report/figures/recovery_by_industry.png)
*Figur 1: Fordeling av restitusjonstid på tvers av ulike industrier.*

### 5.2 Effekt av Backup-leverandører
Analysen viser at selskaper med backup-leverandører har en gjennomsnittlig restitusjonstid på **64.28 dager**, sammenlignet med **90.30 dager** for de uten. Dette representerer en betydelig forbedring i robusthet.

### 5.3 Økonomisk Innvirkning per Industri
| Industri | Gjennomsnittlig Tap (USD) |
| :--- | :--- |
| Aerospace | $6,067,862.37 |
| Automotive | $2,432,135.08 |
| Pharmaceuticals | $3,664,839.16 |

## 6. Modellutvikling og Beslutningsstøtte
I denne fasen har vi utviklet en algoritme for beslutningsstøtte som automatisk foreslår tiltak basert på sanntidsdata om risiko og forsinkelser.

### 6.1 Programmering av Terskelverdier (Thresholds)
Modellen opererer med tre risikonivåer basert på `Total Risk Index`:
*   **Lav risiko (< 0.4):** Ingen umiddelbare tiltak.
*   **Moderat risiko (0.4 - 0.7):** Overvåking og beredskap.
*   **Høy risiko (> 0.7):** Automatisk utløsning av re-allokeringsforslag.

I tillegg utløses tiltak dersom `Delay Ratio` overstiger 0.1 (10% forsinkelse i forhold til planlagt ledetid).

### 6.2 Algoritme for Rute-reallokering
Algoritmen vurderer industri, transportmåte og rute for å foreslå optimale løsninger:
1.  **Switch to Air (Priority):** Brukes for tidskritiske bransjer som farmasøytisk og elektronikk ved høy risiko eller forsinkelse.
2.  **Reroute via Atlantic/Cape:** Foreslås dersom Suez-ruten har høy risiko.
3.  **Switch to Air (Express):** Standard tiltak for å redusere ledetid ved logistiske flaskehalser.

### 6.3 Resultater fra Modellkjøring
Ved testing på 10 000 ordrer ga modellen følgende fordeling av strategier:

| Strategi | Antall Ordrer | Prosentandel |
| :--- | :--- | :--- |
| Maintain Current Route | 7 540 | 75.4% |
| Switch to Air (Express) | 1 105 | 11.1% |
| Switch to Air (Priority) | 618 | 6.2% |
| Reroute via Atlantic/Cape | 384 | 3.8% |
| Manual Review Required | 353 | 3.5% |

Dette viser at modellen er i stand til å identifisere de ~25% av ordrene som krever aktiv håndtering for å sikre forsyningskjedens stabilitet.

### 6.4 Prediksjonsmodell for Restitusjon (2.2.3)
Vi har implementert en maskinlæringsmodell (Lineær Regresjon) for å predikere antall dager til full restitusjon basert på disrupsjonens alvorlighetsgrad, produksjonspåvirkning og tilgang på backup-leverandører.
*   **MAE (Mean Absolute Error):** 31.56 dager.
*   **R2 Score:** 0.3859.

## 7. Simulering og Kvalitetssikring (2.3)
### 7.1 Unittesting (2.3.1)
For å sikre systemets integritet er det gjennomført automatiserte tester av kjernefunksjonaliteten:
*   **Test av beslutningslogikk:** Verifiserer at terskelverdier utløser korrekte re-allokeringsstrategier (f.eks. omruting ved høy risiko i Suez).
*   **Test av prediksjonsmodell:** Bekrefter at modellen kan lastes korrekt og generere logiske estimater for restitusjonstid.

### 7.2 Stresstesting (2.3.2)
Vi har gjennomført stresstester for å evaluere hvordan modellen håndterer "Black Swan"-hendelser. Det mest kritiske scenariet var en **total blokkering av Suez-kanalen**, der risikoindeksen for alle Suez-ruter ble satt til 0.95.

![Sammenligning av strategier ved stresstest](005 report/figures/stress_test_comparison.png)
*Figur 2: Skifte i beslutningsstrategier ved normal drift vs. global Suez-blokkering.*

### 7.3 Evaluering av Målfunksjon (2.3.3)
For å vurdere modellens økonomiske og operasjonelle bærekraft har vi evaluert målfunksjonen ved å sammenligne total transportkostnad mot total spart ledetid for 10 000 ordrer.

**Nøkkeltall fra evaluering:**
| Metrikk | Verdi |
| :--- | :--- |
| Økning i transportkostnad | 45.90% |
| Reduksjon i total ledetid | 11.12% |
| Efficiency Ratio | 0.2423 |

![Trade-off Kostnad vs Ledetid](005 report/figures/cost_leadtime_tradeoff.png)
*Figur 3: Forholdet mellom økte transportkostnader og oppnådd tidsbesparelse.*

Analysen viser at selv om transportkostnadene øker betydelig, oppnår vi en reduksjon i ledetid på over 11%. For tidskritiske bransjer vil denne tidsbesparelsen være kritisk for å unngå produksjonsstans, noe som rettferdiggjør den økte investeringen i transport.

## 8. Diskusjon
*(Her kan vi fylle ut mer om implikasjonene av funnene våre.)*

## 9. Referanser
- APA 7th stil følges i henhold til prosjektets retningslinjer.
