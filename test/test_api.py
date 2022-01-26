from array import array
from controllers.auth import app

def test_all_users():
  response = app.test_client().get('/')

  assert response.status == '200 OK'
  assert type(response.json['data']) is list