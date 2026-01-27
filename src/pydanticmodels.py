from pydantic import BaseModel, ValidationError, field_validator

class Person_pydantic(BaseModel):
    name : str
    email : str