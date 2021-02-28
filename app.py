from flask import Flask, render_template, request, redirect
import os
import requests
import json

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
# app.config.from_object('config')

# # Login required decorator.
# '''
# def login_required(test):
#     @wraps(test)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return test(*args, **kwargs)
#         else:
#             flash('You need to login first.')
#             return redirect(url_for('login'))
#     return wrap
# '''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/<item>')
def dashboard(item):
    data = requests.get('https://healthdata-305001.ue.r.appspot.com').json()
    labels = [data[i]['date'] for i in range(len(data))]
    values = [data[i][str(item)] for i in range(len(data))]
    print(values)
    return render_template('dashboard.html', values=values, labels=labels, label=str(item), items=data, item=get_field(str(item)))

@app.route('/planner')
def planner():
    return redirect('/planner/AM')


@app.route('/planner/<time>')
def med_planner(time):
    return render_template('medicine.html', time_conv=time)


@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/login')
def login():
    return render_template('signin.html')


@app.route('/register')
def register():
    # form = RegisterForm(request.form)
    return render_template('signup.html')


def get_field(item):
    if item == 'heart_rate':
        field = "Heart Rate"
    elif item == 'blood_pressure':
        field = "Blood Pressure"
    elif item == "body_temp":
        field = "Body Temperature"
    else:
        field = item.capitalize()
    return field


# Error handlers.

@app.errorhandler(500)
def internal_error(error):
    # db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
