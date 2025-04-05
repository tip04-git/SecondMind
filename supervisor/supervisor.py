import json
import os
import time
import psutil
import math
from agents.generation import GenerationAgent
from agents.ranking import RankingAgent
from agents.reflection import ReflectionAgent
from agents.evolution import EvolutionAgent
from agents.proximity import ProximityAgent
from agents.meta_review import MetaReviewAgent
import matplotlib.pyplot as plt
from tabulate import tabulate  # pip install tabulate
from datetime import datetime



query_count = 0
cache_hits = 0
cache_misses = 0
api_calls = 0

class Supervisor:
    def __init__(self):
        self.generation = GenerationAgent()
        self.ranking = RankingAgent()
        self.reflection = ReflectionAgent()
        self.evolution = EvolutionAgent()
        self.proximity = ProximityAgent()
        self.meta_review = MetaReviewAgent()
        
        self.memory_file = "memory.json"
        self.memory = self.load_memory()  # ✅ Load past data on startup

        self.stored_plots = []
        self.metrics_list = []  # ✅ Stores data for later plotting


        self.topic_metrics = []
        self.performance_log = []  # For storing individual query performance logs


        self.performance_data = {
    "total_time": 0.0,
    "query_count": 0,
    "cache_hits": 0,
    "cache_misses": 0,
    "cpu_usage": [],
    "memory_used": [],
    "response_times": []

    }
    
    def load_memory(self):
        """Load stored research data from file."""
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as file:
                return json.load(file)
        return {}  # Return empty if no file exists

    def save_memory(self):
        """Save research data to file."""
        with open(self.memory_file, "w") as file:
            json.dump(self.memory, file, indent=4)

    def plot_performance_metrics(self, metrics):
        labels = list(metrics.keys())
        values = list(metrics.values())

        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(labels, values, color='skyblue')
        ax.set_xlabel("Metrics")
        ax.set_ylabel("Values")
        ax.set_title("Performance Metrics Overview")
        ax.tick_params(axis='x', rotation=30)

        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}', 
                ha='center', va='bottom')
        plt.tight_layout()

    # ✅ Instead of showing here, save the figure object
        return fig
    
    def show_all_plots(self):
        for fig in self.stored_plots:
            fig.show()

    def show_combined_plots(self):
        num_plots = len(self.metrics_list)
        if num_plots == 0:
            print("No metrics to display.")
            return

        cols = 2
        rows = math.ceil(num_plots / cols)

        fig, axes = plt.subplots(rows, cols, figsize=(12, 5 * rows))
        axes = axes.flatten()  # Makes it easy to index

        for i, metrics in enumerate(self.metrics_list):
            ax = axes[i]
            labels = list(metrics.keys())
            values = list(metrics.values())

            bars = ax.bar(labels, values, color='skyblue')
            ax.set_title(f"Performance Metrics - Query {i+1}")
            ax.set_ylabel("Values")
            ax.tick_params(axis='x', rotation=30)

            for bar in bars:
                yval = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}', 
                    ha='center', va='bottom')

    # Hide any unused subplots
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout()
        plt.show()

        

    def display_all_metrics(self):
        if not self.topic_metrics:
            print("⚠️ No topics were processed.")
            return

        print("\n📊 **Summary of All Topics Processed:**\n")
        headers = self.topic_metrics[0].keys()
        rows = [list(topic.values()) for topic in self.topic_metrics]
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    def process(self, query):
        """Process user query using multiple agents and improve hypothesis over multiple cycles."""
        print("\n" + "=" * 70)
        global query_count, cache_hits, cache_misses
        query_count += 1
        print(f"🔍 **Processing Research Topic:** {query}")
        print("=" * 70)

        # ✅ Step 1: Start Timer & CPU Usage Tracking
        self.meta_review.start_timer()
        process = psutil.Process()
        cpu_start_time = process.cpu_times().user  # Start CPU time

        # ✅ Step 2: Check past research using Proximity Agent
        print("\n📌 **[Proximity Agent] Checking Past Research...**")
        proximity_feedback = self.proximity.check_past_results(query, self.memory)
        print(f"   ➤ {proximity_feedback}")

        # ✅ Step 3: Check if query exists in memory (Cache Hit/Miss Tracking)
        if query in self.memory:
            cache_hits += 1
            stored_results = self.memory[query]

            # ✅ If hypothesis contains broken structure, reset it
            if " in AI-driven Landscape" in stored_results["hypothesis"]:
                print("⚠️ **[Fix] Bad hypothesis detected. Resetting...**")
                stored_results["hypothesis"] = query  # Reset to original query

            print("✅ **[Cache Hit] Using Previously Stored Research Results...**")

            # ✅ Step 4: Reflection Agent checks if hypothesis is still valid
            print("\n🧐 **[Reflection Agent] Analyzing Existing Research...**")
            ranked_papers = stored_results["ranked_papers"]
            hypothesis = stored_results["hypothesis"]
            reflection_feedback = self.reflection.reflect(query, hypothesis, ranked_papers)
            print(f"   ➤ {reflection_feedback}")

            if "needs refinement" in reflection_feedback:
                print("\n🔄 **[Evolution Agent] Refining Hypothesis...**")
                hypothesis = self.evolution.evolve(hypothesis, ranked_papers)
                print(f"   ➤ New Hypothesis: {hypothesis}")

            # ✅ Update stored hypothesis
            stored_results["hypothesis"] = hypothesis
            self.memory[query] = stored_results
            self.save_memory()
        else:
            cache_misses += 1
            print("❌ **[Cache Miss] No Prior Research Found. Generating New Results...**")

            # ✅ Step 5: Generate initial research & ranking
            print("\n⚙️ **[Generation Agent] Fetching Research Data...**")
            results = self.generation.generate(query)

            print("\n📊 **[Ranking Agent] Ranking Research Papers...**")
            ranked_papers = self.ranking.rank(query, results["recent_papers"])

            # ✅ Step 6: Reflection Agent checks relevance
            print("\n🧐 **[Reflection Agent] Evaluating Hypothesis...**")
            hypothesis = query  # Use query as initial hypothesis
            reflection_feedback = self.reflection.reflect(query, hypothesis, ranked_papers)
            print(f"   ➤ {reflection_feedback}")

            # ✅ Step 7: Evolution Agent refines hypothesis
            if "needs refinement" in reflection_feedback:
                print("\n🔄 **[Evolution Agent] Improving Hypothesis...**")
                hypothesis = self.evolution.evolve(hypothesis, ranked_papers)
                print(f"   ➤ Evolved Hypothesis: {hypothesis}")

            # ✅ Step 8: Store updated data in memory
            stored_results = {
                "summary": results["summary"],
                "ranked_papers": ranked_papers,
                "hypothesis": hypothesis
            }
            self.memory[query] = stored_results
            self.save_memory()

        # ✅ Step 9: Display results
        print("\n📖 **[Domain Summary]**\n" + "-" * 50)
        print(f"{stored_results['summary']}\n")

        print("\n📑 **[Recent Research Papers]**")
        for paper in stored_results["ranked_papers"]:
            print("\n------------------------------------------")
            print(f"\n 🔹 **Title:** {paper['title']}")
            print(f"   📅 **Year:** {paper['year']}")
            print(f"   🔗 **URL:** {paper['url']}")
            print(f"   📊 **Citations:** {paper['citations']}")
            print(f"   📖 **References:** {paper['references']}")
            print(f"   ⭐ **Relevance Score:** {paper['score']}/10")
        print("------------------------------------------")

        # ✅ Step 10: Stop Timer, Compute CPU Usage, and Display Performance Metrics
        total_time = self.meta_review.review_performance()
        cpu_usage = psutil.cpu_percent(interval=1)
        mem_usage = process.memory_info().rss / 1024 / 1024  # Convert to MB

        print(f"\n📊 **[Meta-Review Report]**")
        print(f"⏳ **Response Time:** {total_time}")
        print(f"💻 **CPU Usage:** {cpu_usage}%")
        print(f"💾 **Memory Used:** {mem_usage:.2f} MB")
        print(f"📊 **Total Queries Processed:** {query_count}")
        print(f"✅ **Cache Hits:** {cache_hits} | ❌ Cache Misses: {cache_misses}")

        self.performance_data["query_count"] += 1
        self.performance_data["cache_hits"] = cache_hits
        self.performance_data["cache_misses"] = cache_misses
        self.performance_data["memory_used"] = mem_usage

        metrics = {
            "Execution Time (s)": self.meta_review.query_time(),
            "Memory Used (MB)": mem_usage,
            "Total Queries": self.performance_data["query_count"],
            "Cache Hits": cache_hits,
            "Cache Misses": cache_misses
        }

        
        topic_data = {
        "Topic": query,
        "Execution Time (s)": self.meta_review.query_time(),
        "Memory Used (MB)": mem_usage,
        "Total Queries": self.performance_data["query_count"],
        "Cache Hits": cache_hits,
        "Cache Misses": cache_misses,
        "API Calls": api_calls,
        "Timestamp": datetime.now().strftime("%H:%M:%S")
        }
        self.topic_metrics.append(topic_data)
        self.plot_performance_metrics(metrics)
        self.metrics_list.append(metrics)
        print(f"Appended metrics for query {len(self.metrics_list)}")



        print("\n" + "=" * 70)

# Test
if __name__ == "__main__":
    supervisor = Supervisor()
    query = input("\nEnter research topic: ")
    supervisor.process(query)
