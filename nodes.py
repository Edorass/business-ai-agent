# nodes.py

def input_node(data: dict) -> dict:
    '''
    returns the input as is so that the next node can process it.
    This node simply acts as the start of the graph
    '''
    return data

def processing_node(data: dict) -> dict:
    '''
    Calculations related to Costumer Customer Acquisition Cost (CAC) profit and percentage changes
    
    '''
    today = data["today"]
    yesterday = data["yesterday"]

    profit = today["revenue"] - today["cost"]
    today_cac = today["cost"] / today["customers"]
    yesterday_cac = yesterday["cost"] / yesterday["customers"]

    revenue_change = ((today["revenue"] - yesterday["revenue"]) / yesterday["revenue"]) * 100
    cost_change = ((today["cost"] - yesterday["cost"]) / yesterday["cost"]) * 100
    cac_change = ((today_cac - yesterday_cac) / yesterday_cac) * 100

    # Create a middle result for the next node
    return {
        **data,
        "profit": profit,
        "today_cac": today_cac,
        "cac_change": cac_change,
        "revenue_change": revenue_change,
        "cost_change": cost_change
    }

def recommendation_node(metrics: dict) -> dict:
    '''
    Generates suggestions based on the output of previous processing
    '''
    recommendations = []
    alerts = []

    if metrics["profit"] < 0:
        recommendations.append("Reduce Costs")

    if metrics["cac_change"] > 20:
        alerts.append(f"CAC increased by {metrics['cac_change']:.1f}%")
        recommendations.append("Review marketing campaigns")

    if metrics["revenue_change"] > 0:
        recommendations.append("Consider increasing advertising budget")

    return {
        "profit_status": f"Profit: {metrics['profit']}",
        "alerts": alerts,
        "recommendations": recommendations
    }
