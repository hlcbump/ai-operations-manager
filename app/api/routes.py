from fastapi import APIRouter
from pydantic import BaseModel

from app.agent.state import AgentState

router = APIRouter()

class AskRequest(BaseModel):
    question: str

@router.post("/ask")
def ask(request: AskRequest):
    state = AgentState(user_input=request.question)
    return state