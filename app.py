

from utils.scenario import apply_scenario

import plotly.graph_objects as go
import plotly.express as px

import streamlit as st
import pandas as pd

from utils.data_loader import (
    average_ndvi,
    average_temperature,
    max_temperature
)

from utils.prediction import predict_risk
from utils.recommendation import get_recommendation

from utils.config import (
    HEAT_MAP,
    HOTSPOT_MAP,
    NDVI_MAP,
    DATASET_FILE
)

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="HeatShield AI",
    page_icon="🔥",
    layout="wide"
)

#load css
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


# ---------------------------------------
# Load Dataset
# ---------------------------------------

df = pd.read_csv(DATASET_FILE)

training_samples = len(df)

# ---------------------------------------
# Read Statistics
# ---------------------------------------

avg_ndvi = average_ndvi()
avg_temp = average_temperature()
max_temp = max_temperature()

risk_score = predict_risk(avg_ndvi, max_temp)

# recommendation = get_recommendation(risk_score)

# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.image(
    "assets/logo.png",
    width=180
)

st.sidebar.markdown("# 🔥 HeatShield AI")
st.sidebar.caption("Urban Heat Intelligence Platform")


st.sidebar.markdown("---")

city = st.sidebar.selectbox(
    "Select City",
    ["Lucknow"]
)

strategy = st.sidebar.selectbox(
    "Preferred Cooling Strategy",
    [
        "Auto (AI Recommendation)",
        "Urban Greening",
        "Cool Roofs",
        "Blue-Green Infrastructure"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🛠 Scenario Simulator")

tree_cover = st.sidebar.slider(
    "Increase Tree Cover (%)",
    0,
    100,
    20
)

cool_roofs = st.sidebar.slider(
    "Cool Roof Coverage (%)",
    0,
    100,
    20
)

water_restoration = st.sidebar.slider(
    "Water Body Restoration (%)",
    0,
    100,
    20
)



st.sidebar.markdown("---")

st.sidebar.info(
"""
BAH 2026

Urban Heat Mitigation using
Satellite Data + AI
"""
)

# ---------------------------------------
# Header
# ---------------------------------------


st.markdown("""
# 🔥 HeatShield AI

### AI-powered Urban Heat Detection & Decision Support System

Built using **Google Earth Engine + Landsat-8 + Machine Learning + Streamlit**
""")

st.divider()

# ---------------------------------------
# Dashboard Cards
# ---------------------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.metric(
        "🏙 City",
        city
    )

with col2:

    st.metric(
        "🌡 Avg Temperature",
        f"{avg_temp:.2f} °C"
    )

with col3:

    st.metric(
        "🔥 Max Temperature",
        f"{max_temp:.2f} °C"
    )

with col4:

    st.metric(
        "🌳 Average NDVI",
        f"{avg_ndvi:.3f}"
    )

col5,col6,col7 = st.columns(3)

with col5:

    st.metric(
        "🤖 AI Risk Score",
        f"{risk_score:.1f}/100"
    )

with col6:

    st.metric(
        "📊 Training Samples",
        f"{training_samples:,}"
    )

with col7:

    st.metric(
        "🧠 AI Model",
        "Random Forest"
    )

st.divider()



# ---------------------------------------
# Tabs
# ---------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🛰 Heat Map",
    "🔥 Hotspots",
    "🌳 NDVI",
    "🤖 AI Prediction",
    "📊 Analytics"
])

with tab1:

    st.header("🌡️ Land Surface Temperature")

    st.image(
        str(HEAT_MAP),
        use_container_width=True
    )

    with st.expander("About this Heat Map"):

        st.write("""
This map shows the **Land Surface Temperature (LST)** derived from
Landsat-8 Thermal Infrared imagery.

### Color Interpretation

🔵 Blue → Cooler Surface

🟢 Green → Moderate Temperature

🟡 Yellow → Warm Surface

🟠 Orange → High Temperature

🔴 Red → Extreme Heat

These hotspots indicate Urban Heat Island (UHI) regions that require
cooling interventions.
""")

    st.success(
        f"Maximum Surface Temperature : {max_temp:.2f} °C"
    )


