class MainData:
    __shared_atr = {
        'name': 'qwerty',
        'id': 1,
        'data': {}
    }

    def __init__(self):
        self.__dict__ = self.__shared_atr
