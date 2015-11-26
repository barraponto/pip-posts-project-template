import unittest
import os
import json
# try: from urllib.parse import urlparse
# except ImportError: from urlparse import urlparse # Python 2 compatibility

# Configure our app to use the testing databse
os.environ["CONFIG_PATH"] = "posts.config.TestingConfig"

from posts import app
from posts import models
from posts.database import Base, engine, session

class TestAPI(unittest.TestCase):
    """ Tests for the posts API """

    def setUp(self):
        """ Test setup """
        self.client = app.test_client()

        # Set up the tables in the database
        Base.metadata.create_all(engine)

    def tearDown(self):
        """ Test teardown """
        session.close()
        # Remove the tables and their data from the database
        Base.metadata.drop_all(engine)

    def test_get_empty_posts(self):
        response = self.client.get('/api/posts')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')

        data = json.loads(response.data.decode('ascii'))
        self.assertEqual(data, [])

    def test_get_posts(self):
        post_A = models.Post(title='Example A', body='Body A')
        post_B = models.Post(title='Example B', body='Body B')

        session.add_all([post_A, post_B])
        session.commit()

        response = self.client.get('/api/posts')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')

        data = json.loads(response.data.decode('ascii'))
        self.assertEqual(len(data), 2)

        response_post_A, response_post_B = data
        self.assertEqual(response_post_A['title'], post_A.title)
        self.assertEqual(response_post_A['body'], post_A.body)
        self.assertEqual(response_post_B['title'], post_B.title)
        self.assertEqual(response_post_B['body'], post_B.body)



if __name__ == "__main__":
    unittest.main()
