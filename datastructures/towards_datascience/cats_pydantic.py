from pydantic import BaseModel, Extra, Field

# Cats data format
'''
{
    "name": string,
    "age": integer,
    "address": {
        "city": string,
        "zip_code": string,
        "number": integer
    }
}
'''
'''
class Address(BaseModel):
    """
    Cat API Address definition
    """
    city: str
    zip_code: str
    number: int

class CatRequest(BaseModel):
    """
    Cat API Request definition
    """
    name: str
    age: int
    address: Address
'''

# Forbid extra data

class Address(BaseModel):
    """
    Cat API Address definition
    """
    class Config:
        extra = Extra.forbid

    # Note how we can even add descriptions to the fields!
    city: str = Field(..., description="Where the cat lives")
    zip_code: str
    number: int

 
class CatRequest(BaseModel):
    """
    Cat API Request definition
    """
    class Config:
        extra = Extra.forbid

    name: str
    age: int
    address: Address