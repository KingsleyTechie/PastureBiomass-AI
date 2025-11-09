import torch
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from .models import RobustBiomassPredictor
from .decision_engine import GrazingDecisionEngine, SustainabilityMetrics

class BiomassPredictor:
    """Main class for pasture biomass prediction and decision support."""
    
    def __init__(self, model_dir="models"):
        self.model_dir = Path(model_dir)
        self.model = None
        self.scaler = None
        self.metadata = None
        self.grazing_engine = GrazingDecisionEngine()
        self.sustainability = SustainabilityMetrics()
        self._load_model()
    
    def _load_model(self):
        """Load trained model and components."""
        try:
            self.metadata = joblib.load(self.model_dir / "model_metadata.pkl")
            self.scaler = joblib.load(self.model_dir / "feature_scaler.pkl")
            
            self.model = RobustBiomassPredictor(
                input_dim=self.metadata['input_dim'],
                hidden_dim=self.metadata['hidden_dim']
            )
            self.model.load_state_dict(
                torch.load(self.model_dir / "biomass_model_weights.pth")
            )
            self.model.eval()
            
        except Exception as e:
            raise RuntimeError(f"Failed to load model: {e}")
    
    def predict(self, features):
        """Predict biomass and provide grazing recommendations."""
        # Convert features to array
        feature_array = np.array([[features[feature] 
                                 for feature in self.metadata['feature_names']]])
        
        # Scale features
        features_scaled = self.scaler.transform(feature_array)
        
        # Predict biomass
        with torch.no_grad():
            biomass = self.model(torch.FloatTensor(features_scaled)).item()
        
        # Get recommendations
        grazing_decision, grazing_score, notes = self.grazing_engine.get_grazing_recommendation(biomass)
        carbon_seq = self.sustainability.estimate_carbon_sequestration(biomass)
        sustainability_score = self.sustainability.calculate_sustainability_score(biomass)
        
        return {
            'biomass_kg_ha': biomass,
            'grazing_decision': grazing_decision,
            'grazing_score': grazing_score,
            'grazing_notes': notes,
            'carbon_sequestration_kg_c_ha': carbon_seq,
            'sustainability_score': sustainability_score,
            'confidence_interval': [max(0, biomass - 200), biomass + 200]
        }
