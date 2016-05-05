import os
from mako.template import Template

extensions = {
    'html': 'text/html',
    'atom': 'application/atom+xml'
}


def app(start_response, template_file, vars):
    ext = template_file.rsplit(".")
    contenttype = "text/html"
    if len(ext) > 1 and (ext[1] in extensions):
        contenttype = extensions[ext[1]]
        #template = kid.Template(file=os.path.join('templates', template_file), **vars)
        template=Template(filename=template_file, module_directory='templates/')
        #body = template.serialize(encoding='utf-8')
        start_response("200 OK", [('Content-Type', contenttype)])
        #print(template.render())
        return [template]




