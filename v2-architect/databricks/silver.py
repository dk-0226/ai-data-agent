import pandas as pd
import os

# Get project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define input/output paths
input_path = os.path.join(BASE_DIR, "data/bronze/data.parquet")
output_path = os.path.join(BASE_DIR, "data/silver/data.parquet")

df = pd.read_parquet(input_path)

print("Raw Data: ")
print(df)

# Cleaning logic

clean_df = df.dropna(subset=["name"])
clean_df = clean_df[clean_df["amount"] > 0]

print("\n Cleaned Data: ")
print(clean_df)

# Save Silver Data

clean_df.to_parquet(output_path, index=False)

print("Silver layer created successfully")
print(f"Output saved at :, {output_path}")

