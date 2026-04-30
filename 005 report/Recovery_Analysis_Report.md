Kan # Statistisk Analyse: Supply Chain Disruption Recovery

**Dato:** 2026-04-12
**Totalt antall observasjoner:** 100000

## 0. Datametodikk og Separering

For å sikre robustheten i den kvantitative analysen og legge til rette for eventuell prediktiv modellering (maskinlæring), er originaldatasettet delt inn i to uavhengige sett:

- **Treningssett (80%):** 80 000 observasjoner brukt til å identifisere mønstre og utvikle modeller.
- **Testsett (20%):** 20 000 observasjoner holdt tilbake for å validere funnene og teste modellens generaliseringsevne.

Denne separeringen er et kritisk steg i LOG650-prosjektet for å unngå overfitting og sikre at konklusjonene ikke bare gjelder for det spesifikke utvalget, men er representative for populasjonen.

## 1. Restitusjonstid etter Disrupsjonstype (Dager)

| Disrupsjonstype  | Gjennomsnittlig Restitusjon | Median | Max   | Min |
| :--------------- | :-------------------------- | :----- | :---- | :-- |
| Cyber Attack     | 99.62                       | 84.0   | 798.0 | 8.0 |
| Factory Incident | 71.27                       | 58.0   | 550.0 | 8.0 |
| Geopolitical     | 81.17                       | 67.0   | 545.0 | 8.0 |
| Labor Strike     | 62.77                       | 49.0   | 453.0 | 8.0 |
| Natural Disaster | 90.60                       | 76.0   | 521.0 | 8.0 |
| Port Congestion  | 59.07                       | 46.0   | 420.0 | 8.0 |

## 2. Effekt av Backup-leverandører

| Har Backup-leverandør | Gjennomsnittlig Full Restitusjon (Dager) | Antall |
| :-------------------- | :--------------------------------------- | :----- |
| False                 | 90.30                                    | 44426  |
| True                  | 64.28                                    | 55574  |

## 3. Omsetningstap per Industri (USD)

| Industri        | Totalt Tap         | Gjennomsnittlig Tap |
| :-------------- | :----------------- | :------------------ |
| Aerospace       | $60,975,948,912.37 | $6,067,862.37       |
| Automotive      | $60,642,856,192.42 | $2,432,135.08       |
| Consumer Goods  | $19,791,007,002.04 | $981,794.18         |
| Electronics     | $55,843,813,421.24 | $1,871,190.64       |
| Pharmaceuticals | $55,027,560,037.15 | $3,664,839.16       |

## 4. Alvorlighetsgrad vs. Produksjonspåvirkning

| Alvorlighetsgrad | Gjennomsnittlig Produksjonstap (%) |
| :--------------- | :--------------------------------- |
| 1                | 13.28%                             |
| 2                | 25.12%                             |
| 3                | 37.50%                             |
| 4                | 50.07%                             |
| 5                | 62.25%                             |
