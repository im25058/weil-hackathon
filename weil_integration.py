from wadk import WeilClient

client = WeilClient()

def anchor_hash(report_hash):
    tx = client.store(report_hash)
    return tx