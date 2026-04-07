import subprocess

# -------------------------------
# Logger
# -------------------------------
from app.utils.logger import get_logger
logger = get_logger("pipeline")

# Define pipeline steps
steps = [
    "app/services/databricks/bronze.py",
    "app/services/databricks/silver.py",
    "app/services/databricks/agent_layer.py"
]

def run_pipeline():
    logger.info("Starting pipeline execution...")

    for step in steps:
        logger.info(f"Running step: {step}")

        try:
            result = subprocess.run(
                ["python", step],
                capture_output=True,
                text=True
            )

            # Log stdout
            if result.stdout:
                logger.info(f"{step} OUTPUT:\n{result.stdout}")

            # Log stderr
            if result.stderr:
                logger.error(f"{step} ERROR:\n{result.stderr}")

            if result.returncode != 0:
                logger.error(f"Step failed: {step}")
                break

            logger.info(f"Completed step: {step}")

        except Exception as e:
            logger.exception(f"Unexpected error in step: {step} | {str(e)}")
            break

    logger.info("Pipeline execution completed")