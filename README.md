# LOG650 - G07 Dream Team: Python-basert Beslutningsverktøy

Dette prosjektet inneholder et Python-basert verktøy for å forutsi restitusjonstid og foreslå logistiske tiltak ved forstyrrelser i globale forsyningskjeder. Verktøyet er utvidet med sanntids overvåking av risiko via NewsAPI og OpenWeatherMap.

## 1. Forutsetninger
Du må ha Python 3.x installert på din maskin.

## 2. Installasjon
Installer de nødvendige bibliotekene ved å kjøre følgende kommando i terminalen:
```bash
pip install pandas numpy scikit-learn requests matplotlib seaborn joblib
```

## 3. Brukerveiledning (Slik kjøres verktøyet)

For å se verktøyet i aksjon med sanntidsdata, følg disse stegene i rekkefølge:

### Steg 1: Oppdater Sanntidsrisiko
Dette skriptet henter siste nytt om logistikk-forstyrrelser og værforhold i kritiske havner.
```bash
python "006 scripts/real_time_risk_monitor.py"
```
*Merk: API-nøkler er integrert i koden, men har daglige begrensninger.*

### Steg 2: Kjør Beslutningsmodellen
Dette skriptet analyserer logistikkdataene og kombinerer dem med sanntidssignalene fra steg 1 for å foreslå tiltak (f.eks. omruting eller flyfrakt).
```bash
python "006 scripts/decision_model.py"
```

### Steg 3: Evaluering og Visualisering
Generer oppdaterte figurer og måltall som viser effekten av de foreslåtte tiltakene.
```bash
python "006 scripts/evaluate_objective.py"
python "006 scripts/visualize_results.py"
```

## 4. Prosjektstruktur
- `004 data/`: Inneholder alle datasett og genererte resultater.
- `005 report/figures/`: Inneholder genererte grafer til rapporten.
- `006 scripts/`: Inneholder all kildekode (prediksjonsmodell, beslutningslogikk, etc.).
- `014 fase 4 - report/`: Inneholder den endelige prosjektrapporten i både Markdown og Word-format.

## 5. Merknad om modellfil (.pkl)
På grunn av størrelsesbegrensninger på GitHub er ikke den ferdigtrente modellfilen `recovery_predictor.pkl` inkludert i repoet. Denne kan genereres lokalt ved å kjøre:
```bash
python "006 scripts/recovery_prediction_model.py"
```
