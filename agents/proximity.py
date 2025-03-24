class ProximityAgent:
    def recall(self, query, memory):
        """Check if past interactions exist."""
        return memory.retrieve(query)