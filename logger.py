import json
import datetime

def log_step(step_id, action, input_data, output_data):

    log = {
        "step_id": step_id,
        "action": action,
        "input": str(input_data),
        "output": str(output_data),
        "timestamp": str(datetime.datetime.now())
    }

    with open("audit_logs.json", "a") as f:

        f.write(json.dumps(log) + "\n")

    print("AUDIT LOG:", log)