from animals_pydantic import Sheep, Dogs, Pigs, Mammals
from functools import singledispatch

_sheep = {"legs": 4, "equal": 1, "contribute": "wool"}
_dogs = {"legs": 4, "equal": 1, "contribute": "security"}
_pigs = {"contribute": "leadership"}

sheep = Sheep(**_sheep)
dogs = Dogs(**_dogs)
pigs = Pigs.parse_obj(_pigs)

print(f"{sheep}")
print(f"{dogs}")
print(f"{pigs}")


def get_legs(_animal: Sheep|Dogs|Pigs) -> int:
    print(type(_animal))
    return _animal.legs

print(get_legs(sheep))
print(get_legs(pigs))
print(get_legs(
    Mammals(**{"legs": 2.0, "equal": 2})
))


print("single dispatch")

@singledispatch
def get_contribution(_data):
    raise NotImplementedError(f"No current process for {type(_data)}")

@get_contribution.register
def _(_data: Sheep) -> str:
    return f"Sheep provide {_data.contribute}"

@get_contribution.register
def _(_data: Dogs) -> str:
    return f"Dogs provide {_data.contribute}"

@get_contribution.register
def _(_data: Pigs) -> str:
    return f"Pigs provide {_data.contribute}"

@singledispatch
def get_special(_data):
    raise NotImplementedError(f"No current process for {type(_data)}")

@get_special.register
def _(_data: Sheep):
    return f"Sheep cunning: {_data.cunning}"

@get_special.register
def _(_data: Pigs):
    return f"Pigs cunning: {_data.cunning}"

@get_special.register
def _(_data: Dogs):
    return f"Dogs got fur: {_data.fur}"

farm = [sheep, dogs, pigs]
for animal in farm:
    print(get_contribution(animal))
    print(get_special(animal))
