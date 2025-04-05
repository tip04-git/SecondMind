
# Agents-Based Research Assistant System

A modular multi-agent system designed to automate academic research tasks like hypothesis generation, literature search, ranking, reflection, and refinement using Python-based AI agents.

---

## 📘 Project Description

This system simulates a collaborative pipeline of AI agents, each responsible for a specific task in the academic research process. It uses a modular architecture to:

- Fetch the latest research papers
- Generate summaries for a research domain
- Rank papers based on relevance
- Analyze and improve research hypotheses
- Track system performance

---

## 🚀 Key Features

- Modular agent-based design
- Real-time paper fetching from Google (arXiv, ResearchGate, etc.)
- Topic-aware hypothesis refinement
- Query caching via memory file
- Performance monitoring (CPU, memory, execution time)
- Visual analytics using matplotlib

---

## 🤖 Core Agents

| Agent Name         | Functionality                                                                 |
|--------------------|--------------------------------------------------------------------------------|
| `GenerationAgent`  | Fetches domain summaries and recent research papers via Google Custom Search  |
| `RankingAgent`     | Ranks papers based on title relevance and assigns citation/reference scores   |
| `ReflectionAgent`  | Analyzes how well the hypothesis is supported by the top-ranked papers         |
| `EvolutionAgent`   | Refines hypotheses using topic-specific keywords or context from literature    |
| `ProximityAgent`   | Checks previous queries in memory to reuse past results                        |
| `MetaReviewAgent`  | Measures performance (time, CPU, memory) and provides feedback                 |

---

## 🧠 Technology Stack

### Backend / Core Logic

- Python 3.x
- Modular agent-based architecture

### Libraries & Tools

- `requests` – For Google Custom Search API
- `dotenv` – For managing API keys securely
- `psutil` – For performance tracking (CPU/memory)
- `time` – For query execution time tracking
- `json`, `os`, `re` – For system operations and data parsing
- `matplotlib` – For generating visual performance graphs

---

## 📈 Performance Metrics Tracked

- Query execution time
- CPU and memory usage
- Cache hits and misses
- Number of total queries
- API call delays (simulated or real)

---

## 💾 Data Handling

- All past research queries and responses are stored in `memory.json`
- Used by `ProximityAgent` to avoid redundant processing

---

## 📊 Visual Outputs

Generated using `matplotlib` after processing each query:

- Response time bar chart
- CPU and memory usage line chart
- Cache hits vs misses pie chart (optional)

---

## 🗂️ Project Structure
## 🗂️ Project Structure

AgentSystem/
│
├── agents/                     # All intelligent agents  
│   ├── generation.py           # Content generation agent  
│   ├── ranking.py              # Ranking & filtering agent  
│   ├── reflection.py           # Reflects on past responses  
│   ├── evolution.py            # Evolves/improves responses  
│   ├── proximity.py            # Checks proximity to past queries  
│   └── meta_review.py          # Evaluates performance  
│
├── supervisor/                 
│   └── supervisor.py           # Coordinates all agents  
│
├── storage/                    # Stores past queries, results, and cache  
│   └── memory.json             # Persistent memory storage  
│
├── main.py                     # Entry point for the app  
├── requirements.txt            # Python dependencies  
├── .env                        # API keys (e.g., OpenAI, Google)  
└── README.md                   # Project info & setup instructions  
