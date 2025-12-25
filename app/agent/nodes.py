from app.agent.state import AgentState

def retrieve_information(state: AgentState) -> AgentState:
    #funcao placeholder para rag

    state.action_result = "rag não implementado ainda"
    return state

def execute_action(state: AgentState) -> AgentState:
    #funcao placeholder para executar ação

    state.action_result = "action não implementado ainda"
    return state