import pandas as pd
import os

# -------------------------------
# Logger
# -------------------------------
from app.utils.logger import get_logger
logger = get_logger("bronze_layer")

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Paths
input_path = os.path.join(BASE_DIR, "app/data_lake/raw/data.csv")
output_path = os.path.join(BASE_DIR, "app/data_lake/bronze/data.parquet")

logger.info("Starting Bronze Layer")

# Read & Write
df = pd.read_csv(input_path)
logger.info(f"Read data from: {input_path}")

df.to_parquet(output_path, index=False)
logger.info(f"Saved Bronze data to: {output_path}")

logger.info("Bronze layer completed successfully")