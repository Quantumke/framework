from app import engine
from app import models

def list(environ, start_response):
    rows = models.ben.select().execute()
    return engine.app(start_response, 'templates/index.html', locals())

def item_get(environ, start_response):
    id = environ['selector.vars']['id']
    row = models.ben.select(models.ben.c.id==id).execute().fetchone()
    return engine.app(start_response, 'entry.html', locals())
