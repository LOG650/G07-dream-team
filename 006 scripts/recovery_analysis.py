import csv
from collections import Counter, defaultdict
import os

file_path = '004 data/supply_chain_disruption_recovery.csv'
output_dir = '005 report'
output_path = os.path.join(output_dir, 'Recovery_Analysis_Report.md')

def mean(data):
    return sum(data) / len(data) if data else 0

def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0: return 0
    if n % 2 == 1:
        return sorted_data[n//2]
    else:
        return (sorted_data[n//2-1] + sorted_data[n//2]) / 2

# Ensure report directory exists (it should, but safety first)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Analysis Containers
recovery_by_type = defaultdict(list)
recovery_by_backup = defaultdict(list)
loss_by_industry = defaultdict(list)
impact_by_severity = defaultdict(list)

for row in rows:
    dtype = row['disruption_type']
    full_rec = float(row['full_recovery_days'])
    has_backup = row['has_backup_supplier']
    industry = row['industry']
    loss = float(row['revenue_loss_usd'])
    severity = row['disruption_severity']
    impact = float(row['production_impact_pct'])

    recovery_by_type[dtype].append(full_rec)
    recovery_by_backup[has_backup].append(full_rec)
    loss_by_industry[industry].append(loss)
    impact_by_severity[severity].append(impact)

report_lines = []
report_lines.append("# Statistisk Analyse: Supply Chain Disruption Recovery\n")
report_lines.append(f"**Dato:** 2026-04-12")
report_lines.append(f"**Totalt antall observasjoner:** {len(rows)}\n")

report_lines.append("## 1. Restitusjonstid etter Disrupsjonstype (Dager)")
report_lines.append("| Disrupsjonstype | Gjennomsnittlig Restitusjon | Median | Max | Min |")
report_lines.append("| :--- | :--- | :--- | :--- | :--- |")
for dtype in sorted(recovery_by_type.keys()):
    data = recovery_by_type[dtype]
    report_lines.append(f"| {dtype} | {mean(data):.2f} | {median(data)} | {max(data)} | {min(data)} |")

report_lines.append("\n## 2. Effekt av Backup-leverandører")
report_lines.append("| Har Backup-leverandør | Gjennomsnittlig Full Restitusjon (Dager) | Antall |")
report_lines.append("| :--- | :--- | :--- |")
for val in sorted(recovery_by_backup.keys()):
    data = recovery_by_backup[val]
    report_lines.append(f"| {val} | {mean(data):.2f} | {len(data)} |")

report_lines.append("\n## 3. Omsetningstap per Industri (USD)")
report_lines.append("| Industri | Totalt Tap | Gjennomsnittlig Tap |")
report_lines.append("| :--- | :--- | :--- |")
for ind in sorted(loss_by_industry.keys()):
    data = loss_by_industry[ind]
    report_lines.append(f"| {ind} | ${sum(data):,.2f} | ${mean(data):,.2f} |")

report_lines.append("\n## 4. Alvorlighetsgrad vs. Produksjonspåvirkning")
report_lines.append("| Alvorlighetsgrad | Gjennomsnittlig Produksjonstap (%) |")
report_lines.append("| :--- | :--- |")
for sev in sorted(impact_by_severity.keys()):
    data = impact_by_severity[sev]
    report_lines.append(f"| {sev} | {mean(data):.2f}% |")

with open(output_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(report_lines))

print(f"Analyse ferdig. Rapport lagret i {output_path}")
