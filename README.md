# AI-Powered Self-Healing Data Pipeline Agent

##  Overview

This project demonstrates an **Agentic AI system** that can autonomously:

* Detect failed data pipeline jobs
* Analyze logs using LLM
* Suggest fixes
* Retry jobs

---

## Architecture

```
User / Scheduler
       ↓
   AI Agent (LLM)
       ↓
   Tool Layer (APIs)
       ↓
 Pipeline System (Simulated)
       ↓
   Memory Layer
```

---

##  Tech Stack

* Python
* LangChain
* OpenAI
* Simulated Data Pipelines

---

##  How It Works

1. Fetch failed jobs
2. Read logs
3. Analyze failure
4. Suggest fix
5. Retry job

---

##  Run Locally

```bash
git clone https://github.com/dk-0226/ai-data-agent.git
cd ai-data-agent
python3 -m venv agent_env
source agent_env/bin/activate
pip install -r requirements.txt
python main.py
```

---

## Sample Output

```
Job failed due to schema mismatch
Suggested fix: cast column to integer
Retrying job...
```

---

## Real-World Mapping

| Component | Real System    |
| --------- | -------------- |
| Tools     | Databricks API |
| Pipelines | ADF            |
| Storage   | ADLS Gen2      |
| Execution | Spark          |

---

## Future Enhancements

* Databricks integration
* ADF pipeline triggers
* Streamlit UI dashboard
* Multi-agent architecture

---

## Author

Dev Kishore
