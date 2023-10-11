"""
MySQL Database Class

list
----
UserInfo : USER_INFO
    TFT user's informations


"""

from etl_pipeline.infra.mysql_client import mysql_cnx


class UserInfo:
    """
    Mysql Table "USER_INFO" class
    
    
    """
    table_name = "USER_INFO"
    columns = [
        'puuid', 'leagueid', 'queuetype',
        'tier', 'division', 'summonerid',
        'summonername', 'leaguepoints', 'wins',
        'losses', 'veteran', 'inactive',
        'freshblood', 'hotstreak'
    ]
    column_str = ", ".join(columns)
    form_str= ", ".join(["%s"]*len(columns))
    sql = f""" 
        INSERT INTO {table_name} \n
        ({column_str}) \n
        VALUES ({form_str})
    """
    def __init__(self) -> None:
        # self.user_info= dict(zip(self.tables,data))
        self.cnx =  mysql_cnx()
        self.cursor = self.cnx.cursor()
        
    def insert(self,data=list):
        try:
            data= tuple(data)
            self.cursor.execute(self.sql,data)
            self.cnx.commit()
        except:
            pass
    
    def get_puuid_list(self,tier="all"):
        
        tiers = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND"]
        
        if tier == "all":
            sql = "SELECT puuid FROM USER_INFO;"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
            
        else: 
            if tier in tiers:
                sql = f"""
                    SELECT puuid \n
                    FROM USER_INFO \n
                    WHERE TIER = (%s, )
                """
                self.cursor.execute(sql,tuple(tier))
                return self.cursor
            
class Traits:
    """
    Mysql Table "TRAITS" class
    
    
    """

    table_name = "TRAITS"
    columns = [
        "version", "code_id", 
        "name", "image"
    ] 
    column_str = ", ".join(columns)
    form_str= ", ".join(["%s"]*len(columns))
    sql = f""" 
        INSERT INTO {table_name} \n
        ({column_str}) \n
        VALUES ({form_str})
    """
    def __init__(self) -> None:
        self.cnx =  mysql_cnx()
        self.cursor = self.cnx.cursor()
        
    def insert(self,data=list):
        try:
            data= tuple(data)
            self.cursor.execute(self.sql,data)
            self.cnx.commit()
        except:
            pass


class Champions:
    """
    Mysql Table "CHAMPIONS" class
    
    
    """

    table_name = "CHAMPIONS"
    columns = [
        "version", "code_id",
        "name", "tier", "image"
    ] 
    column_str = ", ".join(columns)
    form_str= ", ".join(["%s"]*len(columns))
    sql = f""" 
        INSERT INTO {table_name} \n
        ({column_str}) \n
        VALUES ({form_str})
    """
    def __init__(self) -> None:
        self.cnx =  mysql_cnx()
        self.cursor = self.cnx.cursor()
        
    def insert(self,data=list):
        try:
            data= tuple(data)
            self.cursor.execute(self.sql,data)
            self.cnx.commit()
        except:
            pass

class Arguments:
    """
    Mysql Table "ARGUMENTS" class
    
    
    """

    table_name = "ARGUMENTS"
    columns = [
        "version", "code_id",
        "name", "image"
    ] 
    column_str = ", ".join(columns)
    form_str= ", ".join(["%s"]*len(columns))
    sql = f""" 
        INSERT INTO {table_name} \n
        ({column_str}) \n
        VALUES ({form_str})
    """
    def __init__(self) -> None:
        self.cnx =  mysql_cnx()
        self.cursor = self.cnx.cursor()
        
    def insert(self,data=list):
        try:
            data= tuple(data)
            self.cursor.execute(self.sql,data)
            self.cnx.commit()
        except:
            pass


class Items:
    """
    Mysql Table "ITEMS" class
    
    
    """

    table_name = "ITEMS"
    columns = [
        "version", "code_id",
        "name", "image"
    ] 
    column_str = ", ".join(columns)
    form_str= ", ".join(["%s"]*len(columns))
    sql = f""" 
        INSERT INTO {table_name} \n
        ({column_str}) \n
        VALUES ({form_str})
    """
    def __init__(self) -> None:
        self.cnx =  mysql_cnx()
        self.cursor = self.cnx.cursor()
        
    def insert(self,data=list):
        try:
            data= tuple(data)
            self.cursor.execute(self.sql,data)
            self.cnx.commit()
        except:
            pass