from returns.result import Result, Success, Failure
from returns.pipeline import flow, is_successful
from returns.pointfree import bind
from models.user import User

def get_user(id_user):
  user = User.query.filter_by(id=id_user).one_or_none()
  if user is not None:
    return Success(user)
  return Failure('Usuário não encontrado')

def get_all_tasks(user):
  if len(user.tasks) > 0:
    return Success([result.serialize for result in user.tasks])
  return Failure('Usuario sem tasks')

def all_tasks(id_user):
  result = flow(
    get_user(id_user),
    bind(get_all_tasks),
  )
  return result.unwrap() if is_successful(result) else result.failure()