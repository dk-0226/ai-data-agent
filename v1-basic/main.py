from dotenv import load_dotenv
import os
import sys

# -------------------------------
# Fix Python import paths
# -------------------------------
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Add v1-basic to Python path so "agents", "tools" etc. work
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()

# Optional: Debug (you can remove later)
print("API KEY Loaded:", os.getenv("OPENAI_API_KEY"))

# -------------------------------
# Import your agent
# -------------------------------
from agents.agent import run_agent


def main():
    print("\n🚀 Starting AI Data Agent...\n")
    
    result = run_agent()
    
    print("\n✅ Final Result:\n")
    print(result)


if __name__ == "__main__":
    main()