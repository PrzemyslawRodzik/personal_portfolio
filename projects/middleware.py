


class SampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("W __init__ ")

    def __call__(self, request):

        print("Przed view")

        response = self.get_response(request)
        print("Po  view")



        return response