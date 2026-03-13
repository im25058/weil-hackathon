import json
import datetime

def store_on_chain(hash_value):

    tx = {
        "transaction_id": "weil_tx_" + str(datetime.datetime.now().timestamp()),
        "report_hash": hash_value,
        "timestamp": str(datetime.datetime.now())
    }

    with open("weilchain_log.json", "a") as f:
        f.write(json.dumps(tx) + "\n")

    print("Stored on Weilchain (simulated):", tx)

    return tx