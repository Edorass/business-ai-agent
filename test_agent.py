# test_agent.py
from agent import app


def test_agent_output():
    sample_data = {
        "today": {"revenue": 1500, "cost": 800, "customers": 40},
        "yesterday": {"revenue": 1200, "cost": 600, "customers": 30}
    }

    result = app.invoke(sample_data)

    assert "profit_status" in result
    assert "alerts" in result
    assert "recommendations" in result

    assert result["profit_status"] == "Profit: 700"
    assert isinstance(result["alerts"], list)
    assert isinstance(result["recommendations"], list)

    print("✅ Test passed.")