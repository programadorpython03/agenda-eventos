from cerberus import Validator

def event_creator_validator(request: any):

  body_validator = Validator({
    "data": {
      "type": "dict",
      "schema": {
        "nome": {"type": "string", "required": True, "empty": False},
      } 
    }
  })

  response = body_validator.validate(request.json)

  if not response:
    raise ValueError(body_validator.errors)

  return response