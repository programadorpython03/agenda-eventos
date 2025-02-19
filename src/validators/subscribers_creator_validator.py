from cerberus import Validator

def subscribers_creator_validator(request: any):

  subscribers_validator = Validator({
    "data": {
      "type": "dict",
      "schema": {
        "nome": {"type": "string", "required": True, "empty": False, "empty": False},
        "email": {"type": "string", "required": True, "empty": False, "empty": False}, 
        "link_evento": {"type": "string", "required": False, "empty": False},
        "evento_id": {"type": "integer", "required": True, "empty": False},
      } 
    }
  })

  response = subscribers_validator.validate(request.json)

  if not response:
    raise ValueError(subscribers_validator.errors)

  return response