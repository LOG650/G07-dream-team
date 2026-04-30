import pandas as pd
import os

# Note: We are using pandas here as it is the standard for feature engineering.
# If pandas is missing, I will revert to csv module, but let's try the efficient way first.

def run_feature_engineering():
    try:
        # Load cleaned data
        disruption_df = pd.read_csv('004 data/global_supply_chain_disruption_v1_cleaned.csv')
        recovery_df = pd.read_csv('004 data/supply_chain_disruption_recovery.csv')

        print("Datasets loaded successfully.")

        # 1. Feature Engineering: Disruption Data
        # Calculate Delay Ratio
        disruption_df['delay_ratio'] = disruption_df['Delay_Days'] / disruption_df['Scheduled_Lead_Time_Days']
        
        # Combined Risk Index
        disruption_df['total_risk_index'] = (disruption_df['Geopolitical_Risk_Index'] * 0.6) + (disruption_df['Weather_Severity_Index'] * 0.04)

        # 2. Feature Engineering: Recovery Data
        # Recovery Efficiency
        recovery_df['recovery_speed'] = recovery_df['full_recovery_days'] / recovery_df['disruption_severity']

        # 3. Sammenslåing (Merging)
        # Since there is no direct ID, we map Product_Category to Industry for a statistical merge
        category_map = {
            'Electronics': ['Semiconductors', 'Consumer Electronics'],
            'Automotive': ['Auto Parts'],
            'Pharmaceuticals': ['Pharmaceuticals'],
            'Consumer Goods': ['Textiles', 'Perishable Foods'],
            'Aerospace': ['Raw Materials'] # Assumption for this model
        }
        
        # For a simplified model merge, we can't do a 1:1 join without a key, 
        # but we can create a representative master set or aggregate stats.
        # Here we will export them as a prepared folder for the model to use both.
        
        print("Feature engineering completed.")
        
        # Save enriched datasets
        disruption_df.to_csv('004 data/enriched_disruption_data.csv', index=False)
        recovery_df.to_csv('004 data/enriched_recovery_data.csv', index=False)
        
        print("Saved enriched files to 004 data/")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_feature_engineering()
