import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
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

    # 1. Feature Engineering
    # Konverter kategoriske variabler til numeriske (One-Hot Encoding)
    categorical_cols = ['industry', 'disruption_type', 'supplier_region']
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    # Inkluder andre relevante numeriske kolonner
    df_encoded['has_backup_int'] = df_encoded['has_backup_supplier'].map({True: 1, False: 0})
    
    # Velg features (X) og target (y)
    # Finn alle de nye dummie-kolonnene
    feature_cols = [col for col in df_encoded.columns if any(cat in col for cat in categorical_cols)]
    feature_cols += ['disruption_severity', 'production_impact_pct', 'has_backup_int', 'revenue_loss_usd']
    
    X = df_encoded[feature_cols]
    y = df_encoded['full_recovery_days']

    # Splitting i trening og test (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 2. Tren modellen (Random Forest for bedre håndtering av ikke-lineære data)
    print(f"Trener RandomForestRegressor med {X.shape[1]} features...")
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    # 3. Evaluering
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Modell 2.2.3 ferdig trent (Random Forest).")
    print(f"Mean Absolute Error: {mae:.2f} dager")
    print(f"R2 Score: {r2:.4f}")

    # Lagre modellen
    joblib.dump(model, '006 scripts/recovery_predictor.pkl')
    # Lagre kolonnenavnene som ble brukt i modellen (viktig for senere bruk)
    joblib.dump(feature_cols, '006 scripts/model_features.pkl')
    print("Modell og features lagret.")

    # Legg til prediksjoner i datasettet for videre analyse
    df['predicted_recovery_days'] = model.predict(X_encoded := df_encoded[feature_cols])
    df.to_csv('004 data/recovery_with_predictions.csv', index=False)

if __name__ == "__main__":
    train_recovery_model()
