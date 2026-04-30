import pandas as pd
import os

# Stier
input_file = '004 data/supply_chain_disruption_recovery.csv'
train_output = '004 data/train_data.csv'
test_output = '004 data/test_data.csv'

def split_dataset(file_path, train_size=0.8, seed=42):
    print(f"Laster inn data fra {file_path}...")
    df = pd.read_csv(file_path)
    
    print(f"Splitter data (trening: {train_size*100}%, test: {(1-train_size)*100}%)...")
    
    try:
        from sklearn.model_selection import train_test_split
        train_df, test_df = train_test_split(df, train_size=train_size, random_state=seed)
    except ImportError:
        print("sklearn ikke funnet, bruker pandas-basert split.")
        train_df = df.sample(frac=train_size, random_state=seed)
        test_df = df.drop(train_df.index)
    
    print(f"Lagrer treningssett til {train_output}...")
    train_df.to_csv(train_output, index=False)
    
    print(f"Lagrer testsett til {test_output}...")
    test_df.to_csv(test_output, index=False)
    
    print("\nOppsummering:")
    print(f"Totalt antall rader: {len(df)}")
    print(f"Rader i treningssett: {len(train_df)}")
    print(f"Rader i testsett: {len(test_df)}")

if __name__ == "__main__":
    if os.path.exists(input_file):
        split_dataset(input_file)
    else:
        print(f"Feil: Fant ikke filen {input_file}")
