import csv

file_path = '004 data/global_supply_chain_disruption_v1.csv'

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

origin_cities = sorted(list(set(row['Origin_City'] for row in rows)))
destination_cities = sorted(list(set(row['Destination_City'] for row in rows)))

print(f"Origin Cities: {origin_cities}")
print(f"Destination Cities: {destination_cities}")
