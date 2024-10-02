class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #       this is executed before reaching the view
        request.META['Custom key'] = 'Davis was here'

        response = self.get_response(request)
        #         add what you want to the response
        response.set_cookie('custom', 'custom-value')
        return response


def FunctionCustomMiddleWare(get_response):
    def middleware(request):
        request.META['Another key'] = 'Another key'
        response = get_response(request)
        response.set_cookie('custom function key', 'custom function key')
        assert False
        return response

    return middleware
