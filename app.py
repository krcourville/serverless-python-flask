# app.py

from flask import Flask

from resources.root import blp as root_resource
from resources.users import blp as users_resource

app = Flask(__name__)
app.register_blueprint(root_resource)
app.register_blueprint(users_resource)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
