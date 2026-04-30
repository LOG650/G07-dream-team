import pandas as pd
import numpy as np
import os
import json

def run_decision_model():
    # Load enriched data
    df = pd.read_csv('004 data/enriched_disruption_data.csv')
    
    # Last inn sanntidssignaler hvis de eksisterer
    live_risk = {}
    if os.path.exists('004 data/live_risk_signals.json'):
        with open('004 data/live_risk_signals.json', 'r') as f:
            live_risk = json.load(f)
            print("Sanntidssignaler lastet inn (inkl. Olje og AIS).")

    # 1. Definer terskelverdier (Thresholds)
    RISK_THRESHOLD_HIGH = 0.7
    RISK_THRESHOLD_MODERATE = 0.4
    DELAY_THRESHOLD = 0.1 # 10% delay ratio
    COST_THRESHOLD_HIGH = 10_000 
    
    # Dynamisk kostnadstillegg basert på oljepris
    oil_cost_multiplier = 1.0
    if 'Oil_Price' in live_risk:
        # Hvis oljepris > $90, legg til 15% på alle ruter
        if live_risk['Oil_Price']['price'] > 90:
            oil_cost_multiplier = 1.15
            print(f"Advarsel: Høy oljepris (${live_risk['Oil_Price']['price']}). Legger til 15% drivstofftillegg.")

    def classify_risk(row):
        base_risk = row['total_risk_index']
        route = row['Route_Type']
        event = row['Disruption_Event']
        
        # Hormuz/Suez sanntidsoverstyring
        if 'Suez' in route and 'Suez' in live_risk:
            base_risk = max(base_risk, live_risk['Suez']['score'])
        
        if 'Hormuz_AIS' in live_risk:
            # Hvis vi er i Midtøsten-ruter og skipstrafikken er lav
            if any(x in str(route) for x in ['Middle East', 'Suez', 'Indian Ocean']):
                base_risk = max(base_risk, live_risk['Hormuz_AIS']['score'])
        
        # Oljepris som risikofaktor for driftsstabilitet
        if 'Oil_Price' in live_risk:
            base_risk = max(base_risk, live_risk['Oil_Price']['score'] * 0.5) # Olje teller 50% inn i risiko
            
        if base_risk >= RISK_THRESHOLD_HIGH:
            return 'High'
        elif base_risk >= RISK_THRESHOLD_MODERATE:
            return 'Moderate'
        else:
            return 'Low'
            
    df['risk_level'] = df.apply(classify_risk, axis=1)
    
    # 2. Algoritme for rute-reallokering
    def suggest_reallocation(row):
        is_high_risk = row['risk_level'] == 'High'
        is_delayed = row['delay_ratio'] > DELAY_THRESHOLD
        is_high_value = row['Shipping_Cost_USD'] > COST_THRESHOLD_HIGH
        
        if is_high_risk or is_delayed or is_high_value:
            critical_industries = ['Pharmaceuticals', 'Semiconductors', 'Consumer Electronics', 'Aerospace']
            
            # Spesialhåndtering for Hormuz/Suez risiko
            if is_high_risk and any(x in str(row['Route_Type']) for x in ['Suez', 'Middle East']):
                if row['Product_Category'] in critical_industries:
                    return 'Switch to Air (Priority)'
                return 'Reroute via Atlantic/Cape'
            
            if row['Product_Category'] in critical_industries or is_high_value:
                if row['Transportation_Mode'] == 'Sea':
                    return 'Switch to Air (Priority)'
            
            if row['Transportation_Mode'] == 'Sea':
                return 'Switch to Air (Express)'
            
            return 'Manual Review Required'
            
        return 'Maintain Current Route'

    df['reallocation_strategy'] = df.apply(suggest_reallocation, axis=1)
    
    # 3. Kostnad og tidsbesparelse med dynamisk oljepris
    def calculate_impact(row):
        strategy = str(row['reallocation_strategy'])
        # Start med grunnkostnad + oljetillegg
        current_cost = row['Shipping_Cost_USD'] * oil_cost_multiplier
        new_lead_time = row['Scheduled_Lead_Time_Days']
        
        if 'Switch to Air' in strategy:
            new_cost = current_cost * 7.0
            new_lead_time *= 0.4
        elif 'Reroute' in strategy:
            new_cost = current_cost * 1.3
            new_lead_time *= 1.1
        else:
            new_cost = current_cost
            
        return pd.Series([new_cost, new_lead_time])

    df[['new_shipping_cost_usd', 'estimated_new_lead_time']] = df.apply(calculate_impact, axis=1)
    
    # Lagre resultater
    output_path = '004 data/decision_model_results.csv'
    df.to_csv(output_path, index=False)
    
    # Oppsummering
    summary = df['reallocation_strategy'].value_counts()
    print("Beslutningsmodell oppdatert med sanntids maritime data.")
    print(summary)

if __name__ == "__main__":
    run_decision_model()
