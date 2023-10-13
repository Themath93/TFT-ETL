import os
import sys


from etl_pipeline.extract.datadragon_extractor import DataDragonExtractor
from etl_pipeline.transform.match_transformer import MatchTransfomer

def main():
    """ Main entry point of the app """
    works = {
        "extract":{
            "data_dragon":DataDragonExtractor("all").extract
        },
        "transform":{
            "data_dragon":None,
            "match_detail": MatchTransfomer().transform
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