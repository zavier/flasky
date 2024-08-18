from flask import jsonify

from . import api

@api.route('/users/')
def get_users():
    users = [{'name':'zhangsan', 'age': 20},{'name':'wangwu', 'age': 26}]
    return jsonify(users)