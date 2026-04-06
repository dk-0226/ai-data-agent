import pandas as pd
import os

#Get project root dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define paths
input_path = os.path.join(BASE_DIR, "data/raw/data.csv")
output_path = os.path.join(BASE_DIR, "data/bronze/data.parquet")

# Read and Write

df = pd.read_csv(input_path)
df.to_parquet(output_path, index=False)
print("Bronze layer created successfully")
print(f"Output saved at: {output_path}")
