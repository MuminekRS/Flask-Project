import mariadb as sql
import sys

def set_up_connection():
    try:
        conn = sql.connect(
            user="prochnia",
            password="prochnia",
            host="3.86.146.90",
            port=3306,
            database="employess")
    except sql.Error as e:
        print(f"Not connected! Reason: {e}")
        sys.exit(1)
    try:
        cur = conn.cursor()
    except sql.Error as e:
        print(f"Curson can't be declare! Reason: {e}")
        sys.exit(1)
    except UnboundLocalError:
        print("Curson can't be declare because connection to DB failed")
        sys.exit(1)
    else:
        return conn,cur

def close_connection(conn,cur):
    cur.close()
    conn.close()

def add_data_to_DB(Table_name, date, value):
    conn, cur = set_up_connection()
    try:
        cur.execute(f"CREATE TABLE IF NOT EXISTS {Table_name} (ID INT AUTO_INCREMENT PRIMARY KEY, date VARCHAR(20) UNIQUE, value FLOAT);")
        cur.execute(
        f"INSERT INTO {Table_name} (date, value) VALUES (?,?)",
        (date, value))
    except sql.IntegrityError as e:
        print(f"Data can't be added to table '{Table_name}'! Reason: {e}")
    
    finally:
        conn.commit()
        close_connection(conn,cur)


def delete_table(Table_name):
    conn, cur = set_up_connection()
    try:
        cur.execute(f"DROP TABLE {Table_name};")
    except sql.OperationalError as e:
        print(f"Nie udało się gdyż: {e}")


def check_data_in_DB(name):
    conn, cur = set_up_connection()
    try:
        cur.execute(
            f"SELECT * FROM {name}"
        )
        for i in cur:
            print(i)
        cur.close()
        conn.close()
    except sql.ProgrammingError as e:
        print(f"Nie udało sie sprawdzić danych gdyż {e}")


def return_dict_for_chart(Table_name,range):
    conn, cur = set_up_connection()
    try:
        cur.execute(
            f"SELECT date,value FROM {Table_name} ORDER BY ID DESC LIMIT {range};"
        )
        dicto = {}
        for i in cur:
            a = i[0].split("-")
            date = tuple((int(i) -1) if a.index(i) ==1 else int(i) for i in a)
            dicto[date] = i[1]
        return dicto
                
    except sql.ProgrammingError as e:
        print(f"Nie udało sie sprawdzić danych gdyż {e}")
        close_connection(conn,cur)

def check_tables():
    conn, cur = set_up_connection()
    try:
        cur.execute(
        "SHOW TABLES"
                    )
        for i in cur:
            print(i)
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    # add_data_to_DB("Dolars", "2022-03-27", 4.13)
    # # delete_table("Dolars")
    # check_data_in_DB("GBP")
    # print(return_dict_for_chart("Dolars",5))
    check_tables()