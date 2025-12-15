from openai import OpenAI
from app.agent.state import AgentState
from app.core.config import Settings

client = OpenAI(api_key=Settings.OPENAI_API_KEY)


INTENT_SYSTEM_PROMPT = """
You are an AI system responsible for classifying user intent.

Possible intents:
- QUERY_DATA
- TAKE_ACTION
- ANALYZE_ONLY

Rules:
- Respond with ONLY the intent name.
- Do not explain.
- Do not add extra text.
"""

def analyze_intent(state: AgentState) -> AgentState:
    # analize o input do usuario e determinar a inteção do agent

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": INTENT_SYSTEM_PROMPT},
            {"role": "user", "content": state.user_input},
        ],
        temperature=0
    )

    intent = response.choices[0].message.content.strip()

    if intent not in {"QUERY_DATA", "TAKE_ACTION", "ANALYZE_ONLY"}:
        intent = "ANALYZE_ONLY"

    state.intent = intent
    return state