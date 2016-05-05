# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460127058.7776
_enable_loop = True
_template_filename = 'templates/index.html'
_template_uri = 'templates/index.html'
_source_encoding = 'ascii'
_exports = ['makerow']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def makerow(row):
            return render_makerow(context._locals(__M_locals),row)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()

        rows = [[v for v in range(0,10)] for row in range(0,10)]
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['row','v','rows'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n<table>\n')
        for row in rows:
            __M_writer('        ')
            __M_writer(str(makerow(row)))
            __M_writer('\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_makerow(context,row):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n    <tr>\n')
        for name in row:
            __M_writer('        <td>')
            __M_writer(str(name))
            __M_writer('</td>')
        __M_writer('    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "templates/index.html", "uri": "templates/index.html", "line_map": {"32": 6, "33": 6, "34": 6, "35": 8, "48": 13, "41": 10, "45": 10, "46": 12, "47": 13, "16": 0, "49": 13, "50": 15, "56": 50, "24": 1, "30": 3, "31": 5}}
__M_END_METADATA
"""
