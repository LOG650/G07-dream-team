import csv

input_file = '004 data/global_supply_chain_disruption_v1.csv'
output_file = '004 data/global_supply_chain_disruption_v1_cleaned.csv'

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    # Logic: If it's Late but says 'None' disruption, change it to 'Unspecified'
    if row['Delivery_Status'] == 'Late' and row['Disruption_Event'] == 'None':
        row['Disruption_Event'] = 'Unspecified/Other'

headers = list(rows[0].keys())

with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)

print(f"Cleaned data saved to {output_file}")
