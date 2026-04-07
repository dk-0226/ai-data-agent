from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from app.pipelines.run_pipeline import run_pipeline

def main():
    print("🚀 Running v2 Architect Pipeline...\n")

    run_pipeline()

    print("\n Pipeline execution completed")


if __name__ == "__main__":
    main()