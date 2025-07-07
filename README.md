# 📊 Business AI Agent (LangGraph)

This is a simple AI agent built with **LangGraph** to analyze basic business data such as daily sales, costs, and customer metrics. It calculates key business indicators and provides actionable recommendations and alerts based on the data.

---

## ✨ Features

- Calculates daily **profit**
- Computes **Customer Acquisition Cost (CAC)** and tracks its changes
- Analyzes **percentage change** in revenue and cost compared to the previous day
- Generates **alerts** and **actionable recommendations**
- Modular structure with clear logic
- Includes a test to validate agent behavior
- Compatible with **LangGraph Studio**

---

## ⚙️ Installation & Usage

```bash
# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install langgraph pytest

To run the agent manually:

bash
Copy
Edit
python agent.py
🔢 Sample Input
python
Copy
Edit
sample_data = {
    "today": {"revenue": 1500, "cost": 800, "customers": 40},
    "yesterday": {"revenue": 1200, "cost": 600, "customers": 30}
}
📤 Expected Output
json
Copy
Edit
{
  "profit_status": "Profit: 700",
  "alerts": [],
  "recommendations": [
    "Consider increasing advertising budget"
  ]
}
🧪 Testing
To run the test and validate the output logic:

bash
Copy
Edit
pytest test_agent.py

🧠 Tech Stack
Python 3.10+

LangGraph

Pytest

🧑‍💻 About
This project was built as a coding challenge for an AI Agent position using LangGraph.
https://github.com/Edorass
