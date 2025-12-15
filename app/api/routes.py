from fastapi import APIRouter
from pydantic import BaseModel

from app.agent.state import AgentState
from app.agent.intent import analyze_intent

router = APIRouter()

class AskRequest(BaseModel):
    question: str

@router.post("/ask")
def ask(request: AskRequest):
    state = AgentState(user_input=request.question)

    state = analyze_intent(state)
    return state