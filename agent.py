# agent.py

from langgraph.graph import StateGraph, END
from nodes import input_node, processing_node, recommendation_node


# Definition of state type — a simple dictionary

state = dict

# Graph construction
graph = StateGraph(state)

# Registering nodes in the graph
graph.add_node("input", input_node)
graph.add_node("processing", processing_node)
graph.add_node("recommendation", recommendation_node)

# Connecting nodes together
graph.set_entry_point("input")  # We start from input
graph.add_edge("input", "processing")
graph.add_edge("processing", "recommendation")
graph.add_edge("recommendation", END)

# Build the ultimate Agent
app = graph.compile()

# This section is for direct execution of the file
if __name__ == "__main__":
    sample_data = {
        "today": {"revenue": 1500, "cost": 800, "customers": 40},
        "yesterday": {"revenue": 1200, "cost": 600, "customers": 30}
    }

    result = app.invoke(sample_data)
    print(result)