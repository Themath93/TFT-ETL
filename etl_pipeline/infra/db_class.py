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
    
    def get_cols(self) -> list:
        return self.columns
    
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
        
    def get_cols(self) -> list:
        return self.columns
        
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
        
    def get_cols(self) -> list:
        return self.columns
    
    def insert(self,data=list):
        try:
            data= tuple(data)
            self.cursor.execute(self.sql,data)
            self.cnx.commit()
        except:
            pass

class Aguments:
    """
    Mysql Table "AGUMENTS" class
    
    
    """

    table_name = "AGUMENTS"
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
    
    def get_cols(self) -> list:
        return self.columns
        
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
    
    def get_cols(self) -> list:
        return self.columns
        
    def insert(self,data=list):
        try:
            data= tuple(data)
            self.cursor.execute(self.sql,data)
            self.cnx.commit()
        except:
            pass
        
class MatchInfo:
    """
    Mysql Table "MATCH_INFO" class
    
    
    """

    table_name = "MATCH_INFO"
    columns = [
        "match_id", "data_version", "participants",
        "game_datetime", "game_length", "game_version"
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
        
    def get_cols(self) -> list:
        return self.columns
        
    def insert(self,data=list):
        try:
            data= tuple(data)
            self.cursor.execute(self.sql,data)
            self.cnx.commit()
        except:
            pass
        
class MatchDetail:
    """
    Mysql Table "MATCH_DETAIL" class
    
    
    """

    table_name = "MATCH_DETAIL"
    columns = [
        "puuid", "match_id", "augments",
        "companion", "gold_left", "last_round",
        "level" , "placement", "players_eliminated",
        "time_eliminated", "total_damage_to_players"
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
        
    def get_cols(self) -> list:
        return self.columns
        
    def insert(self,data=list):
        try:
            data= tuple(data)
            self.cursor.execute(self.sql,data)
            self.cnx.commit()
        except:
            pass
        
class TraitsDetail:
    """
    Mysql Table "TRAITS_DETAIL" class
    
    
    """

    table_name = "TRAITS_DETAIL"
    columns = [
        "puuid", "match_id", "name", 
        "num_units", "style", "tier_current",
        "tier_total"
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
        
    def get_cols(self) -> list:
        return self.columns
        
    def insert(self,data=list):
        try:
            data= tuple(data)
            self.cursor.execute(self.sql,data)
            self.cnx.commit()
        except:
            pass        

class UnitsDetail:
    """
    Mysql Table "UNITS_DETAIL" class
    
    
    """

    table_name = "UNITS_DETAIL"
    columns = [
        "puuid", "match_id", "charactor_id", 
        "item_names", "name", "rarity",
        "tier" 
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
        
    def get_cols(self) -> list:
        return self.columns
        
    def insert(self,data=list):
        try:
            data= tuple(data)
            self.cursor.execute(self.sql,data)
            self.cnx.commit()
        except:
            pass