from cgi import parse_qs


def application(env, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    request_query = parse_qs(env['QUERY_STRING'])
    response = ''
    for key in request_query:
        for value in request_query[key]:
            response += str(key) + '=' + str(value) + '\n'
    return [response]
