import pandas as pd
import os

# Get project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define paths
input_path = os.path.join(BASE_DIR, "data/silver/data.parquet")
output_path = os.path.join(BASE_DIR, "data/gold/insights.parquet")

# Load Silver Data
df = pd.read_parquet(input_path)

print("Input Data for Agent: ")
print(df)

# Agent Logic (Simulating AI)
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

# Convert Dataframe to list of dict
data = df.to_dict(orient='records')

# Run agent
insights = agent_analyze(data)

# Convert back to dataframe
insights_df = pd.DataFrame(insights)

print("\n Agent Insights: ")
print(insights_df)

# Save Gold Layer
insights_df.to_parquet(output_path, index=False)

print("\n Agent Layer completed successfully")
print(f"Output saved at: {output_path}")