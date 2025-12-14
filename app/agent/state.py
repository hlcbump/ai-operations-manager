from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class AgentState(BaseModel):
    # representa o estado completo do ai operations manager 
    # durante um unico ciclo de execução

    # entrada do usuario
    user_input: str

    # detecta a intenção (analise, query, ação etc..)
    intent: Optional[str] = None

    # contexto obtido da memória ou tools
    context: Dict[str, Any] = Field(default_factory=dict)

    # documentos obtidos via RAG
    retrieved_docs: List[str] = Field(default_factory=list)
    
    # decisão final feita pelo agente
    decision: Optional[str] = None

    # resultado após realizar uma ação    
    action_result: Optional[str] = None