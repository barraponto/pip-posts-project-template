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

@app.route('/api/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = session.query(models.Post).get(id)

    if post:
        data = json.dumps(post.as_dict())
        return Response(data, 200, mimetype='application/json')
    else:
        message = 'Could not find post with id {}'.format(id)
        data = json.dumps({'message': message})
        return Response(data, 404, mimetype='application/json')
