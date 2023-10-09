from user_extractor import UserExtractor
from match_extractor import MatchIdExtractor,MatchDetailExtractor
import time

divisions = ["I"*i for i in range(1,5)]
tiers = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND"]
api_key = open("../api_key.txt","r").readline()

api_res = UserExtractor(tier=tiers[-1],division=divisions[0],api_key=api_key,page=1)
# print(api_res.get_whole_data())

puuids = api_res.puuids()

week_before = int(time.time()) - 86400*7
month_before = int(time.time()) - 86400*30
year_before = int(time.time()) - 86400*365
tmp_puuid = "yO5Jh8WN48r_uH0abI-Cjknd_hpXXd9pK0tgAVRUaNd-TB7MPjDPMvXf2hOCU4k5W2L-sR3GqQnJhg"
match_res = MatchIdExtractor(api_key=api_key,puuid=tmp_puuid,start_time=year_before,count=2000)

match_res = match_res.get_match_id_list()

print(match_res[:10])

detail = MatchDetailExtractor(api_key=api_key)

test_detail = detail.get_match_detail(match_res[0])

print(test_detail)