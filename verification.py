import hashlib

def verify_report(report, stored_hash):

    new_hash = hashlib.sha256(report.encode()).hexdigest()

    if new_hash == stored_hash:
        return True
    else:
        return False