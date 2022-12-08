class DataBase:
    """Description"""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, login: str, password: str, port: int):
        self.login = login
        self.password = password
        self.port = port

    def __del__(self):
        DataBase.__instance = None
        print('Выполение удаления')