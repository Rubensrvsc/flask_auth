from returns.result import Result, Success, Failure
from returns.pipeline import flow, is_successful
from returns.pointfree import bind
from models.user import User, Task
from config.imports import db

def get_user(id_user, name_task):
  user = User.query.filter_by(id=id_user).one_or_none()
  if user is not None:
    return Success({'user': user, 'name_task': name_task})
  return Failure('Usuário nao encontrado')

def append_task(dict_user):
  if 'name_task' in dict_user.keys() and dict_user['name_task'] is not None:
    task = Task(name_task=dict_user['name_task'])
    dict_user['user'].tasks.append(task)
    return Success(dict_user['user'])
  return Failure("Nome da task nao existe")

def insert_task(user):
  db.session.add(user)
  db.session.commit()
  return Success(user.serialize)

def create_task_to_user(id_user, name_task):
  result = flow(
    get_user(id_user, name_task),
    bind(append_task),
    bind(insert_task),
  )

  return result.unwrap() if is_successful(result) else result.failure()