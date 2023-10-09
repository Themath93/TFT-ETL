
import requests
import json
import time

from api_utils.api_util import limit_counter

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
        summoner_ids = list(map(lambda e: e["summonerId"],res_json))
        
        result = []
        for summoner_id in summoner_ids:
            url = f"https://kr.api.riotgames.com/tft/league/v1/entries/by-summoner/{summoner_id}?api_key={self.api_key}"
            limit_counter()
            entries_res = requests.get(url=url).text.replace("\n","").replace("[","").replace("]","")
            dict_res = json.loads(entries_res)
            result.append(dict_res)
            time.sleep(0.5)
        return result