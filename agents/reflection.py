class ReflectionAgent:
    def reflect(self, idea):
        """Check if the idea makes sense."""
        return idea if "solar" in idea else "Needs refinement"