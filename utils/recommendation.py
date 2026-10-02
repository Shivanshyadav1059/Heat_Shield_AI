# """Recommendation utilities for HeatShieldAI."""


# def generate_recommendations(predictions):
#     recommendations = []
#     for value in predictions:
#         if value >= 0.8:
#             recommendations.append("High heat risk: issue alert and deploy cooling measures.")
#         elif value >= 0.5:
#             recommendations.append("Moderate heat risk: monitor conditions and advise hydration.")
#         else:
#             recommendations.append("Low heat risk: maintain standard operations.")
#     return recommendations


def get_recommendation(risk):

    if risk >= 80:
        return {
            "level": "High",
            "color": "red",
            "actions": [
                "🌳 Increase tree cover",
                "🏠 Install cool roofs",
                "💧 Restore water bodies",
                "🌬 Improve ventilation corridors"
            ]
        }

    elif risk >= 50:
        return {
            "level": "Moderate",
            "color": "orange",
            "actions": [
                "🌿 Develop green corridors",
                "🌱 Increase vegetation",
                "🏠 Use reflective roofing"
            ]
        }

    else:
        return {
            "level": "Low",
            "color": "green",
            "actions": [
                "✅ Preserve existing green spaces",
                "🌳 Continue urban tree maintenance"
            ]
        }