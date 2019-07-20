from flask import Blueprint

blp = Blueprint('root', __name__)


@blp.route('/')
def hello():
    return "Hello World!"
