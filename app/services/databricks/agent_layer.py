import pandas as pd
import os

# -------------------------------
# Logger
# -------------------------------
from app.utils.logger import get_logger
logger = get_logger("agent_layer")

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Paths
input_path = os.path.join(BASE_DIR, "app/data_lake/silver/data.parquet")
output_path = os.path.join(BASE_DIR, "app/data_lake/gold/insights.parquet")

logger.info("Starting Agent Layer")

# Load data
df = pd.read_parquet(input_path)
logger.info(f"Loaded Silver data from: {input_path}")

logger.info(f"Input Data:\n{df}")

# Agent Logic (UNCHANGED)
def agent_analyze(data):
    insights = []

    for row in data:
        if row["amount"] > 150:
            insights.append({
                "id": row["id"],
                "insight": "High value transaction"
            })
        else:
            insights.append({
                "id": row["id"],
                "insight": "Normal transaction"
            })
    return insights

# Convert
data = df.to_dict(orient='records')

# Run agent
insights = agent_analyze(data)

# Convert back
insights_df = pd.DataFrame(insights)

logger.info(f"Generated Insights:\n{insights_df}")

# Save
insights_df.to_parquet(output_path, index=False)
logger.info(f"Saved Gold data to: {output_path}")

logger.info("Agent layer completed successfully")