import os, sys

def migrate():
	from sqlalchemy import Table
	from app import models
	
	for(name, table) in vars(models).items():
		if isinstance(table, Table):
			table.create()
# def run():
# 	import urls
# 	if os.environ.get("REQUEST_METHOD", ""):
# 		from wsgiref.handlers import BaseCGIHandler
# 		BaseCGIHandler(sys.stdin, sys.stdout, sys.stderr, os.environ).run(urls.urls)
# 	else:
# 		from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
# 		httpd=WSGIServer(('',8000), WSGIRequestHandler)
# 		httpd.set_app(urls.urls)
# 		print("Serving HTTP on %s port %s ..." % httpd.socket.getsockname())
# 		httpd.serve_forever()

def run():
	import urls
	from app.engine import  app
	if os.environ.get("REQUEST_METHOD", ""):
		from wsgiref.handlers import BaseCGIHandler
		BaseCGIHandler(sys.stdin, sys.stdout, sys.stderr, os.environ).run(urls.urls)
	else:
		#from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
		from wsgiref.simple_server import make_server, demo_app
		#httpd = WSGIServer(('', 8080), WSGIRequestHandler)
		httpd = make_server('', 8000, app)
		httpd.set_app(urls.urls)
		print ("Serving HTTP on %s port %s ..." % httpd.socket.getsockname())
		httpd.serve_forever()



if __name__ == '__main__':
	if 'migrate' in sys.argv:
		migrate()
	if 'run' in sys.argv:
		run()
