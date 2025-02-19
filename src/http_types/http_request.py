class HttpRequest:
  def __init__(self, body: dict, params: dict = None) -> None:
    self.body = body
    self.params = params
