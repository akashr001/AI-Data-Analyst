import os
from typing import TypedDict, List, Dict
from dotenv import load_dotenv
from openai import OpenAI
from langgraph.graph import StateGraph

load_dotenv()

# ---------------- OPENROUTER CLIENT ----------------

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def chat(prompt: str) -> str:
    resp = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct:free",
        messages=[{"role": "user", "content": prompt}],
        extra_headers={
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "AI Data Analyst"
        }
    )

    if not resp.choices or not resp.choices[0].message.content.strip():
        return "No meaningful response generated."

    return resp.choices[0].message.content.strip()

# ---------------- SHARED STATE ----------------

class AgentState(TypedDict):
    json_data: List[Dict]
    analytics: Dict
    plan: str
    understanding: str
    analysis: str
    monitor_feedback: str
    report: str

# ---------------- AGENTS ----------------

def planner_agent(state: AgentState) -> AgentState:
    if not state["json_data"]:
        state["plan"] = "No data available"
        return state

    columns = list(state["json_data"][0].keys())

    prompt = f"""
    You are a senior data analyst.

    Dataset columns:
    {columns}

    Decide what analysis should be done.
    """

    state["plan"] = chat(prompt)
    return state

def understanding_agent(state: AgentState) -> AgentState:
    prompt = f"""
    Explain this dataset in very simple words.

    Sample rows:
    {state["json_data"][:5]}
    """
    state["understanding"] = chat(prompt)
    return state

def analyst_team_agent(state: AgentState) -> AgentState:
    prompt = f"""
    Use the REAL analytics below to explain trends.

    Analytics:
    {state["analytics"]}
    """
    state["analysis"] = chat(prompt)
    return state

def monitor_agent(state: AgentState) -> AgentState:
    prompt = f"""
    Review the analysis below.

    {state["analysis"]}

    Reply with OK or list logical issues.
    """
    state["monitor_feedback"] = chat(prompt)
    return state

def reporter_agent(state: AgentState) -> AgentState:
    prompt = f"""
    Create a clear business report using ONLY these analytics.

    Analytics:
    {state["analytics"]}

    Analysis:
    {state["analysis"]}
    """
    report = chat(prompt).strip()
    state["report"] = report or "Analysis completed successfully."
    return state

# ---------------- LANGGRAPH FLOW ----------------

graph = StateGraph(AgentState)

graph.add_node("planner", planner_agent)
graph.add_node("understanding", understanding_agent)
graph.add_node("analyst_team", analyst_team_agent)
graph.add_node("monitor", monitor_agent)
graph.add_node("reporter", reporter_agent)

graph.set_entry_point("planner")
graph.add_edge("planner", "understanding")
graph.add_edge("understanding", "analyst_team")
graph.add_edge("analyst_team", "monitor")
graph.add_edge("monitor", "reporter")

app = graph.compile()
