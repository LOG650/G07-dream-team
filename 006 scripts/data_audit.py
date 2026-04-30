import csv
import sys
from collections import Counter

def is_numeric(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def audit_file(file_path):
    print(f"\n{'='*20}")
    print(f"Audit for {file_path}")
    print(f"{'='*20}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return

    total_rows = len(rows)
    if total_rows == 0:
        print("Empty file")
        return

    headers = list(rows[0].keys())
    print(f"Total rows: {total_rows}")
    print(f"Columns: {headers}")

    stats = {h: {'missing': 0, 'unique': set(), 'numeric_count': 0, 'min': float('inf'), 'max': float('-inf')} for h in headers}

    for row in rows:
        for h in headers:
            val = row[h]
            if not val or val.strip().lower() in ['null', 'nan', '', 'none']:
                stats[h]['missing'] += 1
            else:
                stats[h]['unique'].add(val)
                if is_numeric(val):
                    v = float(val)
                    stats[h]['numeric_count'] += 1
                    stats[h]['min'] = min(stats[h]['min'], v)
                    stats[h]['max'] = max(stats[h]['max'], v)

    print("\n--- Summary ---")
    for h in headers:
        missing = stats[h]['missing']
        unique_count = len(stats[h]['unique'])
        print(f"{h}:")
        print(f"  Missing: {missing} ({missing/total_rows*100:.2f}%)")
        print(f"  Unique: {unique_count}")
        if stats[h]['numeric_count'] > 0:
            print(f"  Range: {stats[h]['min']} to {stats[h]['max']}")

    print("\n--- Categorical Analysis (Small Sets) ---")
    for h in headers:
        if len(stats[h]['unique']) < 15:
            counts = Counter(row[h] for row in rows)
            print(f"{h}: {dict(counts)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        audit_file(sys.argv[1])
    else:
        print("Usage: python scripts/data_audit.py <file_path>")
