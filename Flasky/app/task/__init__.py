from flask import Blueprint

task_api = Blueprint('task', __name__)

from  app.task import TaskUseCelery