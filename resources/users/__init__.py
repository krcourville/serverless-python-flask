import os

import boto3
from flask import Blueprint, jsonify, request

blp = Blueprint('users', __name__, url_prefix='/users')

USERS_TABLE = os.environ.get('USERS_TABLE', 'users-table-dev')
IS_OFFLINE = os.environ.get('IS_OFFLINE', False)

if IS_OFFLINE:
    client = boto3.client(
        'dynamodb',
        region_name='localhost',
        endpoint_url='http://localhost:8000'
    )
else:
    client = boto3.client('dynamodb')


@blp.route("/<string:user_id>")
def get_user(user_id):
    resp = client.get_item(
        TableName=USERS_TABLE,
        Key={
            'userId': {'S': user_id}
        }
    )
    item = resp.get('Item')
    if not item:
        return jsonify({'error': 'User does not exist'}), 404

    return jsonify({
        'userId': item.get('userId').get('S'),
        'name': item.get('name').get('S')
    })


@blp.route("", methods=["POST"])
def create_user():
    user_id = request.json.get('userId')
    name = request.json.get('name')
    if not user_id or not name:
        return jsonify({'error': 'Please provide userId and name'}), 400

    resp = client.put_item(
        TableName=USERS_TABLE,
        Item={
            'userId': {'S': user_id},
            'name': {'S': name}
        }
    )

    return jsonify({
        'userId': user_id,
        'name': name
    })