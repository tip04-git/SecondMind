import random

class GenerationAgent:
    def generate(self, query):
        """Generate initial ideas based on the query."""
        ideas = {
            "renewable energy": ["solar panels", "wind turbines", "geothermal"],
            "ai research": ["neural networks", "symbolic AI", "reinforcement learning"],
            "quantum computing": ["quantum gates", "quantum entanglement", "superposition computing"],
            "quantum learning": ["quantum neural networks", "quantum machine learning", "hybrid quantum-classical AI"],
            "cybersecurity": ["zero-trust architecture", "post-quantum cryptography", "blockchain security"],
            "sustainable software": ["energy-efficient algorithms", "low-power computing", "eco-friendly cloud storage"],
            "agi": ["self-learning AI", "adaptive neural networks", "goal-driven reasoning"],
            "machine unlearning": ["data forgetfulness", "model retraining", "AI bias mitigation"],
            "sustainable software design": ["green coding", "eco-friendly cloud systems", "carbon-aware computing"],
            "common sense reasoning in agentic ai": ["causal inference", "real-world knowledge graphs", "AI decision making"]
        }

        # Convert query to lowercase to match dictionary keys correctly
        query = query.lower().strip()  

        return random.choice(ideas.get(query, ["No relevant ideas found."]))
