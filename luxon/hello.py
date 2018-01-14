from luxon import register_resource

@register_resource('GET', '/hello', 'tag')
def hello(req, resp):
    return 'hello world'
