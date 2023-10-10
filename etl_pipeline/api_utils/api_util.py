import json
import requests

import redis

from infra.redis_client import RedisAPILimitCounter

def get_latest_version() -> str:
    """
    returns latest version of TFT
    
    Returns  str
        example : '13.19.1' 
    
    """
    version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    version_res = requests.get(url=version_url)
    latest_version = json.loads(version_res.text)[0]
    return latest_version

def limit_counter() -> None:
    """
    RIOT API limit Controller
    In production level api limit is 100 in 2 minutes.\n
    this module used for avoid api reqeusts limit.
    """
    
    redis_txt = open("redis.txt","r").readline()
    redis_info = redis_txt.split(",")
    conn_redis = redis.Redis(host="redis",password=redis_info[0])
    limit_counter = RedisAPILimitCounter(conn_redis=conn_redis,key=redis_info[1])
    limit_counter.plus()