import os
from dotenv import load_dotenv

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()

print("API KEY Loaded:", os.getenv("OPENAI_API_KEY"))  # Debug

# -------------------------------
# Import your agent
# -------------------------------
from app.agents.data_agent import run_agent


def main():
    print("\n🚀 Starting AI Data Agent...\n")

    result = run_agent()

    print("\n✅ Final Result:\n")
    print(result)


if __name__ == "__main__":
    main()