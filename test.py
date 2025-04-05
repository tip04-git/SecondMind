from supervisor.supervisor import Supervisor
from tabulate import tabulate

# ✅ Initialize Supervisor
supervisor = Supervisor()

while True:
    topic = input("\n🔍 Enter a research topic (or type 'exit' to stop or 'done' to visualise): ").strip()

    if topic.lower() == "exit":
        print("🚀 Research session ended.")
        break

    elif topic.lower() == "done":
        print("\n📊 Generating performance visualization...\n")
        if supervisor.topic_metrics:
            headers = supervisor.topic_metrics[0].keys()
            rows = [list(metric.values()) for metric in supervisor.topic_metrics]
            print(tabulate(rows, headers=headers, tablefmt="grid"))
            supervisor.show_combined_plots()
        else:
            print("No topic metrics to display.")
        break  # 🧨 This break MUST be inside the 'done' block. Don't outdent it!

    # ✅ This will now only run if the topic is not "exit" or "done"
    supervisor.process(topic)
    print("\n====================================\n")
