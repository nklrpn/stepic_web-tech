#!/usr/bin/python

def app(environ, start_response):
    body = ''

    for line in environ['QUERY_STRING'].split('&'):
        body += line + "\n"

    start_response('200 OK', [('Content-type', 'text/plain')])

    return [body]