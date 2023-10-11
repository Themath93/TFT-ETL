
import json

from etl_pipeline.infra.kafka_client import Consumer
from etl_pipeline.infra.db_class import UserInfo


class UserTransformer:
    topic = "tft-user-info"
    groud_id = "UserTransformer-python"
    broker=["kafka:19092"]
    
    def __init__(self) -> None:
        self.kafka_cousumer = Consumer(
            broker=self.broker,
            group_id=self.groud_id,
            topic=self.topic
            ).consumer
        
    def transform(self):
        while True:
            for msg in self.kafka_cousumer:
                msg_list = json.loads(msg.value)
                for m in msg_list:
                    if type(m) == str :
                        print(m)
                        pass
                    else :
                        data = list(map(lambda e:1 if e == True else e,m.values()))
                        data = list(map(lambda e:0 if e == False else e,data))
                        UserInfo.insert(data=data)