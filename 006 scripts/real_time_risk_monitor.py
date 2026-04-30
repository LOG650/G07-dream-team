import requests
import json
import os
from datetime import datetime, timedelta

# API Konfigurasjon
NEWS_API_KEY = '36d5732c161148bba2ee23b75e77de41'
BASE_URL = 'https://newsapi.org/v2/everything'

def fetch_real_time_risk():
    print("Henter sanntidsdata fra NewsAPI...")
    
    # Definer søkeord for logistikkrisiko
    queries = {
        'Suez': 'Suez Canal disruption OR blockage OR tension',
        'Panama': 'Panama Canal drought OR transit delay',
        'Cyber': 'supply chain cyber attack OR logistics hacking',
        'Weather': 'extreme weather logistics disruption OR hurricane shipping',
        'Geopolitical': 'red sea shipping attacks OR geopolitical supply chain risk'
    }
    
    risk_scores = {}
    
    # Hent nyheter fra siste 7 dager
    from_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    
    for category, query in queries.items():
        params = {
            'q': query,
            'from': from_date,
            'sortBy': 'relevancy',
            'apiKey': NEWS_API_KEY,
            'language': 'en'
        }
        
        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()
            
            if data['status'] == 'ok':
                count = data['totalResults']
                # Beregn en enkel score basert på antall treff (logaritmisk skala)
                # 0-5 treff = Lav, 5-20 = Moderat, 20+ = Høy
                if count == 0:
                    score = 0.1
                elif count < 10:
                    score = 0.4
                elif count < 50:
                    score = 0.7
                else:
                    score = 0.95
                
                risk_scores[category] = {
                    'score': score,
                    'article_count': count,
                    'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                print(f"Kategori {category}: {count} artikler funnet. Risk Score: {score}")
            else:
                print(f"Feil ved henting av {category}: {data.get('message')}")
                risk_scores[category] = {'score': 0.0, 'error': 'API Error'}
                
        except Exception as e:
            print(f"Kunne ikke koble til NewsAPI for {category}: {e}")
            risk_scores[category] = {'score': 0.0, 'error': str(e)}

    # Lagre resultatene
    output_path = '004 data/live_risk_signals.json'
    with open(output_path, 'w') as f:
        json.dump(risk_scores, f, indent=4)
    
    print(f"\nSanntidssignaler lagret i {output_path}")

if __name__ == "__main__":
    fetch_real_time_risk()
