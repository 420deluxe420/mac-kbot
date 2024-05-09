import os
import requests

# Function to retrieve the port and password from the League of Legends lockfile
def get_lockfile_info():
    lockfile_path = "/Applications/League of Legends.app/Contents/LoL/lockfile"
    if not os.path.exists(lockfile_path):
        print("Lockfile not found.")
        return None, None
    with open(lockfile_path, "r") as file:
        lockfile_content = file.readline().strip().split(":")
        port = lockfile_content[2]
        password = lockfile_content[3]
    return port, password

# Function to perform authenticated POST request
def authenticated_post(url, payload):
    port, password = get_lockfile_info()
    if port is None or password is None:
        return {"error": "Lockfile not found."}
    headers = {'Content-Type': 'application/json'}
    auth = ('riot', password)
    response = requests.post(url, headers=headers, json=payload, auth=auth, verify=False)
    return response.json()

if __name__ == "__main__":
    pass  # No need to execute anything in this case