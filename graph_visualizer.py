import graphviz

def draw_agent_graph():

    dot = graphviz.Digraph()

    dot.node("A", "User Query")
    dot.node("B", "Planner Agent")
    dot.node("C", "Research Agent")
    dot.node("D", "Validator Agent")
    dot.node("E", "Report Generator")
    dot.node("F", "Hash + Blockchain")

    dot.edges([
        ("A","B"),
        ("B","C"),
        ("C","D"),
        ("D","E"),
        ("E","F")
    ])

    return dot