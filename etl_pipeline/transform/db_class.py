

from infra.mysql_client import mysql_cnx


class UserInfo:
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
    def __init__(self,data=list) -> None:
        # self.user_info= dict(zip(self.tables,data))
        self.user_info= tuple(data)
        self.cnx =  mysql_cnx()
        self.cursor = self.cnx.cursor()
        
    def insert(self):
        try:
            self.cursor.execute(self.sql,self.user_info)
            self.cnx.commit()
        except:
            pass