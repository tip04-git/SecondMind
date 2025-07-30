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

## 🗂️ Project Structure
AgentSystem/
│
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

---

## 📌 Future Improvements

- Integration with ArXiv API directly (to bypass scraping limitations)  
- GUI dashboard for real-time control of agent workflows  
- LLM fine-tuning on domain-specific research documents  
- Enhanced feedback loops between agents for adaptive intelligence

---

# SECOND MIND - Agents Based Research Assistant System

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
