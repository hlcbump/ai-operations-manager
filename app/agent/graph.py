from langgraph.graph import StateGraph, END

from app.agent.state import AgentState
from app.agent.intent import analyze_intent
from app.agent.decision import decide_next_step
from app.agent.nodes import retrieve_information, execute_action

def route_by_decision(state: AgentState) -> str:
    #determina o proximo node baseado na decisão do agente
    
    if state.decision == "RETRIEVE_INFORMATION":
        return "retrieve_information"
    
    if state.decision == "EXECUTE_ACTION":
        return "execute_action"
    
    return END

def build_agent_graph():
    graph = StateGraph(AgentState)

    # registrar nodes
    graph.add_node("analyze_intent", analyze_intent)
    graph.add_node("decide_next_step", decide_next_step)
    graph.add_node("retrieve_information", retrieve_information)
    graph.add_node("execute_action", execute_action)

    # definir o fluxo
    graph.set_entry_point("analyze_intent")
    graph.add_edge("analyze_intent", "decide_next_step")

    graph.add_conditional_edges(
        "decide_next_step",
        route_by_decision,
        {
            "retrieve_information": "retrieve_information",
            "execute_action": "execute_action",
            END: END,
        },
    )

    graph.add_edge("retrieve_information", END)
    graph.add_edge("execute_action", END)

    return graph.compile()