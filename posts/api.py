import json

from flask import request, Response, url_for
from jsonschema import validate, ValidationError

from . import models
from . import decorators
from posts import app
from .database import session

@app.route('/api/posts', methods=['GET'])
def get_posts():
    data = session.query(models.Post).order_by(models.Post.id)
    return Response(json.dumps([post.as_dict() for post in data]),
                    200, mimetype='application/json')
