# 🧠 Second Mind – Agents-Based Research Assistant System

**Second Mind** is a modular, multi-agent AI system designed to automate key academic research tasks such as hypothesis generation, literature review, ranking, and refinement. Built with Python, the system simulates the collaboration of expert agents to streamline the research workflow from query to insight.

---

## 📘 Project Description

This intelligent pipeline of agents enables researchers and students to:

- Automatically fetch the latest domain-specific research papers  
- Generate concise summaries using LLM-powered logic  
- Rank papers based on relevance and citation heuristics  
- Reflect on hypothesis validity with real-time feedback  
- Evolve and improve ideas iteratively  
- Monitor system performance with visual analytics

---

## 🚀 Key Features

- 🧩 **Modular Agent-Based Design** – Each agent performs a distinct task in the research workflow  
- 🔍 **Real-Time Web Search** – Uses Google Custom Search for paper retrieval (e.g., arXiv, ResearchGate)  
- 🧠 **Topic-Aware Hypothesis Refinement** – Evolve queries contextually based on current literature  
- 🔁 **Query Caching** – Reduces repeated processing via memory-based proximity checks  
- 📊 **Performance Monitoring** – Track execution time, CPU & memory usage with real-time charts  
- 📈 **Visual Analytics** – View detailed system behavior via Matplotlib graphs

---

## 🤖 Core Agents

| Agent Name         | Responsibility                                                                 |
|--------------------|----------------------------------------------------------------------------------|
| **GenerationAgent**   | Fetches domain summaries and papers using Google Search API                    |
| **RankingAgent**      | Ranks papers by relevance score, citation strength, and semantic context       |
| **ReflectionAgent**   | Evaluates how well top papers support or conflict with the hypothesis          |
| **EvolutionAgent**    | Refines or rewrites hypotheses using learned context or keywords               |
| **ProximityAgent**    | Detects similar past queries to reuse memory and optimize performance          |
| **MetaReviewAgent**   | Logs and visualizes system metrics including execution time and memory usage   |

---

## 🧠 Technology Stack

- **Core Language**: Python 3.x  
- **Architecture**: Modular multi-agent system  
- **Key Libraries**:
  - `requests` – Google Search API integration  
  - `dotenv` – Secure environment variable management  
  - `psutil` – Real-time resource monitoring  
  - `time`, `json`, `re`, `os` – System control & I/O  
  - `matplotlib` – Performance data visualization

---

## 📈 Performance Metrics Tracked

- Total query execution time  
- CPU and memory utilization per session  
- Cache hits vs misses  
- Number of processed queries  
- API call delays (if simulated or logged)

---

## 💾 Data Handling

- Persistent memory stored in `memory.json`
- ProximityAgent uses this memory to reduce redundant computation and API calls
- Supports temporal and semantic matching for historical queries

---

## 📊 Visual Outputs

Matplotlib graphs generated after each query:

- **Bar Chart** – Response time comparison  
- **Line Chart** – CPU & memory usage over time  
- **Pie Chart** – Cache hit vs miss ratio (optional)

---

```
## 🗂️ Project Structure

AgentSystem/
├── agents/ # All AI agents
│ ├── generation.py # Fetches domain content
│ ├── ranking.py # Ranks results based on relevance
│ ├── reflection.py # Evaluates query quality
│ ├── evolution.py # Refines the query based on keywords
│ ├── proximity.py # Memory lookup for similar past queries
│ └── meta_review.py # Performance evaluation agent
│
├── supervisor/
│ └── supervisor.py # Coordinates agent execution
│
├── storage/
│ └── memory.json # Query cache and memory log
│
├── main.py # Entry point for the system
├── requirements.txt # Python dependencies
├── .env # API keys and configurations
└── README.md # Project overview and usage
```
---

## 📌 Future Improvements

- Integration with ArXiv API directly (to bypass scraping limitations)  
- GUI dashboard for real-time control of agent workflows  
- LLM fine-tuning on domain-specific research documents  
- Enhanced feedback loops between agents for adaptive intelligence

---



