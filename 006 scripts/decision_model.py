import pandas as pd
import numpy as np

def run_decision_model():
    # Load enriched data
    df = pd.read_csv('004 data/enriched_disruption_data.csv')
    
    # 1. Definer terskelverdier (Thresholds)
    RISK_THRESHOLD_HIGH = 0.7
    RISK_THRESHOLD_MODERATE = 0.4
    DELAY_THRESHOLD = 0.1 # 10% delay ratio
    
    def classify_risk(row):
        if row['total_risk_index'] >= RISK_THRESHOLD_HIGH:
            return 'High'
        elif row['total_risk_index'] >= RISK_THRESHOLD_MODERATE:
            return 'Moderate'
        else:
            return 'Low'
            
    df['risk_level'] = df.apply(classify_risk, axis=1)
    
    # 2. Algoritme for rute-reallokering
    def suggest_reallocation(row):
        # Trigger: High risk or significant delay
        if row['risk_level'] == 'High' or row['delay_ratio'] > DELAY_THRESHOLD:
            
            # Spesifikk logikk basert på industri og rute
            if row['Product_Category'] in ['Pharmaceuticals', 'Semiconductors', 'Consumer Electronics']:
                if row['Transportation_Mode'] == 'Sea':
                    return 'Switch to Air (Priority)'
            
            if row['Route_Type'] == 'Suez' and row['risk_level'] == 'High':
                return 'Reroute via Atlantic/Cape'
                
            if row['Transportation_Mode'] == 'Sea':
                return 'Switch to Air (Express)'
            
            return 'Manual Review Required'
            
        return 'Maintain Current Route'

    df['reallocation_strategy'] = df.apply(suggest_reallocation, axis=1)
    
    # 3. Beregn potensiell tidsbesparelse (Simulering)
    # Anta at Air reduserer ledetid med 60% sammenlignet med Sea
    def estimate_new_lead_time(row):
        if 'Air' in str(row['reallocation_strategy']):
            return row['Scheduled_Lead_Time_Days'] * 0.4
        return row['Scheduled_Lead_Time_Days']

    df['estimated_new_lead_time'] = df.apply(estimate_new_lead_time, axis=1)
    
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
