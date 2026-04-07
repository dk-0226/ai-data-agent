import os
from dotenv import load_dotenv

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()

# -------------------------------
# Logger
# -------------------------------
from app.utils.logger import get_logger
logger = get_logger("data_agent")

logger.info("Initializing Data Agent...")

# -------------------------------
# Imports
# -------------------------------
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool

from app.services.orchestration.pipeline_tools import (
    get_failed_jobs,
    retry_job,
    get_logs
)

from app.services.store import save_memory

# -------------------------------
# LLM
# -------------------------------
logger.info("Loading LLM...")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# -------------------------------
# Tools
# -------------------------------
logger.info("Setting up tools...")

tools = [
    Tool(
        name="GetFailedJobs",
        func=lambda _: get_failed_jobs(),
        description="Get all failed jobs"
    ),
    Tool(
        name="GetLogs",
        func=lambda job_id: get_logs(int(job_id)),
        description="Get logs for a job"
    ),
    Tool(
        name="RetryJob",
        func=lambda job_id: retry_job(int(job_id)),
        description="Retry failed job"
    ),
]

# -------------------------------
# Agent
# -------------------------------
logger.info("Initializing agent...")
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

# -------------------------------
# Run function
# -------------------------------
def run_agent():
    task = """
    Find failed jobs, analyze logs, identify issue, suggest fix and retry jobs.
    """

    logger.info("Agent started execution")
    logger.info(f"Task: {task.strip()}")

    result = agent.run(task)

    logger.info("Agent execution completed")

    # Save memory
    save_memory({"task": task, "result": result})
    logger.info("Memory saved")

    return result