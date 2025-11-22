admin_password = "supersecret123"

def get_file(filename):
    # Vulnerability 3: Path traversal
    with open("/home/data/" + filename, "r") as f: