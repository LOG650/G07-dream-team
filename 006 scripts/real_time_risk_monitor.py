import requests
import json
import os
from datetime import datetime, timedelta

# API Konfigurasjon
NEWS_API_KEY = '36d5732c161148bba2ee23b75e77de41'
WEATHER_API_KEY = 'b81033523740bd2bc26ccd7a0b1bb6b9'
NEWS_BASE_URL = 'https://newsapi.org/v2/everything'
WEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_risk():
    print("Henter værdata fra OpenWeatherMap...")
    # Kritiske logistikknoder (Byer/Havner)
    nodes = {
        'Suez': {'lat': 29.9667, 'lon': 32.55},
        'Panama': {'lat': 8.9833, 'lon': -79.5167},
        'Shanghai': {'lat': 31.2304, 'lon': 121.4737},
        'Rotterdam': {'lat': 51.9225, 'lon': 4.47917},
        'Singapore': {'lat': 1.3521, 'lon': 103.8198}
    }
    
    node_risks = {}
    for name, coords in nodes.items():
        params = {
            'lat': coords['lat'],
            'lon': coords['lon'],
            'appid': WEATHER_API_KEY,
            'units': 'metric'
        }
        try:
            response = requests.get(WEATHER_BASE_URL, params=params)
            data = response.json()
            if response.status_code == 200:
                wind_speed = data.get('wind', {}).get('speed', 0)
                weather_main = data.get('weather', [{}])[0].get('main', '')
                
                # Enkel risikoscore: Vind over 15 m/s eller 'Extreme' værtyper
                score = 0.1
                if wind_speed > 20 or weather_main in ['Thunderstorm', 'Tornado', 'Squall']:
                    score = 0.9
                elif wind_speed > 12 or weather_main in ['Rain', 'Snow']:
                    score = 0.5
                
                node_risks[name] = score
                print(f"Vær i {name}: {weather_main}, Vind: {wind_speed} m/s. Risk Score: {score}")
        except Exception as e:
            print(f"Feil ved henting av vær for {name}: {e}")
    
    # Returner gjennomsnittlig værrisiko hvis data finnes
    return sum(node_risks.values()) / len(node_risks) if node_risks else 0.1

def fetch_real_time_risk():
    print("Henter sanntidsdata...")
    
    # 1. Hent Værrisiko
    avg_weather_risk = get_weather_risk()
    
    # 2. Hent Nyhetsrisiko
    queries = {
        'Suez': 'Suez Canal disruption OR blockage OR tension',
        'Panama': 'Panama Canal drought OR transit delay',
        'Cyber': 'supply chain cyber attack OR logistics hacking',
        'Geopolitical': 'red sea shipping attacks OR geopolitical supply chain risk'
    }
    
    risk_scores = {}
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
            response = requests.get(NEWS_BASE_URL, params=params)
            data = response.json()
            
            if data['status'] == 'ok':
                count = data['totalResults']
                if count == 0: score = 0.1
                elif count < 10: score = 0.4
                elif count < 50: score = 0.7
                else: score = 0.95
                
                risk_scores[category] = {
                    'score': score,
                    'article_count': count,
                    'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                print(f"Kategori {category}: {count} artikler funnet. Risk Score: {score}")
        except Exception as e:
            print(f"Feil ved henting av {category}: {e}")

    # Legg til værrisikoen som en egen kategori
    risk_scores['Weather'] = {
        'score': avg_weather_risk,
        'info': 'Gjennomsnittlig værrisiko i kritiske havner',
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Lagre resultatene
    output_path = '004 data/live_risk_signals.json'
    with open(output_path, 'w') as f:
        json.dump(risk_scores, f, indent=4)
    
    print(f"\nSanntidssignaler (Nyheter + Vær) lagret i {output_path}")

if __name__ == "__main__":
    fetch_real_time_risk()
