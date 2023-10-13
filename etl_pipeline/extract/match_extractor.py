
from etl_pipeline.api_utils.match_api import MatchIdAPI
from etl_pipeline.api_utils.match_api import MatchDetailAPI
from etl_pipeline.infra.kafka_client import MessageProducer
from etl_pipeline.infra.db_class import UserInfo



class MatchIdExtractor:
    """
    Match Id Extractor from Roit API
    
    Parameters
    ----------
    tier : str default  "all"
        TFT Rank 
        example : "BRONE", "SILVER" ...
        if "all" it will extract all match_id in ["IRON", "BRONZE", "SILVER", "PLATINUM", "DIAMOND"]
    end_time : int default 1624244400 2021-06-21
        Extract time cutting line
    
    """
    broker=["kafka:19092"]
    topic="match-id"
    base_path = "/home/worker/tft-app/etl_pipeline/"
    with open(f"{base_path}api_key.txt", "r") as f:
        api_key = f.readline()
    def __init__(self,tier="all",end_time=1624244400) -> None:
        self.kafka_producer = MessageProducer(broker=self.broker,topic=self.topic)
        self.user_info = UserInfo().get_puuid_list(tier)
        self.puuids = list(map(lambda e: e[0],self.user_info))
        self.end_time=end_time
    
    def extract(self) -> None:
        """
        Match_id Extract with puuids. 
        and send kafka broker datas that JSON typed.
        
        """
        for puuid in self.puuids:
            match_api = MatchIdAPI(
                api_key= self.api_key,
                puuid= puuid,
                count= 500
                )
            match_ids = match_api.get_match_ids()
            msg = {
                "data":match_ids
            }
            self.kafka_producer.send_my(msg=msg)
            