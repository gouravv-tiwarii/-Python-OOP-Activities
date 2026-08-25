class UpperAttrMeta(type):
    def __new__(mcs, name, bases, dct):
        uppercase_attrs = {
            k.upper() if not k.startswith("__") else k: v 
            for k, v in dct.items()
        }
        return super().__new__(mcs, name, bases, uppercase_attrs)


class Config(metaclass=UpperAttrMeta):
    port = 8080
    host = "localhost"


if __name__ == "__main__":
    print("PORT:", Config.PORT)
    print("HOST:", Config.HOST)