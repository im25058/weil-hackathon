import hashlib

def generate_hash(text):

    hash_object = hashlib.sha256(text.encode())

    return hash_object.hexdigest()