import requests
import lockfile

def dodge_lobby():
    port, password = lockfile.get_lockfile_info()
    if port is None or password is None:
        return {"error": "Lockfile not found."}
    
    url = f'https://127.0.0.1:{port}/lol-login/v1/session/invoke?destination=lcdsServiceProxy&method=call&args=["","teambuilder-draft","quitV2",""]'
    auth = ('riot', password)  # Assuming 'riot' is the username
    
    try:
        response = requests.post(url, auth=auth, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        # Remove the line that triggers the message box
        # return {"success": "Lobby dodged successfully"}
        return {"success": "Lobby dodged successfully"}  # You can return this message if needed
    except requests.exceptions.RequestException as e:
        return {"error": f"An error occurred: {e}"}
