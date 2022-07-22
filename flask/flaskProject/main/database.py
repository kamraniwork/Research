from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# import setup

# Database ORM Configuration
# db = SQLAlchemy()
serializer = Marshmallow()
# Database Migrations Configuration
migration = Migrate(directory='./app/migrations')
