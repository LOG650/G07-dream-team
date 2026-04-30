import requests
import json
import os
import asyncio
import websockets
import yfinance as yf
from datetime import datetime, timedelta

# API Konfigurasjon
NEWS_API_KEY = '36d5732c161148bba2ee23b75e77de41'
WEATHER_API_KEY = 'b81033523740bd2bc26ccd7a0b1bb6b9'
ALPHA_VANTAGE_KEY = '4J70OEYH207V5RXF'
AIS_STREAM_KEY = '7726a793f005b07d1916936fd6622ef885d7a1f0'

NEWS_BASE_URL = 'https://newsapi.org/v2/everything'
WEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

async def get_ais_risk():
    """Sjekker skipstrafikk i Hormuzstredet via AISStream."""
    print("Sjekker maritime bevegelser i Hormuzstredet...")
    # Bounding box for Hormuzstredet
    # Format: [[lat, lon], [lat, lon]]
    hormuz_box = [[26.0, 55.5], [27.0, 57.0]]
    
    ship_count = 0
    try:
        async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
            subscribe_msg = {
                "APIKey": AIS_STREAM_KEY,
                "BoundingBoxes": [hormuz_box],
                "FiltersShipMMSI": [],
                "FilterMessageTypes": ["PositionReport"]
            }
            await websocket.send(json.dumps(subscribe_msg))
            
            # Vi venter i 5 sekunder for å telle skip i området
            start_time = datetime.now()
            while (datetime.now() - start_time).seconds < 5:
                try:
                    message = await asyncio.wait_for(websocket.recv(), timeout=1.0)
                    ship_count += 1
                except asyncio.TimeoutError:
                    continue
    except Exception as e:
        print(f"Feil ved AIS-henting: {e}")
        return 0.5 # Default risk hvis API feiler

    # Tolkning: Få skip i et så trafikkert område kan indikere blokade/stans
    # Normalt er det mange skip her. Hvis < 2 skip på 5 sekunder, øk risiko.
    if ship_count < 2:
        risk = 0.8
    elif ship_count < 5:
        risk = 0.4
    else:
        risk = 0.1
        
    print(f"Hormuz AIS-sjekk: Fant {ship_count} skip. Risk Score: {risk}")
    return risk

def get_oil_price_risk():
    """Henter Brent Crude pris og beregner risiko."""
    print("Henter Brent Crude oljepris...")
    try:
        # Bruker yfinance for raskere oppslag (AlphaVantage har 25/day limit)
        brent = yf.Ticker("BZ=F")
        price = brent.fast_info['lastPrice']
        
        # Terskelverdier for logistikkostnad
        if price > 100: risk = 0.95
        elif price > 90: risk = 0.75
        elif price > 80: risk = 0.4
        else: risk = 0.2
        
        print(f"Brent Crude: ${price:.2f}/fat. Risk Score: {risk}")
        return risk, price
    except Exception as e:
        print(f"Feil ved henting av oljepris: {e}")
        return 0.3, 80.0

def get_weather_risk():
    print("Henter værdata fra OpenWeatherMap...")
    nodes = {
        'Suez': {'lat': 29.9667, 'lon': 32.55},
        'Panama': {'lat': 8.9833, 'lon': -79.5167},
        'Shanghai': {'lat': 31.2304, 'lon': 121.4737},
        'Rotterdam': {'lat': 51.9225, 'lon': 4.47917},
        'Singapore': {'lat': 1.3521, 'lon': 103.8198}
    }
    
    node_risks = {}
    for name, coords in nodes.items():
        params = {'lat': coords['lat'], 'lon': coords['lon'], 'appid': WEATHER_API_KEY, 'units': 'metric'}
        try:
            response = requests.get(WEATHER_BASE_URL, params=params)
            data = response.json()
            if response.status_code == 200:
                wind_speed = data.get('wind', {}).get('speed', 0)
                weather_main = data.get('weather', [{}])[0].get('main', '')
                score = 0.1
                if wind_speed > 20 or weather_main in ['Thunderstorm', 'Tornado', 'Squall']: score = 0.9
                elif wind_speed > 12 or weather_main in ['Rain', 'Snow']: score = 0.5
                node_risks[name] = score
        except: pass
    return sum(node_risks.values()) / len(node_risks) if node_risks else 0.1

async def fetch_real_time_risk():
    print("Starter omfattende sanntidsovervåking (Hormuz, Olje, Vær, Nyheter)...")
    
    # 1. Olje og AIS (Hormuz)
    oil_risk, oil_price = get_oil_price_risk()
    ais_risk = await get_ais_risk()
    
    # 2. Vær
    avg_weather_risk = get_weather_risk()
    
    # 3. Nyheter
    queries = {
        'Suez': 'Suez Canal disruption OR blockage',
        'Hormuz': 'Strait of Hormuz tension OR tanker attack',
        'Cyber': 'supply chain cyber attack',
        'Geopolitical': 'red sea shipping attacks'
    }
    
    risk_scores = {}
    from_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    
    for category, query in queries.items():
        params = {'q': query, 'from': from_date, 'sortBy': 'relevancy', 'apiKey': NEWS_API_KEY, 'language': 'en'}
        try:
            response = requests.get(NEWS_BASE_URL, params=params)
            data = response.json()
            if data['status'] == 'ok':
                count = data['totalResults']
                if count == 0: score = 0.1
                elif count < 10: score = 0.4
                elif count < 50: score = 0.7
                else: score = 0.95
                risk_scores[category] = {'score': score, 'article_count': count}
        except: pass

    # Samle alt
    risk_scores['Oil_Price'] = {'score': oil_risk, 'price': oil_price}
    risk_scores['Hormuz_AIS'] = {'score': ais_risk}
    risk_scores['Weather'] = {'score': avg_weather_risk}
    
    # Lagre
    output_path = '004 data/live_risk_signals.json'
    with open(output_path, 'w') as f:
        json.dump(risk_scores, f, indent=4)
    
    print(f"\nOppdaterte sanntidssignaler lagret i {output_path}")

if __name__ == "__main__":
    asyncio.run(fetch_real_time_risk())
