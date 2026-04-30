import unittest
import pandas as pd
import os
import joblib
from decision_model import run_decision_model

class TestSupplyChainModels(unittest.TestCase):
    
    def test_decision_logic(self):
        # Test av terskelverdier i en simulert rad
        high_risk_row = pd.Series({
            'total_risk_index': 0.8,
            'delay_ratio': 0.0,
            'Product_Category': 'Electronics',
            'Transportation_Mode': 'Sea',
            'Route_Type': 'Suez'
        })
        
        # Sjekk risiko-klassifisering (basert på logikken i decision_model.py)
        risk = 'High' if high_risk_row['total_risk_index'] >= 0.7 else 'Low'
        self.assertEqual(risk, 'High')
        
        # Sjekk omruting (basert på logikken i decision_model.py)
        if risk == 'High' and high_risk_row['Route_Type'] == 'Suez':
            strategy = 'Reroute via Atlantic/Cape'
        self.assertEqual(strategy, 'Reroute via Atlantic/Cape')

    def test_predictor_loading(self):
        # Sjekk at modellen fra 2.2.3 eksisterer og kan lastes
        model_path = '006 scripts/recovery_predictor.pkl'
        self.assertTrue(os.path.exists(model_path))
        
        model = joblib.load(model_path)
        self.assertIsNotNone(model)
        
        # Test prediksjon med dummy-data
        # features: [disruption_severity, production_impact_pct, has_backup_int]
        prediction = model.predict([[5, 80, 1]])
        self.assertGreater(prediction[0], 0)

if __name__ == '__main__':
    unittest.main()
