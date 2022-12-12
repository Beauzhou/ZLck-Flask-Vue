from flask_script import Manager
from app.exts import db

DBmanager = Manager()

@DBmanager.command
def createdb(drop_first=False):
    """Creates the database."""
    if drop_first:
        db.drop_all()
    db.create_all()