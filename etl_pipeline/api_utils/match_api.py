import json
import requests
import time

class MatchIdAPI:
    
    
    current_time = int(time.time())
    two_hour_before = current_time - 3600
    
    def __init__(self,api_key=str,puuid=str,start_time=two_hour_before,end_time=current_time,count=20) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.api_key = api_key
        self.puuid = puuid
        self.count = count
        url = f"https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{self.puuid}/ids?start=0&startTime={self.start_time}&endTime={self.end_time}&count={self.count}&api_key={self.api_key}"
        self.res = requests.get(url=url).text[1:-1].replace('"',"").split(",")
    
    def get_match_id_list(self):
        return self.res
    
    
class MatchDetailExtractor:
    
    def __init__(self,api_key=str) -> None:
        self.url = "https://asia.api.riotgames.com/tft/match/v1/matches/"
        self.api_key = "?api_key="+api_key
    
    def get_match_detail(self,match_id=str):
        url = self.url + match_id + self.api_key
        res = requests.get(url=url).text
        return json.loads(res)
    
    def get_match_details(self,match_id=list):
        pass