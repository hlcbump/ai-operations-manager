from app.agent.state import AgentState

def analyze_intent(state: AgentState) -> AgentState:
    # analize o input do usuario e determinar a inteção do agent

    text = state.user_input.lower()

    if any(word in text for word in ["send", "email", "notify"]):
        state.intent = "TAKE_ACTION"

    elif any(word in text for word in ["which", "list", "show", "how many"]):
        state.intent = "QUERY_DATA"

    else:
        state.intent = "ANALYZE_ONLY"

    return state