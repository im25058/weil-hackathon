from langgraph.graph import StateGraph, END
from typing import TypedDict, List

from utils.llm import get_llm
from tools.web_search import web_search
from audit.logger import log_step
from utils.hashing import generate_hash

llm = get_llm()


class AgentState(TypedDict):

    query: str
    tasks: List[str]
    research: List[str]
    validated: str
    report: str
    hash: str


# ---------------- PLANNER AGENT ----------------

def planner_agent(state):

    query = state["query"]

    prompt = f"""
Break this research query into ONLY 3 steps.

Query:
{query}
"""

    response = llm.invoke(prompt)

    tasks = response.content.split("\n")[:3]

    log_step(1, "planner_agent", query, tasks)

    return {"tasks": tasks}

# ---------------- RESEARCH AGENT ----------------

def research_agent(state):

    tasks = state["tasks"]

    research_results = []

    for task in tasks:

        if task.strip() == "":
            continue

        result = web_search(task)

        research_results.append(result)

    combined = "\n".join(research_results)

    log_step(2, "research_agent", tasks, combined)

    return {"research": research_results}

# ---------------- VALIDATOR AGENT ----------------

def validator_agent(state):

    research = state["research"]

    combined = "\n".join(research)

    prompt = f"""
You are an expert research writer.

Using the research below, write a short structured report.

Research:
{combined}

Include:
- Introduction
- Key Points
- Conclusion
"""

    response = llm.invoke(prompt)

    validated_report = response.content

    log_step(3, "validator_agent", combined, validated_report)

    return {"validated": validated_report}

# ---------------- REPORT GENERATOR ----------------

def report_generator(state):

    report = state["validated"]

    log_step(4, "report_generation", "", report)

    return {"report": report}


# ---------------- HASH GENERATION ----------------

def hash_generator(state):

    report = state["report"]

    hash_value = generate_hash(report)

    log_step(5, "hash_generation", report, hash_value)

    return {"hash": hash_value}


# ---------------- BUILD GRAPH ----------------

builder = StateGraph(AgentState)

builder.add_node("planner", planner_agent)
builder.add_node("research", research_agent)
builder.add_node("validator", validator_agent)
builder.add_node("report", report_generator)
builder.add_node("hash", hash_generator)

builder.set_entry_point("planner")

builder.add_edge("planner", "research")
builder.add_edge("research", "validator")
builder.add_edge("validator", "report")
builder.add_edge("report", "hash")
builder.add_edge("hash", END)

graph = builder.compile()


def run_agent(query):

    result = graph.invoke({
        "query": query,
        "tasks": [],
        "research": [],
        "validated": "",
        "report": "",
        "hash": ""
    })

    return result["report"], result["hash"]