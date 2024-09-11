class SimpleMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
    # One-time configuration and initialization.

  def __call__(self, request):
    # request view ga kelishidan oldin tutib olib nimadir qilish
    
    # Code to be executed for each request before
    # the view (and later middleware) are called.
    print(f"Before request for {request.path}")

    response = self.get_response(request)
     # response klientga ga ketishidan oldin tutib olib nimadir qilish

    # Code to be executed for each request/response after
    # the view is called.
    print("After getting response")

    return response