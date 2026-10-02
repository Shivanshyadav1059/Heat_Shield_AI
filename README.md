# HeatShieldAI-Urban-Heat-Mitigation
Optimizing Urban Heat Mitigation and cooling strategies via Artificial Intelligence and Machine Learning

---

## 📌 Overview

HeatShield AI is an AI-powered decision support system designed to identify Urban Heat Island (UHI) hotspots using satellite-derived data and provide intelligent cooling recommendations.

The system combines Google Earth Engine, Landsat-8 imagery, NDVI analysis, Land Surface Temperature (LST), and a Random Forest Machine Learning model to estimate urban heat risk and recommend mitigation strategies.

Developed for **BAH 2026 Hackathon**.

---

## 🌍 Problem Statement

Rapid urbanization replaces natural vegetation with concrete infrastructure, causing Urban Heat Islands (UHIs). Increased surface temperatures negatively affect:

- Public Health
- Energy Consumption
- Urban Sustainability
- Climate Resilience

Current heat maps mainly visualize hotspots but provide limited decision support.

HeatShield AI bridges this gap by integrating AI-driven heat risk prediction with actionable mitigation recommendations.

---

# ✨ Features

- 🌍 Satellite-based Urban Heat Mapping
- 🔥 Urban Heat Hotspot Detection
- 🌳 NDVI Vegetation Analysis
- 🤖 AI Heat Risk Prediction
- 🎯 Interactive Scenario Simulation
- 📊 Explainable AI Dashboard
- 🌿 Intelligent Cooling Recommendations
- 📈 Analytics Dashboard
- 🛰️ Google Earth Engine Integration
- 🎨 Modern Space-themed UI

---

# 🏗 System Architecture

```
Satellite Data
        │
        ▼
Google Earth Engine
        │
        ▼
LST + NDVI Extraction
        │
        ▼
Dataset Generation
        │
        ▼
Random Forest Model
        │
        ▼
Heat Risk Prediction
        │
        ▼
Recommendation Engine
        │
        ▼
Interactive Streamlit Dashboard
```

---

# 🛰 Data Sources

- Landsat-8 Satellite Imagery
- Google Earth Engine
- NDVI Raster
- Land Surface Temperature (LST)
- Generated Heat Risk Dataset

---

# 🤖 AI Model

Machine Learning Algorithm:

- Random Forest Regressor

Input Features

- Average NDVI
- Maximum Temperature

Output

- Heat Risk Score (0–100)

The dashboard also supports scenario-based prediction where users can change environmental parameters to observe how heat risk changes.

---

# 🌿 Recommendation Engine

Recommendations are dynamically generated based on predicted heat risk.

Examples include:

- Urban Greening
- Cool Roofs
- Blue-Green Infrastructure
- Reflective Pavements
- Water Body Restoration
- Urban Tree Plantation

---

# 📊 Dashboard

The Streamlit dashboard includes:

- Heat Map
- Hotspot Detection
- NDVI Analysis
- Interactive AI Prediction
- Scenario Simulation
- Feature Importance
- Dataset Analytics

---

# 🛠 Technology Stack

### Programming

- Python

### Machine Learning

- Scikit-Learn
- Random Forest

### Data Processing

- NumPy
- Pandas

### Visualization

- Plotly
- Streamlit

### Geospatial

- Google Earth Engine
- Landsat-8

---


```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/mrssingh537-lab/HeatShieldAI.git
```

Move inside project

```bash
cd HeatShieldAI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

# 📈 Future Improvements

- Multi-city Support
- Real-time Satellite Updates
- Weather API Integration
- Deep Learning Models
- Time-series Heat Forecasting
- Mobile-friendly Dashboard
- Cloud Deployment

---

# 🎯 Hackathon

Developed for

**BAH 2026**
Optimizing Urban Heat Mitigation and Cooling Strategies using Artificial Intelligence and Machine Learning (AIML)

---

# 👨‍💻 Author

Shivansh Yadav

B.Tech Computer Science Engineering

AI / Machine Learning Enthusiast

---

# 📜 License

This project is released under the MIT License.
