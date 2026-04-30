import pandas as pd
import numpy as np
import os

def evaluate_objective_function():
    # Last inn resultatene fra beslutningsmodellen
    file_path = '004 data/decision_model_results.csv'
    if not os.path.exists(file_path):
        print("Error: Model-resultater ikke funnet.")
        return

    df = pd.read_csv(file_path)
    
    # 1. Definer kostnadsparametere (Estimater basert på logistikkstandarder)
    # Flyfrakt er typisk 5-10 ganger dyrere enn sjøfrakt per kg
    # Omruting via Kapp (Atlantic) øker drivstoffkostnader med ca. 30%
    
    def calculate_new_cost(row):
        base_cost = row['Shipping_Cost_USD']
        strategy = str(row['reallocation_strategy'])
        
        if 'Switch to Air' in strategy:
            # Anta 7x økning i kostnad for flyfrakt
            return base_cost * 7.0
        elif 'Reroute' in strategy:
            # Anta 1.3x økning for omruting
            return base_cost * 1.3
        return base_cost

    df['new_shipping_cost_usd'] = df.apply(calculate_new_cost, axis=1)
    
    # 2. Sammenlign totaler
    total_cost_base = df['Shipping_Cost_USD'].sum()
    total_cost_model = df['new_shipping_cost_usd'].sum()
    
    total_days_base = df['Scheduled_Lead_Time_Days'].sum()
    total_days_model = df['estimated_new_lead_time'].sum()
    
    # 3. Beregn KPIer
    cost_increase_pct = ((total_cost_model - total_cost_base) / total_cost_base) * 100
    lead_time_reduction_pct = ((total_days_base - total_days_model) / total_days_base) * 100
    
    # "Efficiency Ratio" - Hvor mange % ledetid sparer vi per % kostnadsøkning
    efficiency_ratio = lead_time_reduction_pct / cost_increase_pct if cost_increase_pct > 0 else 0

    print("EVALUERING AV MÅLFUNKSJON (2.3.3)")
    print("-" * 50)
    print(f"Total Transportkostnad (Base):  ${total_cost_base:,.2f}")
    print(f"Total Transportkostnad (Modell): ${total_cost_model:,.2f}")
    print(f"Kostnadsøkning:                  {cost_increase_pct:.2f}%")
    print("-" * 50)
    print(f"Total Ledetid (Base):            {total_days_base:,.0f} dager")
    print(f"Total Ledetid (Modell):          {total_days_model:,.0f} dager")
    print(f"Reduksjon i Ledetid:             {lead_time_reduction_pct:.2f}%")
    print("-" * 50)
    print(f"Efficiency Ratio:                {efficiency_ratio:.4f}")
    
    # Lagre resultater for rapporten
    results_df = pd.DataFrame({
        'Metric': ['Total Cost Base', 'Total Cost Model', 'Cost Increase %', 'Total Days Base', 'Total Days Model', 'Lead Time Reduction %', 'Efficiency Ratio'],
        'Value': [total_cost_base, total_cost_model, cost_increase_pct, total_days_base, total_days_model, lead_time_reduction_pct, efficiency_ratio]
    })
    results_df.to_csv('004 data/objective_evaluation.csv', index=False)
    print("\nEvaluering ferdig. Lagret i 004 data/objective_evaluation.csv")

if __name__ == "__main__":
    evaluate_objective_function()
