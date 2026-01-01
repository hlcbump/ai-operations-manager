from app.agent.state import AgentState
from app.rag.supabase_retriever import get_retriever


def retrieve_information(state: AgentState) -> AgentState:
    retriever = get_retriever()

    docs = retriever(state.user_input)

    SIMILARITY_THRESHOLD = 0.65
    print("SIMILARITY_THRESHOLD: ")
    print(SIMILARITY_THRESHOLD)

    filtered_docs = [
        doc for doc in docs if doc.metadata["similarity"] >= SIMILARITY_THRESHOLD
    ]

    state.retrieved_docs = [doc.page_content for doc in docs]

    print("[RAG] Retrieved documents:")
    for doc in filtered_docs:
        print(f" - {doc.page_content} (similarity={doc.metadata['similarity']:.2f})")

    state.retrieved_docs = [doc.page_content for doc in filtered_docs]
    state.action_result = "RAG_COMPLETED"

    return state


def execute_action(state: AgentState) -> AgentState:
    # funcao placeholder para executar ação

    state.action_result = "action não implementado ainda"
    return state
