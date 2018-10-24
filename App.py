from cgi_gateway import run_with_cgi
from Plotter import graph


def simple_app(environ, start_response):
    """
    (dict, callable( status: str,
                     headers: list[(header_name: str, header_value: str)]))
                  -> body: iterable of strings
    """
    status = 'OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    #need to implement graph here

if __name__ == '__main__':
    run_with_cgi(simple_app(environ, start_response))
    
        
