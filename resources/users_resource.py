import os

import boto3
from flask import Blueprint, jsonify, request
from injector import inject
from werkzeug.exceptions import abort

from infrastructure.repositories.UserRepository import UserRepository

blp = Blueprint('users', __name__, url_prefix='/users')

# USERS_TABLE = os.environ.get('USERS_TABLE', 'users-table-dev')
# IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
#
# if IS_OFFLINE:
#     client = boto3.client(
#         'dynamodb',
#         region_name='localhost',
#         endpoint_url='http://localhost:8000'
#     )
# else:
#     client = boto3.client('dynamodb')

# user_repository = UserRepository()


@inject
@blp.route("/<string:user_id>")
def get_user(user_id, user_repository: UserRepository):

    user = user_repository.get(user_id)

    if user:
        return jsonify(user)

    return abort(404)

    # resp = client.get_item(
    #     TableName=USERS_TABLE,
    #     Key={
    #         'userId': {'S': user_id}
    #     }
    # )
    # item = resp.get('Item')
    # if not item:
    #     return jsonify({'error': 'User does not exist'}), 404
    #
    # return jsonify({
    #     'userId': item.get('userId').get('S'),
    #     'name': item.get('name').get('S')
    # })

@inject
@blp.route("", methods=["POST"])
def create_user(user_repository: UserRepository):

    json = request.json
    user_repository.add(json)
    return jsonify(json)

    # user_id = request.json.get('userId')
    # name = request.json.get('name')
    # if not user_id or not name:
    #     return jsonify({'error': 'Please provide userId and name'}), 400
    #
    # resp = client.put_item(
    #     TableName=USERS_TABLE,
    #     Item={
    #         'userId': {'S': user_id},
    #         'name': {'S': name}
    #     }
    # )
    #
    # return jsonify({
    #     'userId': user_id,
    #     'name': name
    # })