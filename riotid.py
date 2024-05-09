import requests
import lockfile

# Function to change the Riot ID (nickname)
def change_riot_id(new_nickname, tag_line):
    # Retrieve port and password from the lockfile
    port, password = lockfile.get_lockfile_info()
    if port is None or password is None:
        return {"error": "Lockfile not found."}
    
    # Endpoint for changing the Riot ID
    url = f'https://127.0.0.1:{port}/lol-summoner/v1/save-alias'
    headers = {'Content-Type': 'application/json'}
    
    # Payload for changing the Riot ID
    data = {
        "gameName": new_nickname,
        "tagLine": tag_line
    }
    
    # Send the request to change the Riot ID
    auth = ('riot', password)
    response = requests.post(url, headers=headers, json=data, auth=auth, verify=False)
    return response.json()

if __name__ == "__main__":
    pass  # No need to execute anything in this case
