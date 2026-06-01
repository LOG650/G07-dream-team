import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib

# Sett stil
sns.set_theme(style="whitegrid")

def create_visualizations():
    # Opprett mappe for figurer hvis den ikke eksisterer
    output_dir = '005 report/figures'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 1. Visualisering av Stresstest (Base vs Suez Stress)
    # ... (eksisterende kode)

    # 4. Feature Importance (Hva påvirker modellen mest?)
    try:
        # Last inn modellen og feature-listen
        model = joblib.load('006 scripts/recovery_predictor.pkl')
        features = joblib.load('006 scripts/model_features.pkl')
        
        # Hent importances
        importances = model.feature_importances_
        feature_imp_df = pd.DataFrame({'Feature': features, 'Importance': importances})
        feature_imp_df = feature_imp_df.sort_values(by='Importance', ascending=False).head(10)

        plt.figure(figsize=(10, 6))
        sns.barplot(data=feature_imp_df, x='Importance', y='Feature', palette='viridis')
        plt.title('Topp 10 Faktorer for Prediksjon av Restitusjonstid (Feature Importance)')
        plt.xlabel('Relativ Viktighet (0-1)')
        plt.ylabel('Variabel')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/feature_importance.png')
        plt.close()
        print("Lagret feature_importance.png")
    except Exception as e:
        print(f"Kunne ikke lage feature importance-graf: {e}")
    try:
        stress_df = pd.read_csv('004 data/stress_test_summary.csv')
        # Smelt dataen for plotting
        df_plot = stress_df.melt(id_vars='Strategy', value_vars=['Base', 'Suez_Stress'], 
                                  var_name='Scenario', value_name='Andel %')
        
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df_plot, x='Andel %', y='Strategy', hue='Scenario')
        plt.title('Beslutningsstrategier: Normal vs. Suez-blokkering (Stresstest)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/stress_test_comparison.png')
        plt.close()
        print("Lagret stress_test_comparison.png")
    except Exception as e:
        print(f"Kunne ikke lage stresstest-graf: {e}")

    # 2. Kostnad vs. Ledetid (Målfunksjon)
    try:
        obj_df = pd.read_csv('004 data/objective_evaluation.csv')
        # Hent verdier manuelt for en enkel sammenligning
        costs = [obj_df.loc[obj_df['Metric'] == 'Average Cost Base', 'Value'].values[0],
                 obj_df.loc[obj_df['Metric'] == 'Average Cost Model', 'Value'].values[0]]
        days = [obj_df.loc[obj_df['Metric'] == 'Average Days Base', 'Value'].values[0],
                obj_df.loc[obj_df['Metric'] == 'Average Days Model', 'Value'].values[0]]
        
        fig, ax1 = plt.subplots(figsize=(10, 6))

        color = 'tab:red'
        ax1.set_xlabel('Scenario')
        ax1.set_ylabel('Gj.snitt Kostnad (USD)', color=color)
        ax1.bar(['Base', 'Modell'], costs, color=color, alpha=0.3, label='Kostnad')
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()
        color = 'tab:blue'
        ax2.set_ylabel('Gj.snitt Ledetid (Dager)', color=color)
        ax2.plot(['Base', 'Modell'], days, color=color, marker='o', linewidth=3, label='Ledetid')
        ax2.tick_params(axis='y', labelcolor=color)

        plt.title('Trade-off: Økt Kostnad vs. Redusert Ledetid (Per Forsendelse)')
        fig.tight_layout()
        plt.savefig(f'{output_dir}/cost_leadtime_tradeoff.png')
        plt.close()
        print("Lagret cost_leadtime_tradeoff.png")
    except Exception as e:
        print(f"Kunne ikke lage trade-off-graf: {e}")

    # 3. Restitusjonstid per disrupsjonstype (Viser tydeligere trender enn industri)
    try:
        rec_df = pd.read_csv('004 data/supply_chain_disruption_recovery.csv')
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=rec_df, x='disruption_type', y='full_recovery_days', palette="Set2")
        plt.xticks(rotation=45)
        plt.title('Fordeling av Restitusjonstid per Disrupsjonstype')
        plt.xlabel('Disrupsjonstype')
        plt.ylabel('Dager til full restitusjon')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/recovery_by_disruption.png')
        plt.close()
        print("Lagret recovery_by_disruption.png")
    except Exception as e:
        print(f"Kunne ikke lage disrupsjon-graf: {e}")

if __name__ == "__main__":
    create_visualizations()
