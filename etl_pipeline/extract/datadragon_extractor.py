

import time
import json

from api_utils.datadragon_api import DataDragonAPI
from api_utils.api_util import get_latest_version
from infra.hdfs_client import get_client


class DataDragonExtractor:
    """
    returns TFT's base information
    
    Parameters
    ---------
    version : str, default latest_version
        the value of TFT version. 
    asset : str, "all"
        the value of Data Dragon Data & Assets.
        only choose one of list below. \n
        ["arena_mode", "arguments", "champions",\n
        "items", "queues", "regalia", "tacticians", "traits"]
        
        if asset == "all" then all asset will selected
        
        More information https://developer.riotgames.com/docs/lol#data-dragon_versions
    
    """
    assets_list = [
    "arena_mode", "arguments", "champions",
    "items", "queues", "regalia",
    "tacticians","traits"
    ]
    base_path = "data_dragon/"
    
    def __init__(self,asset=str,version=get_latest_version()) -> None:
        self.asset = asset
        self.version = version
        if self.asset != "all":
            self.data_dragon_api = DataDragonAPI(asset=self.asset,version=get_latest_version()).get_data
    
    
    def to_hdfs(self) -> None:
        """
        Save data to Hadoop HDFS
        """
        hdfs_client = get_client()
        if self.asset == "all" :
            for ass in self.assets_list:
                api_res = DataDragonAPI(asset=ass,version=self.version).get_data()
                path = f"/{self.base_path}/{self.version}/{ass}"
                data = json.dumps(api_res, ensure_ascii=False)
                hdfs_client.write(path,data=data,encoding="utf-8",overwrite=True)
                
        else :
            path = f"/{self.base_path}/{self.version}/{self.asset}"
            data = json.dumps(self.data_dragon_api(), ensure_ascii=False)
            hdfs_client.write(path,data=data,encoding="utf-8")