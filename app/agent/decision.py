from app.agent.state import AgentState

def decide_next_step(state: AgentState) -> AgentState:
    # Decide o que o agente deve fazer a seguir baseado na intenção detectada

    if state.intent == "QUERY_DATA":
        state.decision = "RETRIEVE_INFORMATION"

    elif state.intent == "TAKE_ACTION":
        state.decision = "EXECUTE_ACTION"

    else:
        state.decision = "RESPONDE_ONLY"
    
    return state