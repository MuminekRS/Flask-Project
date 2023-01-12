from flask import Blueprint, Markup, render_template
views = Blueprint('views', __name__)


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

def close_connection(conn,cur):
    cur.close()
    conn.close()

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

def return_dict_for_chart(Table_name,range):
    conn, cur = set_up_connection()
    try:
        cur.execute(
            f"SELECT date,value FROM {Table_name} ORDER BY ID DESC LIMIT {range};"
        )
        # data = dict((key,value) for key, value in cur)
        dicto = {}
        for i in cur:
            a = i[0].split("-")
            date = tuple((int(i) -1) if a.index(i) ==1 else int(i) for i in a)
            dicto[date] = i[1]
        return dicto
    except mariadb.ProgrammingError as e:
        print(f"Nie udało sie sprawdzić danych gdyż {e}")
        close_connection(conn,cur)


@views.route('/')
def home():
    return render_template('home.html', values=return_dict_for_chart("Dolars",18))




