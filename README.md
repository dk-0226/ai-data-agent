# 🤖 AI-Powered Self-Healing Data Pipeline Agent

## 📌 Overview

This project demonstrates an **Agentic AI system** that can autonomously:

* Detect failed data pipeline jobs
* Analyze logs using LLM
* Suggest fixes
* Retry jobs

🚀 It has been extended into an **architect-level data platform** simulating real-world systems like Databricks and Azure Data Factory.

---

# 🏗️ Architecture

## 🔹 v1-basic (Agentic AI System)

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

## 🔹 v2-architect (Enterprise Data Platform)

```
ADF (Simulated Orchestration)
        ↓
Bronze Layer (Raw Data)
        ↓
Silver Layer (Cleaned Data)
        ↓
Agent Layer (AI Insights)
        ↓
Gold Layer (Business Output)
```

---

# 🧠 Key Features

### 🔹 v1-basic

* Autonomous AI agent for pipeline failure analysis
* LLM-powered log interpretation
* Self-healing retry mechanism
* Modular design (agents, tools, memory)

### 🔹 v2-architect

* Medallion architecture (Bronze → Silver → Gold)
* Simulated Databricks processing layers
* ADF-like orchestration pipeline
* Agentic AI layer for intelligent insights
* End-to-end data pipeline execution

---

# ⚙️ Tech Stack

* Python
* LangChain
* OpenAI
* Pandas
* Parquet (pyarrow)
* Simulated Data Pipelines

---

# 🔄 How It Works

## 🔹 v1-basic (Agent Workflow)

1. Fetch failed jobs
2. Read logs
3. Analyze failure
4. Suggest fix
5. Retry job

---

## 🔹 v2-architect (Data Pipeline Flow)

1. Ingest raw data (Bronze layer)
2. Clean and validate data (Silver layer)
3. Analyze data using AI agent (Agent layer)
4. Generate insights (Gold layer)
5. Orchestrate pipeline using simulated ADF

---

# ▶️ Run Locally

```bash
git clone https://github.com/dk-0226/ai-data-agent.git
cd ai-data-agent

# Create virtual environment
python3 -m venv agent_env
source agent_env/bin/activate

# Install dependencies
pip install -r v1-basic/requirements.txt

# Run v1 (Agent system)
python v1-basic/main.py

# Run v2 (Full pipeline)
python v2-architect/run_pipeline.py
```

---

# 📊 Sample Output

```
Job failed due to schema mismatch
Suggested fix: cast column to integer
Retrying job...

---

🔹 Agent Insights:
id | insight
1  | Normal transaction
2  | High value transaction
```

---

# 🌍 Real-World Mapping

| Your Project Component | Real System Equivalent     |
| ---------------------- | -------------------------- |
| run_pipeline.py        | Azure Data Factory         |
| bronze.py              | Databricks Bronze Notebook |
| silver.py              | Databricks Silver Notebook |
| agent_layer.py         | AI/ML Processing Layer     |
| data/ folders          | ADLS Gen2                  |
| Agents                 | LLM-powered services       |

---

# 🚀 Project Evolution

This project demonstrates a **progressive architecture approach**:

* **v1-basic** → Working Agentic AI system
* **v2-architect** → Enterprise-grade data platform design

👉 This showcases both **implementation skills** and **architectural thinking**

---

# 🔮 Future Enhancements

* Databricks integration (real cluster)
* Azure Data Factory pipeline triggers
* FastAPI-based agent service
* Real-time streaming (Kafka)
* Streamlit dashboard for visualization
* Multi-agent orchestration

---

# 👨‍💻 Author

**Dev Kishore**
