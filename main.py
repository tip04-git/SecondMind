# main.py
from supervisor.supervisor import Supervisor

if __name__ == "__main__":
    supervisor = Supervisor()
    query = input("Enter research topic: ")
    supervisor.process(query)
