from agent.agent_graph import run_agent

def applet(query):

    report, hash_value = run_agent(query)

    return {
        "report": report,
        "hash": hash_value
    }