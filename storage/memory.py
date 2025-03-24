# /storage/memory.py
class Memory:
    def __init__(self):
        self.data = {}  # Dictionary to store query-result pairs

    def store(self, query, result):
        self.data[query] = result

    def retrieve(self, query):
        return self.data.get(query, "No past results found.")

# Test
if __name__ == "__main__":
    memory = Memory()
    memory.store("solar panels", "Score: 8/10")
    print(memory.retrieve("solar panels"))  # Should print "Score: 8/10"
