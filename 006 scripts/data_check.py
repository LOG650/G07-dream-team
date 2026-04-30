import pandas as pd

file_path = '004 data/global_supply_chain_disruption_v1.csv'
df = pd.read_csv(file_path)

print(f"--- Data Quality Report for {file_path} ---")
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicates ---")
print(f"Duplicate rows: {df.duplicated().sum()}")
print(f"Duplicate Order_IDs: {df['Order_ID'].duplicated().sum()}")

print("\n--- Summary Statistics for Numeric Columns ---")
print(df.describe())

print("\n--- Unique Values in Categorical Columns ---")
categorical_cols = ['Route_Type', 'Transportation_Mode', 'Product_Category', 'Delivery_Status', 'Disruption_Event', 'Mitigation_Action_Taken']
for col in categorical_cols:
    print(f"{col}: {df[col].unique()}")

print("\n--- Date Range ---")
print(f"Min Order_Date: {df['Order_Date'].min()}")
print(f"Max Order_Date: {df['Order_Date'].max()}")
