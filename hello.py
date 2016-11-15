def application(env, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    qs = env['QUERY_STRING']
    data = '\n'.join(qs.split('&'))
    return [data]
