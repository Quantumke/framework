import selector
from app import controller

urls = selector.Selector()
urls.add('/home/', GET=app.controller.list)
urls.add('', GET=app.controller.list)
