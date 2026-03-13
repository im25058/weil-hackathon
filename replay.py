import json

def load_audit_logs():

    logs = []

    try:

        with open("audit_logs.json", "r") as f:

            for line in f:

                logs.append(json.loads(line))

    except:

        pass

    return logs