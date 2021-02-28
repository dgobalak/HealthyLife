import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                   unix_socket=unix_socket, db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_health_data():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM health;')
        data = cursor.fetchall()
        if result > 0:
            got_data = jsonify(data)
        else:
            got_data = 'No Health Data in DB'
    conn.close()
    return got_data


def add_health_data(data):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO health (email, date, age, blood_pressure, heart_rate, body_temp, height, weight) VALUES("%s", "%s", %d, "%s", %d, %d, %f, %f)' % (data["email"], data["date"], data["age"], data["blood_pressure"], data["heart_rate"], data["body_temp"], data["height"], data["weight"]))
    conn.commit()
    conn.close()


def del_health_data(del_data):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM health WHERE email = "%s" AND date = "%s"' % (del_data["email"], del_data["date"]))
    conn.commit()
    conn.close()

