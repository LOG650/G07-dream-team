import csv

file_path = '004 data/global_supply_chain_disruption_v1.csv'

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

inconsistencies = []

for i, row in enumerate(rows):
    # Check Delay_Days vs Delivery_Status
    delay = float(row['Delay_Days'])
    status = row['Delivery_Status']
    
    if delay > 0 and status != 'Late':
        inconsistencies.append(f"Row {i+2}: Delay_Days={delay} but Delivery_Status='{status}'")
    if delay == 0 and status == 'Late':
        inconsistencies.append(f"Row {i+2}: Delay_Days=0 but Delivery_Status='Late'")
        
    # Check Disruption_Event vs Delivery_Status (Optional, but good to know)
    disruption = row['Disruption_Event']
    if disruption != 'None' and status == 'On Time':
        # This might be possible if mitigation worked, but let's see
        pass
    if disruption == 'None' and status == 'Late':
        inconsistencies.append(f"Row {i+2}: Disruption_Event='None' but Delivery_Status='Late'")

print(f"Total Inconsistencies found: {len(inconsistencies)}")
for inc in inconsistencies[:10]:
    print(inc)

# Check for hidden missing values
hidden_missing = ['?', 'N/A', 'NA', 'NULL', 'nan']
found_hidden = {}
for row in rows:
    for h, val in row.items():
        if val.strip() in hidden_missing:
            found_hidden[h] = found_hidden.get(h, 0) + 1

if found_hidden:
    print("\n--- Hidden Missing Values ---")
    for h, count in found_hidden.items():
        print(f"{h}: {count}")
else:
    print("\nNo hidden missing values found.")
