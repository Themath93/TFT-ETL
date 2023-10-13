import time
import json


from etl_pipeline.api_utils.user_api import UserAPI
from etl_pipeline.api_utils.high_user_api import HighUserAPI
from etl_pipeline.infra.kafka_client import MessageProducer


class UserExtractor:
    """
    Extract under the master tier's user info.\n
    Data to Kafka Broker of your Topic.
    
    
    
    Parameters
    ----------
    kafka_topic : str default "tft-user-info"
        the value of kafka topic name. \n
    user_tier : str default "low"
        choose which tier you want to extract.\n
        if "low" extract list of ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND"].
        if "high" extract high tier users
    """
    
    divisions = ["I"*i for i in range(1,4)] + ["IV"]
    tiers = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND"]
    base_path = "/home/worker/tft-app/etl_pipeline/"
    api_key = open(f"{base_path}api_key.txt", "r").readline()
    
    def __init__(self,kafka_topic="tft-high-user",user_tier="low") -> None:
        self.topic = kafka_topic
        self.kakfa_producer = MessageProducer(broker=["kafka:19092"],topic=self.topic)
        self.user_tier = user_tier
        

    def extract(self):
        """
        Extract data from ROIT Games.\n
        data to kafka with JSON type
        """
        
        if self.user_tier == "high":
            high_user_api = HighUserAPI(api_key=self.api_key)
            res_datas = high_user_api.get_whole_data()
            for res_data in res_datas:
                if res_data != []:
                        self.kakfa_producer.send_my(msg=res_data)
            return
        
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
