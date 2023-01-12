from flask import Blueprint, Markup, render_template, request
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
        data = dict((key,value) for key, value in cur)

        return dict(((date.replace("-",","),),value) for date, value in data.items())

    except mariadb.ProgrammingError as e:
        print(f"Nie udało sie sprawdzić danych gdyż {e}")
        close_connection(conn,cur)

    

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")




@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    errors = {}
    if request.method == 'POST':
        if not request.form['firstName'].isalpha():
            errors['firstName'] = ["Username should start with an alphabet"]
        if request.form['password1'] != request.form['password2']:
            errors['password2']  = ["Password and Confirm Password should be the same"]
        else:
            add_data_to_DB(request.form.get('firstName').capitalize(), request.form.get('password1'), request.form.get('email'))

    return render_template("sign_up.html", errors=errors)





@auth.route('/logout')
def logout():
    return render_template("login.html")

@auth.route('/sample')
def sample():
    return render_template("sample.html")

