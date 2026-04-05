from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Optional: Debug (you can remove later)
print("API KEY Loaded:", os.getenv("OPENAI_API_KEY"))

# Import your agent
from agents.agent import run_agent


def main():
    print("\n Starting AI Data Agent...\n")
    
    result = run_agent()
    
    print("\n Final Result:\n")
    print(result)


if __name__ == "__main__":
    main()
