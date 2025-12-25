from langgraph.graph import StateGraph, END

from app.agent.state import AgentState
from app.agent.intent import analyze_intent
from app.agent.decision import decide_next_step


def build_agent_graph():
    graph = StateGraph(AgentState)

    #registrar nodes
    graph.add_node("analyze_intent", analyze_intent)
    graph.add_node("decide_next_step", decide_next_step)

    #definir o fluxo
    graph.set_entry_point("analyze_intent")
    graph.add_edge("analyze_intent", "decide_next_step")
    graph.add_edge("decide_next_step", END)

    return graph.compile()