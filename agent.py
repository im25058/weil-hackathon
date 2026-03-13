from agent.planner import plan_query
from agent.executor import execute_tasks
from audit.logger import log_step
from utils.hashing import generate_hash


def run_agent(query):

    log_step(1, "Query Received", query, "")

    tasks = plan_query(query)

    log_step(2, "Tasks Created", query, tasks)

    results = execute_tasks(tasks)

    log_step(3, "Tasks Executed", tasks, results)

    report = ""

    for r in results:
        report += str(r)

    hash_value = generate_hash(report)

    log_step(4, "Report Generated", report, hash_value)

    return report, hash_value