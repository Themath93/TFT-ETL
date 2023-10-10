"""
MySQL Database Class

list
----
UserInfo : USER_INFO
    TFT user's informations


"""

from infra.mysql_client import mysql_cnx


class UserInfo:
    """
    Mysql Table "USER_INFO" class
    
    
    """
    tables = [
        'puuid', 'leagueid', 'queuetype',
        'tier', 'division', 'summonerid',
        'summonername', 'leaguepoints', 'wins',
        'losses', 'veteran', 'inactive',
        'freshblood', 'hotstreak'
    ]
    tables_str = ", ".join(tables)
    form_str= ", ".join(["%s"]*len(tables))
    sql = f""" 
        INSERT INTO USER_INFO \n
        ({tables_str}) \n
        VALUES ({form_str})
    """
    def __init__(self) -> None:
        # self.user_info= dict(zip(self.tables,data))
        self.cnx =  mysql_cnx()
        self.cursor = self.cnx.cursor()
        
    def insert(self,data=list):
        try:
            user_info= tuple(data)
            self.cursor.execute(self.sql,user_info)
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