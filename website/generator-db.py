import mariadb
import sys


def set_up_connection():
    try:
        conn = mariadb.connect(
            user="prochnia",
            password="prochnia",
            host="3.86.146.90",
            port=3306,
            database="employess")
    except mariadb.Error as e:
        print(f"Nie udało siebo : {e}")

    try:
        cur = conn.cursor()
    except:
        print(f"Nie można zestawić połączenia przez")
        sys.exit(1)

    return conn,cur

def add_data_to_DB(first_name, password, email):
    conn, cur = set_up_connection()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS `Persons` (ID INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(20), password VARCHAR(20), email VARCHAR(255) UNIQUE);")
        cur.execute(
        "INSERT INTO Persons (firstname, password, email) VALUES (?,?,?)",
        (first_name, password, email))
    except mariadb.IntegrityError as e:
        print(f"Nie można gdyż: {e}")
    
    finally:
        conn.commit()
        cur.close()
        conn.close()

