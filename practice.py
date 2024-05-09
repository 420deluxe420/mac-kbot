import lockfile

# Function to start the 5v5 practice tool lobby
def start_practice_tool():
    # Endpoint for creating the practice tool lobby
    url = f'https://127.0.0.1:{lockfile.get_lockfile_info()[0]}/lol-lobby/v2/lobby'
    
    # Payload for creating the lobby
    payload = {
       "customGameLobby": {
          "configuration": {
             "gameMode": "PRACTICETOOL",
             "gameMutator": "",
             "gameServerRegion": "",
             "mapId": 11,  # Summoner's Rift
             "mutators": {"id": 1},  # Summoner's Rift
             "spectatorPolicy": "AllAllowed",
             "teamSize": 5  # 5v5
          },
          "lobbyName": "KBOT",  # Lobby name
          "lobbyPassword": None  # Lobby password (optional)
       },
       "isCustom": True  # Indicates it's a custom lobby
    }
    
    # Send the request to create the lobby
    return lockfile.authenticated_post(url, payload)

if __name__ == "__main__":
    pass  # No need to execute anything in this case
