import requests
import lockfile

# Global variable to track the state of auto accept
auto_accept_enabled = False

def enable_auto_accept():
    global auto_accept_enabled
    port, _ = lockfile.get_lockfile_info()
    if port is None:
        return {"error": "Lockfile not found."}

    url = f"https://127.0.0.1:{port}/lol-matchmaking/v1/ready-check/accept"
    response = requests.post(url, verify=False)
    if response.status_code == 200:
        auto_accept_enabled = True
        return {"message": "Auto accept enabled successfully."}
    else:
        return {"error": "Failed to enable auto accept."}

def disable_auto_accept():
    global auto_accept_enabled
    auto_accept_enabled = False

# Function to check if auto accept is enabled
def is_auto_accept_enabled():
    global auto_accept_enabled
    return auto_accept_enabled
