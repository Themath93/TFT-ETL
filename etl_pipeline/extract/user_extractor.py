import time
import json


from api_utils.user_api import UserAPI
from api_utils.high_user_api import HighUserAPI
from api_utils.match_api import MatchIdAPI, MatchDetailAPI
from infra.kafka_client import MessageProducer


class UserExtractor:
    """
    Extract under the master tier's user info.\n
    Data to Kafka Broker of your Topic.
    
    
    
    Parameters
    ----------
    kafka_topic : str default "tft-user-info"
        the value of kafka topic name. \n
         
    """
    
    divisions = ["I"*i for i in range(1,4)] + ["IV"]
    tiers = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND"]
    api_key = open("api_key.txt", "r").readline()
    
    def __init__(self,kafka_topic="tft-user-info") -> None:
        self.topic = kafka_topic
        self.kakfa_producer = MessageProducer(broker=["kafka:19092"],topic=self.topic)
        

    def extract(self):
        """
        Extract data from ROIT Games.\n
        data to kafka with JSON type
        """
        for division in self.divisions:
            for tier in self.tiers:
                p_num = 1
                while True :
                    time.sleep(0.1)
                    user_api = UserAPI(api_key=self.api_key,tier=tier,division=division,page=p_num)
                    p_num += 1
                    res_data = user_api.get_whole_data()
                    if res_data != []:
                        self.kakfa_producer.send_my(msg=res_data)
                    else :
                        p_num = 1
                        break
