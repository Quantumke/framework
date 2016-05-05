import selector
from app import controller

urls = selector.Selector()
urls.add('/', GET=controller.list)