from fastapi import APIRouter
from pydantic import BaseModel

from app.agent.state import AgentState
from app.agent.intent import analyze_intent
from app.agent.decision import decide_next_step
from app.agent.graph import build_agent_graph

router = APIRouter()


class AskRequest(BaseModel):
    question: str


@router.post("/ask")
def ask(request: AskRequest):
    state = AgentState(user_input=request.question)

    graph = build_agent_graph()
    result = graph.invoke(state)

    return result
