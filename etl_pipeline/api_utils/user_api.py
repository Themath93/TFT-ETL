import json
import requests



from etl_pipeline.api_utils.api_util import limit_counter

class UserAPI:
    """
    Roit Games TFT(TeamFigth Tactics) Users Infomations Extractor
    
    
    Parameters
    ----------
    api_key : str
            the value of api_key or token which is generated from RIOT GAMES API (https://developer.riotgames.com)
    tier : str
            tier
            example : "BRONE", "SILVER" ...
    division : str
            division string
            only use one of ['I', 'II', 'III', 'IV']
    """
    
    def __init__(self,api_key=str,tier=str,division=str,page=int) -> None:
        
        self.api_key = api_key
        self.tier = tier
        self.division = division
        url = f"https://kr.api.riotgames.com/tft/league/v1/entries/{self.tier}/{self.division}?page={str(page)}&api_key={self.api_key}"
        limit_counter()
        self.res_json = json.loads(requests.get(url).text)
        
    def get_whole_data(self) -> dict:
        """
        returns User information
        
        
        Returns dict
        ------------
        
        
        """
        return self.res_json

    def puuids(self) -> list:
        """
        returns puuids list
        
        Returns list
        ------------
        """
        return list(map(lambda e: e["puuid"],self.res_json))

    def summoner_ids(self) -> list:
        """
        returns summonerId list
        
        Returns list
        ------------
        """
        return list(map(lambda e: e["summonerId"],self.res_json))
    

    def summoner_names(self) -> list:
        """
        returns summonerName list
        
        Returns list
        ------------
        """
        return list(map(lambda e: e["summonerName"],self.res_json))
    def total_games_qty(self) -> dict:
        """
        returns list about each users total qty of games
        
        Returns dict
        """
        wins = list(map(lambda e: e["wins"],self.res_json))
        loses = list(map(lambda e: e["losses"],self.res_json))
        zipped = list(zip(wins,loses))
        total_games = list(map(sum,zipped))
        puuids = list(map(lambda e: e["puuid"],self.res_json))
        
        return dict(zip(puuids,total_games))