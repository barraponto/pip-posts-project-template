class DevelopmentConfig(object):
    DATABASE_URI = "postgresql://postgres@localhost:5432/tf-posts"
    DEBUG = True

class TestingConfig(object):
    DATABASE_URI = "postgresql://postgres@localhost:5432/tf-posts-test"
    DEBUG = True
