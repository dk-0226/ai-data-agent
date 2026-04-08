import pandas as pd
import os

# -------------------------------
# Logger
# -------------------------------
from app.utils.logger import get_logger
logger = get_logger("silver_layer")


def run_silver_layer(config):
    # Get project root (UNCHANGED)
    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
        )
    )

    # Paths (UNCHANGED)
    input_path = os.path.join(BASE_DIR, "app/data_lake/bronze/data.parquet")
    output_path = os.path.join(BASE_DIR, "app/data_lake/silver/data.parquet")

    logger.info("Starting Silver Layer")

    df = pd.read_parquet(input_path)
    logger.info(f"Loaded data from: {input_path}")

    logger.info(f"Raw Data:\n{df}")

    # Cleaning logic (UNCHANGED)
    clean_df = df.dropna(subset=["name"])
    clean_df = clean_df[clean_df["amount"] > 0]

    logger.info(f"Cleaned Data:\n{clean_df}")

    # Save
    clean_df.to_parquet(output_path, index=False)
    logger.info(f"Saved Silver data to: {output_path}")

    logger.info("Silver layer completed successfully")