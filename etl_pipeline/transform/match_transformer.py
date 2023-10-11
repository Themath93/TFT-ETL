
import json

from etl_pipeline.infra.kafka_client import Consumer
# from etl_pipeline.infra.db_class
from etl_pipeline.api_utils.match_api import MatchDetailAPI

class MatchTransfomer:
    topic = "match-id"
    groud_id = "MatchTransformer-python"
    broker=["kafka:19092"]
    
    base_path = "/home/worker/tft-app/etl_pipeline/"
    with open(f"{base_path}api_key.txt", "r") as f:
        api_key = f.readline()
    
    def __init__(self) -> None:
        self.kafka_cousumer = Consumer(
            broker=self.broker,
            group_id=self.groud_id,
            topic=self.topic
            ).consumer
        self.match_detail_api = MatchDetailAPI(api_key=self.api_key)
        
    def transform(self):
        
        ## Kafka cousuming 
        while True:
            for msg in self.kafka_cousumer:
                msg_list = json.loads(msg.value)
                match_ids = msg_list['data']
                print("1")
                if type(match_ids) == list:
                    match_details = self.match_detail_api.get_match_details(match_ids=match_ids)

                    print(match_details)
            
            
MatchTransfomer().transform()