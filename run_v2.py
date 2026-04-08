from dotenv import load_dotenv
load_dotenv()

# -------------------------------
# Import Config
# -------------------------------
from app.config.loader import get_config

# -------------------------------
# Import Pipeline
# -------------------------------
from app.pipelines.run_pipeline import run_pipeline


def main():
    print("🚀 Running v2 Architect Pipeline...\n")

    # Load config
    config = get_config()

    import os

    print(f"🌍 ENV: {os.getenv('ENV')}")
    print(f"🔧 Log Level: {config.logging.level}")
    print(f"📦 Batch Size: {config.pipeline.batch_size}")

    # Run pipeline with config
    run_pipeline(config)

    print("\n Pipeline execution completed")


if __name__ == "__main__":
    main()