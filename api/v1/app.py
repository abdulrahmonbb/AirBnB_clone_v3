#!/usr/bin/python3
"""
Starts a flask web application
"""
import os
from flask import Flask, Blueprint, jsonify, make_response
from api.v1.views import app_views
from models import storage
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown_appcontext(code):
    """
    teardown_appcontext
    """
    storage.close()


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
        port=int(os.getenv('HBNB_API_PORT', '5000'))
    )