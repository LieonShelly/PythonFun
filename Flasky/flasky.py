import os
from app import create_app, db
from auth.models import User, Role

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
