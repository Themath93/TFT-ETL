import json
import requests


def get_latest_version() -> str:
    """
    returns latest version of TFT
    
    Returns  str
        example : '13.19.1' 
    
    """
    version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    version_res = requests.get(url=version_url)
    latest_version = json.loads(version_res.text)[0]
    return latest_version
