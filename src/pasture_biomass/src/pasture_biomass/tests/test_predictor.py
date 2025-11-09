import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.pasture_biomass import BiomassPredictor

def test_predictor_initialization():
    """Test that predictor initializes correctly."""
    predictor = BiomassPredictor()
    assert predictor.model is not None
    assert predictor.scaler is not None
    assert predictor.metadata is not None

def test_prediction_output():
    """Test prediction output format and types."""
    predictor = BiomassPredictor()
    
    sample_features = {
        'green_ratio': 0.35,
        'exg': 25.0, 
        'ndvi_rgb': 0.45,
        'edge_density': 0.3,
        'contrast': 45.0
    }
    
    result = predictor.predict(sample_features)
    
    # Check output structure
    assert 'biomass_kg_ha' in result
    assert 'grazing_decision' in result
    assert 'grazing_score' in result
    assert 'carbon_sequestration_kg_c_ha' in result
    
    # Check value ranges
    assert 0 <= result['grazing_score'] <= 100
    assert result['biomass_kg_ha'] > 0

if __name__ == "__main__":
    pytest.main([__file__])
