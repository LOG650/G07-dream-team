import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Sett stil
sns.set_theme(style="whitegrid")

def create_visualizations():
    # Opprett mappe for figurer hvis den ikke eksisterer
    output_dir = '005 report/figures'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 1. Visualisering av Stresstest (Base vs Suez Stress)
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
        costs = [obj_df.loc[obj_df['Metric'] == 'Total Cost Base', 'Value'].values[0],
                 obj_df.loc[obj_df['Metric'] == 'Total Cost Model', 'Value'].values[0]]
        days = [obj_df.loc[obj_df['Metric'] == 'Total Days Base', 'Value'].values[0],
                obj_df.loc[obj_df['Metric'] == 'Total Days Model', 'Value'].values[0]]
        
        fig, ax1 = plt.subplots(figsize=(10, 6))

        color = 'tab:red'
        ax1.set_xlabel('Scenario')
        ax1.set_ylabel('Total Kostnad (USD)', color=color)
        ax1.bar(['Base', 'Modell'], costs, color=color, alpha=0.3, label='Kostnad')
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()
        color = 'tab:blue'
        ax2.set_ylabel('Total Ledetid (Dager)', color=color)
        ax2.plot(['Base', 'Modell'], days, color=color, marker='o', linewidth=3, label='Ledetid')
        ax2.tick_params(axis='y', labelcolor=color)

        plt.title('Trade-off: Økt Kostnad vs. Redusert Ledetid')
        fig.tight_layout()
        plt.savefig(f'{output_dir}/cost_leadtime_tradeoff.png')
        plt.close()
        print("Lagret cost_leadtime_tradeoff.png")
    except Exception as e:
        print(f"Kunne ikke lage trade-off-graf: {e}")

    # 3. Restitusjonstid per bransje (fra de originale dataene)
    try:
        rec_df = pd.read_csv('004 data/supply_chain_disruption_recovery.csv')
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=rec_df, x='industry', y='full_recovery_days')
        plt.xticks(rotation=45)
        plt.title('Fordeling av Restitusjonstid per Industri')
        plt.ylabel('Dager til full restitusjon')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/recovery_by_industry.png')
        plt.close()
        print("Lagret recovery_by_industry.png")
    except Exception as e:
        print(f"Kunne ikke lage bransje-graf: {e}")

if __name__ == "__main__":
    create_visualizations()
