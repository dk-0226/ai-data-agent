# -------------------------------
# Logger
# -------------------------------
from app.utils.logger import get_logger
logger = get_logger("pipeline")

# -------------------------------
# Import Layers (NEW)
# -------------------------------
from app.services.databricks.bronze import run_bronze_layer
from app.services.databricks.silver import run_silver_layer
from app.services.databricks.agent_layer import run_agent_layer


def run_pipeline(config):
    logger.info("Starting pipeline execution...")

    try:
        # -------------------------------
        # Bronze Layer
        # -------------------------------
        logger.info("Running Bronze Layer...")
        run_bronze_layer(config)

        # -------------------------------
        # Silver Layer
        # -------------------------------
        logger.info("Running Silver Layer...")
        run_silver_layer(config)

        # -------------------------------
        # Agent Layer
        # -------------------------------
        logger.info("Running Agent Layer...")
        run_agent_layer(config)

    except Exception as e:
        logger.exception(f"Pipeline failed: {str(e)}")

    logger.info("Pipeline execution completed")