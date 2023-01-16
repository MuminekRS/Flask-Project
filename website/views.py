from flask import Blueprint, Markup, render_template, request
views = Blueprint('views', __name__)
from modules.connect_to_MariaDB import *


chart = "USD"
rangee = "5"
print(chart)

@views.route('/', methods=['GET','POST'])
def home():
    global chart 
    global rangee
    if request.method == 'POST':
        if "chart_button" in request.form:
            chart = request.form['chart_button']
            return render_template('home.html', values=return_dict_for_chart(Table_name=chart, range=rangee), currency=chart)
        if "range_days" in request.form:
            print(request.form)
            rangee = int(request.form['range_days'])
            return render_template('home.html', values=return_dict_for_chart(Table_name=chart, range=rangee), currency=chart)
    return render_template('home.html', values=return_dict_for_chart(Table_name=chart, range=rangee), currency=chart)



