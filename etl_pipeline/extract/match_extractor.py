

from etl_pipeline.api_utils.match_api import MatchIdAPI
from etl_pipeline.api_utils.match_api import MatchDetailAPI
from etl_pipeline.infra.kafka_client import MessageProducer
from etl_pipeline.infra.db_class import UserInfo



class MatchIdExtractor:
    
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
    
    def extract(self):
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

MatchIdExtractor().extract()
            