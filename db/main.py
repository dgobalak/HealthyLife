from flask import Flask, jsonify, request
from db import *


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET', 'DELETE'])
def dashboard():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400  

        add_health_data(request.get_json())
        return 'Data Added'

    if request.method == 'DELETE':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400 
        del_health_data(request.get_json())
        return 'Data Deleted'
    
    return get_health_data()


@app.route('/planner', methods=['POST', 'GET', 'DELETE'])
def dashboard():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400  

        add_health_data(request.get_json())
        return 'Data Added'

    if request.method == 'DELETE':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400 
        del_health_data(request.get_json())
        return 'Data Deleted'
    
    return get_health_data()

if __name__ == '__main__':
    app.run()