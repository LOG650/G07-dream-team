import pandas as pd
import numpy as np
import os

def run_sensitivity_analysis():
    # Last inn resultatene fra beslutningsmodellen
    file_path = '004 data/decision_model_results.csv'
    if not os.path.exists(file_path):
        print("Error: Model-resultater ikke funnet.")
        return

    df = pd.read_csv(file_path)
    
    # Parametere for analyse
    air_cost_multipliers = [3.0, 5.0, 7.0, 9.0, 12.0]  # Hvor mange ganger dyrere er fly?
    lead_time_reductions = [0.4, 0.5, 0.6, 0.7, 0.8]   # 1 - reduksjon (0.4 betyr 60% reduksjon)
    
    sensitivity_results = []

    print("KJØRER SENSITIVITETSANALYSE")
    print("-" * 60)
    print(f"{'Air Cost Mult.':<15} | {'LT Red. %':<12} | {'Cost Inc. %':<12} | {'LT Red. % (Tot)':<15} | {'Eff. Ratio':<10}")
    print("-" * 60)

    for cost_mult in air_cost_multipliers:
        for lt_factor in lead_time_reductions:
            # Beregn ny kostnad og ledetid for dette scenarioet
            def calc_scenario(row):
                base_cost = row['Shipping_Cost_USD']
                base_lt = row['Scheduled_Lead_Time_Days']
                strategy = str(row['reallocation_strategy'])
                
                if 'Switch to Air' in strategy:
                    new_cost = base_cost * cost_mult
                    new_lt = base_lt * lt_factor
                elif 'Reroute' in strategy:
                    new_cost = base_cost * 1.3
                    new_lt = base_lt * 1.1
                else:
                    new_cost = base_cost
                    new_lt = row['estimated_new_lead_time'] # Bruk modellens prediksjon hvis ingen tiltak
                
                return pd.Series([new_cost, new_lt])

            scenario_df = df.apply(calc_scenario, axis=1)
            scenario_df.columns = ['cost', 'lt']
            
            total_cost_base = df['Shipping_Cost_USD'].sum()
            total_cost_scenario = scenario_df['cost'].sum()
            
            total_days_base = df['Scheduled_Lead_Time_Days'].sum()
            total_days_scenario = scenario_df['lt'].sum()
            
            cost_inc = ((total_cost_scenario - total_cost_base) / total_cost_base) * 100
            lt_red = ((total_days_base - total_days_scenario) / total_days_base) * 100
            eff_ratio = lt_red / cost_inc if cost_inc > 0 else 0
            
            sensitivity_results.append({
                'Air_Cost_Multiplier': cost_mult,
                'Lead_Time_Reduction_Factor': 1 - lt_factor,
                'Total_Cost_Increase_Pct': cost_inc,
                'Total_LT_Reduction_Pct': lt_red,
                'Efficiency_Ratio': eff_ratio
            })
            
            print(f"{cost_mult:<15.1f} | {(1-lt_factor)*100:<12.0f} | {cost_inc:<12.2f} | {lt_red:<15.2f} | {eff_ratio:.4f}")

    # Lagre resultatene
    res_df = pd.DataFrame(sensitivity_results)
    res_df.to_csv('004 data/sensitivity_analysis_results.csv', index=False)
    print("-" * 60)
    print("Analyse ferdig. Lagret i 004 data/sensitivity_analysis_results.csv")

if __name__ == "__main__":
    run_sensitivity_analysis()
