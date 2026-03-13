from tools.web_search import web_search

def execute_tasks(tasks):

    results = []

    for task in tasks:

        result = web_search(task)

        results.append({
            "task": task,
            "result": result
        })

    return results