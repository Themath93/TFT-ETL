import json
import requests
import time

from etl_pipeline.api_utils.api_util import limit_counter

class MatchIdAPI:
    """
    MatchId API about TFT games in Asia region by puuids
    
    Prameters
    ---------
    api_key : str
        the value of api_key or token which is generated from RIOT GAMES API (https://developer.riotgames.com)
    puuid : str
        the unique value of TFT SummonerId
    start_time : int default 1623801600 : June 16th, 2021
        Epoch timestamp in seconds.
        The matchlist started storing timestamps on June 16th, 2021.\n
        Any matches played before June 16th, 2021 won't be included in the results if the startTime filter is set.
    end_time : int default current time
        Epoch timestamp in seconds.
    count : int defalut 20
        Number of match ids to return.
    
    """
    current_time = int(time.time())
    from_the_first = 1623801600 # 2021-06-16
    
    def __init__(self,api_key=str,puuid=str,start_time=from_the_first,end_time=current_time,count=20) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.api_key = api_key
        self.puuid = puuid
        self.count = count
        url = f"https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{self.puuid}/ids?start=0&startTime={self.start_time}&endTime={self.end_time}&count={self.count}&api_key={self.api_key}"
        limit_counter()
        self.res = requests.get(url=url).text[1:-1].replace('"',"").split(",")
    
    def get_match_ids(self) -> list:
        """
        returns list of match ids
        """
        return self.res
    
    
class MatchDetailAPI:
    """
    MatchId API about TFT games in Asia region by puuids
    
    Prameters
    ---------
    api_key : str
        the value of api_key or token which is generated from RIOT GAMES API (https://developer.riotgames.com)
    """
    def __init__(self,api_key=str) -> None:
        self.url = "https://asia.api.riotgames.com/tft/match/v1/matches/"
        self.api_key = "?api_key="+api_key
    
    def get_match_detail(self,match_id=str) -> dict :
        """
        returns a match detail of your match_id
        
        
        Parameters
        ----------
        match_id : str
            the value of match_id
            example : "KR_660112314"
        """
        url = self.url + match_id + self.api_key
        limit_counter()
        res = requests.get(url=url).text
        return json.loads(res)
    
    def get_match_details(self,match_ids=list) -> dict:
        """
        returns count of match detail of your match_ids.\n
        count is number of match_ids length.
        But if your api_key is production level not a development level,\n
        your request limit is 200 in 2 minutes.\n
        See more https://developer.riotgames.com
        
        Returns : dict
        ----------
        
        Parameters
        ----------
        match_ids : list
            the list which contains about TFT match_id.\n
            example : ["KR_660112312", "KR_660112314", ...]
        
        """
        
        tmp = []
        for id in match_ids:
            url = self.url + id + self.api_key
            limit_counter()
            res = requests.get(url=url).text
            tmp.append(json.loads(res))
            time.sleep(0.05)
            
        result = {
            "match_ids": match_ids,
            "match_details": tmp
        }
        
        return result