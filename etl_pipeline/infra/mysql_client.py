
from mysql import connector
from mysql.connector import errorcode

def mysql_cnx() -> object:
    """
    returns mysql connetion object if connected.
    """
    with open("mysql.txt", "r") as f:
        mysql_info = f.readline().split(",")
    try:
        cnx = connector.connect(
            user= mysql_info[0],
            password = mysql_info[1],
            host= mysql_info[2],
            database= mysql_info[3],
        )
        
    except connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        return cnx