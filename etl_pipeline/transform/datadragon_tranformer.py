import json

from etl_pipeline.api_utils.api_util import get_latest_version
from etl_pipeline.infra.hdfs_client import get_client
from etl_pipeline.infra.mysql_client import mysql_cnx
from etl_pipeline.infra.db_class import Champions,Items,Traits,Aguments



class DataDragonTransformer:
    fnames= ['arguments', 'champions', 'items', 'traits']
    table_list = [Aguments, Champions, Items, Traits]
    cur_version = get_latest_version()
    base_path= f"/data_dragon/{cur_version}/"
    
    def __init__(self) -> None:
        self.hdfs_object = get_client()
        self.table_dict = dict(zip(self.fnames,self.table_list))
        
        
    def transform(self):

        for fname, table_obj in self.table_dict.items():
            with self.hdfs_object.read(self.base_path+fname,encoding="utf-8") as r :
                tmp = json.load(r)
            
            data_rows = tmp["data"].values()
            for row_dict in data_rows:
                row_values = list(row_dict.values())
                row_values.insert(0,self.cur_version)
                row_values[-1] = json.dumps(row_values[-1],ensure_ascii=False)
                table_obj().insert(data=row_values)