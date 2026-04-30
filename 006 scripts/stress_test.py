import pandas as pd
import numpy as np
import os

def run_stress_test():
    # Last inn berikede data (baselinjen)
    file_path = '004 data/enriched_disruption_data.csv'
    if not os.path.exists(file_path):
        print("Error: Baseline-data ikke funnet.")
        return

    df_base = pd.read_csv(file_path)
    
    # 1. Definer Scenarier
    # Scenario A: "Global Suez Blockage" - Alle Suez-ruter får maks risiko
    df_suez_stress = df_base.copy()
    df_suez_stress.loc[df_suez_stress['Route_Type'] == 'Suez', 'total_risk_index'] = 0.95
    
    # Scenario B: "Cyber Blackout" - Alle Cyber Attack hendelser får ekstrem forsinkelse
    df_cyber_stress = df_base.copy()
    df_cyber_stress.loc[df_base['Disruption_Event'] == 'Cyber Attack', 'delay_ratio'] = 3.0
    
    # 2. Gjenbruk beslutningslogikk fra decision_model.py
    def apply_decision_logic(df):
        RISK_THRESHOLD_HIGH = 0.7
        DELAY_THRESHOLD = 0.1
        
        def suggest(row):
            risk_level = 'High' if row['total_risk_index'] >= RISK_THRESHOLD_HIGH else 'Low'
            if risk_level == 'High' or row['delay_ratio'] > DELAY_THRESHOLD:
                if row['Product_Category'] in ['Pharmaceuticals', 'Semiconductors', 'Consumer Electronics']:
                    if row['Transportation_Mode'] == 'Sea': return 'Switch to Air (Priority)'
                if row['Route_Type'] == 'Suez' and risk_level == 'High': return 'Reroute via Atlantic/Cape'
                if row['Transportation_Mode'] == 'Sea': return 'Switch to Air (Express)'
                return 'Manual Review Required'
            return 'Maintain Current Route'
        
        return df.apply(suggest, axis=1)

    # 3. Kjør simuleringer
    res_base = apply_decision_logic(df_base).value_counts(normalize=True) * 100
    res_suez = apply_decision_logic(df_suez_stress).value_counts(normalize=True) * 100
    res_cyber = apply_decision_logic(df_cyber_stress).value_counts(normalize=True) * 100

    # 4. Sammenlign resultater
    print("STRESSTEST RESULTATER (Andel ordrer i %)")
    print("-" * 50)
    print(f"{'Strategi':<25} | {'Base':<10} | {'Suez Stress':<12} | {'Cyber Stress':<12}")
    print("-" * 50)
    
    all_strategies = set(res_base.index) | set(res_suez.index) | set(res_cyber.index)
    for strat in sorted(all_strategies):
        b = res_base.get(strat, 0)
        s = res_suez.get(strat, 0)
        c = res_cyber.get(strat, 0)
        print(f"{strat:<25} | {b:>9.1f}% | {s:>11.1f}% | {c:>11.1f}%")

    # Lagre stress-data for rapporten
    summary_df = pd.DataFrame({
        'Strategy': list(all_strategies),
        'Base': [res_base.get(s, 0) for s in all_strategies],
        'Suez_Stress': [res_suez.get(s, 0) for s in all_strategies],
        'Cyber_Stress': [res_cyber.get(s, 0) for s in all_strategies]
    })
    summary_df.to_csv('004 data/stress_test_summary.csv', index=False)
    print("\nStresstest ferdig. Oppsummering lagret i 004 data/stress_test_summary.csv")

if __name__ == "__main__":
    run_stress_test()
