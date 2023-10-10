

from api_utils.match_api import MatchIdAPI
from api_utils.match_api import MatchDetailAPI
from infra.kafka_client import MessageProducer
from infra.db_class import UserInfo



class MatchIdExtractor:
    
    broker=["kafka:19092"]
    topic="match-id"
    with open("api_key.txt", "r") as f:
        api_key = f.readline()
    def __init__(self,tier="all") -> None:
        self.kafka_producer = kafka_producer = MessageProducer(broker=self.broker,topic=self.topic)
        self.user_info = UserInfo().get_puuid_list(tier)
        self.puuids = list(map(lambda e: e[0],self.user_info))
    
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
            