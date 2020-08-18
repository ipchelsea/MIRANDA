from endpoints import Controller

from vision import detectText


class Default(Controller):
  def GET(self):
    detectText('carpic.jpg')

  def POST(self, **kwargs):
    return 'hello {}'.format(kwargs['name'])

class Foo(Controller):
  def GET(self):
    return "bang"

#https://pypi.org/project/endpoints/