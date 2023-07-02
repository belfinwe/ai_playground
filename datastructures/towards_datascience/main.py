from cats_pydantic import CatRequest, Address
my_json = {
    "name": "Lévy",
    "age": 3,
    "address": {
        "city": "Wonderland",
        "zip_code": "ABCDE",
        "number": 123
    }
}

data = CatRequest.parse_obj(my_json)
print(data.name)  # Lévy
print(data.address.number) # 123


def bad_data():
    # Bad data, data not matching typing. Throws exception
    bad_data = {
        "name": "Lévy",
        "age": "am I an age?",  # Note the type change here
        "address": {
            "city": "Wonderland",
            "zip_code": "ABCDE",
            "number": 123
        }
    }

    try:
        CatRequest.parse_obj(bad_data)
    except Exception as err:
        print(f"Something went wrong with the data: {err}")


def extra_data():
    # More key value pairs are added:
    unnecessary_data = {
        "name": "Lévy",
        "age": 3,
        "key": "value",  # unnecessary
        "key2": "value2",  # unnecessary x2
        "address": {
            "city": "Wonderland",
            "zip_code": "ABCDE",
            "number": 123
        }
    }

    data = CatRequest.parse_obj(unnecessary_data)  # Does not contain the extra data
    try:
        print(data.key2)
    except Exception as err2:
        print(f"{err2}")


def single_dispatch():
    from functools import singledispatch

    @singledispatch
    def process(model):
        """
        Default processing definition
        """
        raise NotImplementedError(f"I don't know how to process {type(model)}")

    @process.register
    def _(model: Address):
        """
        Handle addresses
        """
        print(f"Just got an address from {model.city}")

    @process.register
    def _(model: CatRequest):
        """
        Handle Cat Requests
        """
        print(f"Processing {model.name} the cat!")

    address = Address(
        city="Wonderland",
        zip_code="ABCDE",
        number=123,
    )
    cat = CatRequest(
        name="Lévy",
        age=3,
        address=address
    )

    process(address)  # Just got an address from Wonderland
    process(cat)  # Processing Lévy the cat!
    process("something else")  # NotImplementedError: I don't know how to process <class 'str'>


if __name__ == "__main__":
    bad_data()
    extra_data()
    single_dispatch()