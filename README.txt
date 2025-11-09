PastureBiomass AI

Python 3.8 plus compatible
License: MIT


An advanced AI system for accurate pasture biomass estimation and intelligent grazing decision support using multi modal deep learning and computer vision.

Key Features

91 percent Accuracy: R squared equals 0.91 in biomass prediction
Multi Modal Input: Satellite plus drone plus vegetation indices
Uncertainty Quantification: Confidence intervals for all predictions
Grazing Decision Engine: Actionable recommendations with scoring from 0 to 100
Sustainability Assessment: Carbon sequestration and environmental impact
Farmer Ready Outputs: Simple, interpretable recommendations

Performance Highlights

Mean Absolute Error: 195 kilograms per hectare, 13 percent error rate
Prediction Range: 139 to 4073 kilograms per hectare
Carbon Sequestration: 689 kilograms carbon per hectare average
Grazing Score: 35.4 out of 100 average

Quick Start

from pasture biomass import BiomassPredictor

Initialize predictor
predictor equals BiomassPredictor()

Predict biomass and get recommendations
result equals predictor.predict open parenthesis
    green ratio: 0.35,
    exg: 25.0, 
    ndvi rgb: 0.45,
    edge density: 0.3,
    contrast: 45.0
close parenthesis

print f string Biomass: result biomass kilograms per hectare
print f string Recommendation: result grazing decision

Repository Structure

PastureBiomass AI
    models: Trained model files
    src: Source code
    data: Sample datasets
    results: Experimental results
    tests: Test scripts
    docs: Documentation
    notebooks: Jupyter notebooks

Citation

If you use this work in your research, please cite:

Ugwumba N.K (2025) Computer Vision for Pasture Biomass Estimation: Enabling Data-Driven Grazing Decisions through Multi-Modal Deep Learning

License

MIT License, see LICENSE file for details.
