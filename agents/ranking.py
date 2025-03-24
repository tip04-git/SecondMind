class RankingAgent:
    def rank(self, idea):
        """Assign a score to the idea."""
        scores = {"solar panels": 8, "wind turbines": 7, "geothermal": 6}
        return scores.get(idea, 5)