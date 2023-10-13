import os
import sys

## extract Moudules
from etl_pipeline.extract.datadragon_extractor import DataDragonExtractor
from etl_pipeline.extract.user_extractor import UserExtractor
from etl_pipeline.extract.match_extractor import MatchIdExtractor

from etl_pipeline.transform.match_transformer import MatchTransfomer
from etl_pipeline.transform.datadragon_tranformer import DataDragonTransformer
from etl_pipeline.transform.user_transformer import UserTransformer

def main():
    """ Main entry point of the app """
    works = {
        "extract":{
            "data_dragon":DataDragonExtractor("all").extract,
            "user_extract":UserExtractor(user_tier="low").extract,
            "high_user_extract":UserExtractor(user_tier="high").extract,
            "matctId_extract":MatchIdExtractor()
        },
        "transform":{
            "data_dragon":DataDragonTransformer().transform,
            "user_transform":UserTransformer().transform,
            "match_detail": MatchTransfomer().transform,
        }
    }
    return works
works = main()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    args = sys.argv
    
    if args[1] not in works.keys() :
        raise Exception("첫번째 전달인자가 이상함 >> " +str(works.keys()))
    if args[2] not in works[args[1]].keys() :
        raise Exception("두번째 전달인자가 이상함 >> " +str(works[args[1]].keys()))
    
    
    if len(args) == 3 :
        work = works[args[1]][args[2]]
        work()
    else :
        work = works[args[1]][args[2]]
        work(int(args[3]))