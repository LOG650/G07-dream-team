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
            print("Sanntidssignaler lastet inn.")

    # 1. Definer terskelverdier (Thresholds)
    RISK_THRESHOLD_HIGH = 0.7
    RISK_THRESHOLD_MODERATE = 0.4
    DELAY_THRESHOLD = 0.1 # 10% delay ratio
    COST_THRESHOLD_HIGH = 10_000 # Anta at ordrer over 10k USD er prioritert
    
    def classify_risk(row):
        base_risk = row['total_risk_index']
        
        # Sjekk om ruten eller hendelsen har høy sanntidsrisiko
        route = row['Route_Type']
        event = row['Disruption_Event']
        
        # Suez-spesifikk sanntidsoverstyring
        if route == 'Suez' and 'Suez' in live_risk:
            base_risk = max(base_risk, live_risk['Suez']['score'])
        
        # Geopolitisk sanntidsoverstyring
        if 'Geopolitical' in str(event) and 'Geopolitical' in live_risk:
            base_risk = max(base_risk, live_risk['Geopolitical']['score'])
            
        if base_risk >= RISK_THRESHOLD_HIGH:
            return 'High'
        elif base_risk >= RISK_THRESHOLD_MODERATE:
            return 'Moderate'
        else:
            return 'Low'
            
    df['risk_level'] = df.apply(classify_risk, axis=1)
    
    # 2. Algoritme for rute-reallokering
    def suggest_reallocation(row):
        # Trigger: High risk, significant delay, or high value order
        is_high_risk = row['risk_level'] == 'High'
        is_delayed = row['delay_ratio'] > DELAY_THRESHOLD
        is_high_value = row['Shipping_Cost_USD'] > COST_THRESHOLD_HIGH
        
        if is_high_risk or is_delayed or is_high_value:
            
            # Prioritert logikk for tidskritiske bransjer eller høykost-ordrer
            critical_industries = ['Pharmaceuticals', 'Semiconductors', 'Consumer Electronics', 'Aerospace']
            if row['Product_Category'] in critical_industries or is_high_value:
                if row['Transportation_Mode'] == 'Sea':
                    return 'Switch to Air (Priority)'
            
            if row['Route_Type'] == 'Suez' and is_high_risk:
                return 'Reroute via Atlantic/Cape'
                
            if row['Transportation_Mode'] == 'Sea':
                return 'Switch to Air (Express)'
            
            return 'Manual Review Required'
            
        return 'Maintain Current Route'

    df['reallocation_strategy'] = df.apply(suggest_reallocation, axis=1)
    
    # 3. Kostnad og tidsbesparelse
    def calculate_impact(row):
        strategy = str(row['reallocation_strategy'])
        new_cost = row['Shipping_Cost_USD']
        new_lead_time = row['Scheduled_Lead_Time_Days']
        
        if 'Switch to Air' in strategy:
            new_cost *= 7.0
            new_lead_time *= 0.4 # 60% reduksjon
        elif 'Reroute' in strategy:
            new_cost *= 1.3
            new_lead_time *= 1.1 # 10% økning pga lengre rute
            
        return pd.Series([new_cost, new_lead_time])

    df[['new_shipping_cost_usd', 'estimated_new_lead_time']] = df.apply(calculate_impact, axis=1)
    
    # Lagre resultater
    output_path = '004 data/decision_model_results.csv'
    df.to_csv(output_path, index=False)
    
    # Oppsummering for rapport
    summary = df['reallocation_strategy'].value_counts()
    print("Modellutvikling ferdig. Oppsummering av strategier:")
    print(summary)
    print(f"\nResultater lagret i {output_path}")

if __name__ == "__main__":
    run_decision_model()
