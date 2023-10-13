
import requests
import json
import time

from etl_pipeline.api_utils.api_util import limit_counter


class HighUserAPI:
    
    
    def __init__(self,api_key=str) -> None:
        self.api_key = api_key
        self.url = f"https://kr.api.riotgames.com/tft/league/v1/grandmaster?api_key={self.api_key}"
        
    def get_whole_data(self) -> list:
        
        
        result = self.__extract_user_datas()
        
        return result

    def __extract_user_datas(self):
        
        limit_counter()
        res = requests.get(url=self.url).text
        res_json = json.loads(res)
        
        try: 
            entires = res_json["entries"]
            summoner_ids = list(map(lambda e: e["summonerId"],entires))
        
        except:
            return
        
        result = []
        for summoner_id in summoner_ids:
            url = f"https://kr.api.riotgames.com/tft/league/v1/entries/by-summoner/{summoner_id}?api_key={self.api_key}"
            limit_counter()
            res_text = requests.get(url=url).text
            user_info_data = json.loads(res_text)[0]
            result.append(user_info_data)

            time.sleep(0.05)
        return result