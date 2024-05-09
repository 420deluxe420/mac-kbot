import requests
import lockfile

# Function to fetch information about all champion skins
def get_all_champion_skins():
    url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/skins.json"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch champion skins:", response.status_code)
        return None
    skins_data = response.json()

    champ_skins = {}
    for champ_id, skin_info in skins_data.items():
        champ_name = skin_info["loadScreenPath"].split("ASSETS/Characters/")[1].split("/")[0]
        if champ_name not in champ_skins:
            champ_skins[champ_name] = []
        if skin_info.get("isBase", False):
            champ_skins[champ_name].append({"id": champ_id, "name": "default"})
        elif skin_info.get("questSkinInfo"):
            for skin_tier in skin_info["questSkinInfo"]["tiers"]:
                champ_skins[champ_name].append({"id": skin_tier["id"], "name": skin_tier["name"]})
        else:
            champ_skins[champ_name].append({"id": champ_id, "name": skin_info["name"]})
    
    return champ_skins

# Function to change the background skin of the League of Legends client
def change_background_skin(value):
    port, password = lockfile.get_lockfile_info()
    if port is None or password is None:
        return {"error": "Lockfile not found."}
    url = f'https://127.0.0.1:{port}/lol-summoner/v1/current-summoner/summoner-profile/'
    headers = {'Content-Type': 'application/json'}
    data = {
        "key": "backgroundSkinId",
        "value": value,
        "regalia": "{\"bannerType\":2,\"crestType\":1,\"selectedPrestigeCrest\":1}"
    }
    response = lockfile.authenticated_post(url, data)
    return response

if __name__ == "__main__":
    pass  # No need to execute anything in this case
