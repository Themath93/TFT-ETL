import json
import requests


from etl_pipeline.api_utils.api_util import get_latest_version

class DataDragonAPI:
    """
    returns TFT's base information
    
    Parameters
    ---------
    version : str, default latest_version
        the value of TFT version. 
    asset : str,
        the value of Data Dragon Data & Assets.
        only choose one of list below. \n
        ["arena_mode", "arguments", "champions",\n
        "items", "queues", "regalia", "tacticians", "traits"]
        
        More information https://developer.riotgames.com/docs/lol#data-dragon_versions
    
    """
    assets_list = [
        "arena_mode", "arguments", "champions",
        "items", "queues", "regalia",
        "tacticians","traits"
        ]
    assets_arguments = [
        "tft-arena.json", "tft-augments.json", "tft-champion.json",
        "tft-item.json", "tft-queues.json", "tft-regalia.json",
        "tft-tactician.json", "tft-trait.json"]
    
    def __init__(self,version=get_latest_version(),asset=str) -> None:
        
        if asset not in self.assets_list:
            raise Exception(f"아래 assets 리스트중 하나에서만 골라주세요. \n assets 리스트 : {self.assets_list}")
        
        asset_idx = self.assets_list.index(asset)
        asset_arg = self.assets_arguments[asset_idx]
        self.version = version
        self.asset = asset_arg
        self.url = f"http://ddragon.leagueoflegends.com/cdn/{self.version}/data/ko_KR/{self.asset}"
        
    def get_data(self) -> dict :
        """
        returns arena mode information 
        
        Retruns dict
        
        """
        res_text = requests.get(url=self.url).text
        json_res = json.loads(res_text)
        return json_res
            


