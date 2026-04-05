#  AI-Powered Self-Healing Data Pipeline Agent

##  Overview
This project demonstrates an Agentic AI system that:
- Detects failed data pipeline jobs
- Analyzes logs using LLM
- Suggests fixes
- Retries jobs automatically

##  Architecture
LLM Agent → Tools → Logs → Retry → Memory

##  Tech Stack
- Python
- LangChain
- OpenAI
- Simulated Data Pipelines

## How to Run

```bash
git clone https://github.com/your-username/ai-data-agent.git
cd ai-data-agent
python3 -m venv agent_env
source agent_env/bin/activate
pip install -r requirements.txt
python main.py 

## Features
> Self-healing pipelines
> Log analysis
> Automated Retry
> Modular Architecture

## Future enhancements
> Databricks Integration
> ADF pipeline
> Streamlit UI

## Author
Dev Kishore