with tab2:

    st.header("🔥 Urban Heat Hotspots")

    st.image(
        str(HOTSPOT_MAP),
        use_container_width=True
    )

    with st.expander("Hotspot Detection Method"):

        st.write("""
Hotspots were detected using a temperature threshold.

Pixels having

**LST > 40°C**

were classified as heat stress zones.

These areas require immediate mitigation.
""")

    st.warning(
        "High temperature regions have been automatically identified."
    )


with tab3:

    st.header("🌳 Vegetation Analysis")

    st.image(
        str(NDVI_MAP),
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Average NDVI",
            f"{avg_ndvi:.3f}"
        )

    with col2:

        vegetation = avg_ndvi * 100

        st.metric(
            "Estimated Vegetation Cover",
            f"{vegetation:.1f}%"
        )

    with st.expander("What is NDVI?"):

        st.write("""
NDVI (Normalized Difference Vegetation Index) measures vegetation health.

### NDVI Scale

0.6 – 1.0 → Dense Vegetation

0.3 – 0.6 → Moderate Vegetation

0.1 – 0.3 → Sparse Vegetation

< 0.1 → Bare Land / Urban Areas

Lower NDVI usually corresponds to higher urban temperatures.
""")

    if avg_ndvi < 0.2:

        st.error(
            "Low vegetation detected. Urban greening is recommended."
        )

    elif avg_ndvi < 0.4:

        st.warning(
            "Moderate vegetation cover."
        )

    else:

        st.success(
            "Healthy vegetation cover."
        )


