from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from tools.pipeline_tools import get_failed_jobs, retry_job, get_logs

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

tools = [
    Tool(
        name = "GetFailedJobs",
        func = lambda _: get_failed_jobs(),
        description = "Get all failed jobs"
    ),
    Tool(
        name = "GetLogs",
        func = lambda job_id: get_logs(int(job_id)),
        description = "Get logs for a job"
    ),
    Tool(
        name = "RetryJob",
        func = lambda job_id: retry_job(int(job_id)),
        description = "Retry failed job"
    ),
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def run_agent():
    task = """
    Find failed jobs, analyze logs, identify issue, suggest fix and retry jobs.
    """
    return agent.run(task)
