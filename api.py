
from flask import Flask, jsonify, request
from flask_cors import CORS

from databases import MongoDatabase
from users import User

app = Flask(__name__)
CORS(app)

DB = MongoDatabase()

#
# TODO: Validate user is authenticated (careful with CORS, and CSRF)
#


@app.route('/assets/time-series', methods=['GET'])
def assets_time_series():
    user_id = request.args['user_id']
    resp = {'success': True, 'message': ''}
    resp['data'] = User(db=DB, user_id=user_id).assets_time_series()
    return jsonify(resp)


# @app.route('/assets/time-series/aggregated', methods=['GET'])
# def assets_time_series():
#     user_id = request.args['user_id']
#     resp = {'success': True, 'message': ''}
#     resp['data'] = User(db=DB, user_id=user_id).assets_time_series()
#     return jsonify(resp)


# @app.route('/assets/time-series/aggregated/last', methods=['GET'])
# def assets_time_series():
#     user_id = request.args['user_id']
#     resp = {'success': True, 'message': ''}
#     resp['data'] = User(db=DB, user_id=user_id).assets_time_series()
#     return jsonify(resp)


# @app.route('/assets/time-series/disaggregated', methods=['GET'])
# def assets_time_series():
#     user_id = request.args['user_id']
#     resp = {'success': True, 'message': ''}
#     resp['data'] = User(db=DB, user_id=user_id).assets_time_series()
#     return jsonify(resp)


# @app.route('/assets/time-series/disaggregated/last', methods=['GET'])
# def assets_time_series():
#     user_id = request.args['user_id']
#     resp = {'success': True, 'message': ''}
#     resp['data'] = User(db=DB, user_id=user_id).assets_time_series()
#     return jsonify(resp)


# @app.route('/assets/overview', methods=['GET'])
# def assets_current_status():
#     user_id = request.args['user_id']
#     resp = {'success': True, 'message': ''}
#     resp['data'] = User(db=DB, user_id=user_id).assets_current_status()
#     return jsonify(resp)


# @app.route('/assets/balances', methods=['GET'])
# def assets_balances():
#     user_id = request.args['user_id']
#     resp = {'success': True, 'message': ''}
#     resp['data'] = User(db=DB, user_id=user_id).assets_balances()
#     return jsonify(resp)
