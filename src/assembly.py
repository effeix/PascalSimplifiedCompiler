class Assembly():
    __code = ""

    def __new__(cls):

        if not hasattr(cls, "__instance"):
            cls.__instance = super(Assembly, cls).__new__(cls)

        return cls.__instance

    @staticmethod
    def append(line):
        Assembly.__code += line

    @staticmethod
    def code():
        print(Assembly.__code)