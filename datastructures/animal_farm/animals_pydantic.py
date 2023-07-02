from pydantic import BaseModel

class Mammals(BaseModel):
    legs: int = 4
    equal: int = 1

class Sheep(Mammals):
    contribute: str
    cunning: bool = False

class Dogs(Mammals):
    contribute: str
    fur: bool = True

class Pigs(Mammals):
    contribute: str
    equal: int = 2
    cunning: bool = True
