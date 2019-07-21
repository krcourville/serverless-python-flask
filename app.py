# app.py

from flask import Flask
from flask_injector import FlaskInjector

import providers
from resources.root_resource import blp as root_resource
from resources.users_resource import blp as users_resource

app = Flask(__name__)
app.register_blueprint(root_resource)
app.register_blueprint(users_resource)

FlaskInjector(app=app, modules=[providers.RepositoriesModule])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
