
import json
import time
import os

from etl_pipeline.infra.kafka_client import Consumer
from etl_pipeline.infra.db_class import MatchInfo, MatchDetail, TraitsDetail, UnitsDetail
from etl_pipeline.api_utils.match_api import MatchDetailAPI

class MatchTransfomer:
    """
    TFT Each Match Transformer
    """
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
        """
        
        """
        
        ## Kafka cousuming 
        while True:
            for msg in self.kafka_cousumer:
                msg_list = json.loads(msg.value)
                match_ids = msg_list['data']
                
                if type(match_ids) == list:
                    match_details = self.match_detail_api.get_match_details(match_ids=match_ids)
                    try:
                        match_list = match_details["match_details"]
                    except:
                        print(match_details)
                    
                     
                    
                    for game_detail in match_list:
                        
                        start= time.time() # measure time to transforming each match
                        
                        # match_info
                        match_id = game_detail["metadata"]["match_id"]
                        data_version = game_detail["metadata"]["data_version"]
                        participants = json.dumps(game_detail["metadata"]["participants"],ensure_ascii=False)
                        game_datetime = game_detail["info"]["game_datetime"]
                        game_length = game_detail["info"]["game_length"]
                        game_version = game_detail["info"]["game_version"]
                        match_info = [
                            match_id, data_version, participants,
                            game_datetime, game_length, game_version
                        ]
                        MatchInfo().insert(data=match_info)
                        
                        # match_detail
                        participants_list = game_detail["info"]["participants"]
                        
                        # each_participant loop
                        for participant in participants_list:
                            puuid = participant["puuid"]
                            augments = json.dumps(participant["augments"],ensure_ascii=False)
                            companion = json.dumps(participant["companion"],ensure_ascii=False)
                            gold_left = participant["gold_left"]
                            last_round = participant["last_round"]
                            level = participant["level"]
                            placement = participant["placement"]
                            players_eliminated = participant["players_eliminated"]
                            time_eliminated = participant["time_eliminated"]
                            total_damage_to_players = participant["total_damage_to_players"]

                            match_detail = [
                                puuid, match_id, augments,
                                companion, gold_left, last_round,
                                level, placement, players_eliminated,
                                time_eliminated, total_damage_to_players
                            ]
                            MatchDetail().insert(data=match_detail)
                            
                            
                            # each_trait loop
                            
                            traits_list = participant["traits"]
                            units_list = participant["units"]
                            for trait in traits_list:
                                name = trait["name"]
                                num_units = trait["num_units"]
                                style =trait["style"]
                                tier_current = trait["tier_current"]
                                tier_total = trait["tier_total"]

                                traits_detail = [
                                    puuid, match_id, name,
                                    num_units, style, tier_current,
                                    tier_total
                                ]
                                TraitsDetail().insert(data=traits_detail)
                            
                            
                                # units_detail
                                # each_unit loop
                            for unit in units_list:
                                charactor_id = unit["character_id"]
                                item_names = json.dumps(unit["itemNames"],ensure_ascii=False)
                                units_name = unit["name"]
                                rarity = unit["rarity"]
                                tier = unit["tier"]

                                units_detail = [
                                    puuid, match_id, charactor_id,
                                    item_names, units_name, rarity,
                                    tier
                                ]
                                UnitsDetail().insert(data=units_detail)
                                
                                takes_time = round(time.time()-start,2)
                                os.system(f'echo "Taks {takes_time} seconds for transfoming each MATCH DEATIL"')