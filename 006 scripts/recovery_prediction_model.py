import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

def train_recovery_model():
    # Last inn berikede data
    file_path = '004 data/enriched_recovery_data.csv'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} ikke funnet.")
        return

    df = pd.read_csv(file_path)

    # Forbered features (X) og target (y)
    # Vi bruker alvorlighetsgrad, produksjonspåvirkning og om vi har backup
    df['has_backup_int'] = df['has_backup_supplier'].map({True: 1, False: 0})
    
    X = df[['disruption_severity', 'production_impact_pct', 'has_backup_int']]
    y = df['full_recovery_days']

    # Splitting i trening og test (ref. metodikk i rapporten)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Tren modellen (Enkel Lineær Regresjon for denne fasen)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluering
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Modell 2.2.3 ferdig trent.")
    print(f"Mean Absolute Error: {mae:.2f} dager")
    print(f"R2 Score: {r2:.4f}")

    # Lagre modellen
    joblib.dump(model, '006 scripts/recovery_predictor.pkl')
    print("Modell lagret som recovery_predictor.pkl")

    # Legg til prediksjoner i datasettet for videre analyse
    df['predicted_recovery_days'] = model.predict(X)
    df.to_csv('004 data/recovery_with_predictions.csv', index=False)

if __name__ == "__main__":
    train_recovery_model()