with tab4:

    st.header("🤖 Interactive AI Heat Risk Prediction")

    st.write("Adjust the environmental conditions and let the AI predict the heat risk.")

    user_ndvi = st.slider(
        "🌳 Average NDVI",
        min_value=0.0,
        max_value=0.8,
        value=float(avg_ndvi),
        step=0.01
    )

    user_temp = st.slider(
        "🌡 Maximum Temperature (°C)",
        min_value=20.0,
        max_value=60.0,
        value=float(max_temp),
        step=0.5
    )


    future_ndvi, future_temp = apply_scenario(
        user_ndvi,
        user_temp,
        tree_cover,
        cool_roofs,
        water_restoration
    )

    future_risk = predict_risk(
        future_ndvi,
        future_temp
    )

    
    predicted_risk = predict_risk(
        user_ndvi,
        user_temp
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Current NDVI",
            f"{user_ndvi:.3f}"
        )

    with col2:
        st.metric(
            "Current Temperature",
            f"{user_temp:.1f} °C"
        )

    with col3:
        st.metric(
            "Predicted Heat Risk",
            f"{predicted_risk:.1f}/100"
        )

    recommendation = get_recommendation(predicted_risk)


    

    st.divider()

    # -------------------------
    # Risk Gauge
    # -------------------------

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=predicted_risk,
        title={"text": "Heat Risk Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "darkred"},
            "steps": [
                {"range": [0, 50], "color": "lightgreen"},
                {"range": [50, 80], "color": "orange"},
                {"range": [80, 100], "color": "red"},
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # -------------------------
    # Risk Level
    # -------------------------

    if predicted_risk < 40:

        st.success("🟢 Safe Zone")

    elif predicted_risk < 70:

        st.warning("🟠 Moderate Heat Risk")

    else:

        st.error("🔴 Severe Heat Risk")

    st.subheader("Recommended Cooling Strategies")

    for action in recommendation["actions"]:

        st.write(action)


    st.divider()
    st.subheader("📈 Scenario Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Current")

        st.metric("NDVI", f"{user_ndvi:.3f}")
        st.metric("Temperature", f"{user_temp:.1f} °C")
        st.metric("Risk", f"{predicted_risk:.1f}")

    with col2:
        st.markdown("### After Interventions")

        st.metric(
            "NDVI",
            f"{future_ndvi:.3f}",
            delta=f"+{future_ndvi-user_ndvi:.3f}"
        )

        st.metric(
            "Temperature",
            f"{future_temp:.1f} °C",
            delta=f"-{user_temp-future_temp:.1f} °C"
        )

        st.metric(
            "Risk",
            f"{future_risk:.1f}",
            delta=f"-{predicted_risk-future_risk:.1f}"
        )

    st.divider()

    st.subheader("🤖 AI Decision Summary")

    st.info(f"""
Average NDVI : {user_ndvi:.3f}

Maximum Temperature : {user_temp:.2f} °C

Predicted Heat Risk : {predicted_risk:.1f}/100

The Random Forest model predicts heat stress using
satellite-derived vegetation and temperature information.
The recommended interventions aim to reduce urban heat
and improve thermal comfort.
""")
    


with tab5:

    st.header("📊 Analytics")

    st.subheader("Feature Importance")

    importance_df = pd.DataFrame({
        "Feature": ["LST", "NDVI"],
        "Importance": [99.08, 0.92]
    })

    fig = px.bar(
        importance_df,
        x="Feature",
        y="Importance",
        title="Random Forest Feature Importance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("Project Statistics")

    stats_df = pd.DataFrame({
        "Metric": [
            "Training Samples",
            "Average NDVI",
            "Average Temperature",
            "Maximum Temperature"
        ],
        "Value": [
            f"{training_samples:,}",
            f"{avg_ndvi:.3f}",
            f"{avg_temp:.2f} °C",
            f"{max_temp:.2f} °C"
        ]
    })

    st.dataframe(
        stats_df,
        use_container_width=True
    )

    st.divider()

    st.subheader("Dataset Distribution")

    histogram = px.histogram(
        df,
        x="Risk",
        nbins=30,
        title="Heat Risk Distribution",
        labels={"Risk":"Heat Risk Score"},
        marginal="box"
    )

    st.plotly_chart(
        histogram,
        use_container_width=True
    )

    st.divider()
    st.subheader("🌳 NDVI vs Temperature")

    scatter = px.scatter(
        df.sample(5000),      # Sample for faster rendering
        x="NDVI",
        y="LST",
        color="Risk",
        title="Relationship between Vegetation and Surface Temperature",
        opacity=0.6
    )

    st.plotly_chart(
        scatter,
        use_container_width=True
    )

    st.divider()

    st.subheader("🌡 Land Surface Temperature Distribution")

    temp_hist = px.histogram(
        df,
        x="LST",
        nbins=40,
        title="Temperature Distribution"
    )

    st.plotly_chart(
        temp_hist,
        use_container_width=True
    )

    st.divider()

    st.subheader("🌿 NDVI Distribution")

    ndvi_hist = px.histogram(
        df,
        x="NDVI",
        nbins=40,
        title="Vegetation Distribution"
    )

    st.plotly_chart(
        ndvi_hist,
        use_container_width=True
    )

    risk_df = df.copy()

    risk_df["Category"] = pd.cut(
        risk_df["Risk"],
        bins=[0,40,70,100],
        labels=["Low","Moderate","High"]
    )

    pie = px.pie(
        risk_df,
        names="Category",
        title="Heat Risk Categories"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

    st.divider()

    st.subheader("📈 Correlation Matrix")

    corr = df.corr(numeric_only=True)

    heatmap = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Correlation between Features"
    )

    st.plotly_chart(
        heatmap,
        use_container_width=True
    )



st.divider()

with st.expander("ℹ️ About HeatShield AI"):

    st.write("""
### HeatShield AI

HeatShield AI is an AI-powered Urban Heat Island
Mitigation System developed for BAH 2026.

### Features

✅ Satellite-based Heat Mapping

✅ Hotspot Detection

✅ NDVI Vegetation Analysis

✅ AI Risk Prediction

✅ Cooling Recommendations

### Technology Stack

• Google Earth Engine

• Landsat 8

• Python

• Streamlit

• Scikit-Learn

• Random Forest

### Study Area

Lucknow, India
""")
    

st.divider()

st.markdown(
    """
    <center>
    <b>HeatShield AI</b><br>
    Built for <b>BAH 2026 Hackathon</b><br>
    Developed by <b>ASTRA AI</b><br><br>

    Google Earth Engine • Python • Streamlit • Random Forest
    </center>
    """,
    unsafe_allow_html=True
)
