class Server:
    """Description"""

    __AMOUNT_OF_SERVERS = 0

    def __new__(cls, *args, **kwargs):
        cls.__AMOUNT_OF_SERVERS += 1
        return super().__new__(cls)

    def __init__(self):
        self.__ip = self.__AMOUNT_OF_SERVERS
        self.buffer = []
        self.router = None

    def send_data(self, data):
        self.router.buffer.append(data)

    def get_data(self):
        result = self.buffer.copy()
        self.buffer = []
        return result

    def get_ip(self):
        return self.__ip


class Router:
    """Description"""

    def __init__(self):
        self.buffer = []
        self.__linked_srvs = {}

    def link(self, server):
        self.__linked_srvs[server.get_ip()] = server
        server.router = self

    def unlink(self, server):
        del self.__linked_srvs[server.get_ip()]
        server.router = None

    def send_data(self):
        for item in self.buffer:
            if item.ip in self.__linked_srvs.keys():
                self.__linked_srvs[item.ip].buffer.append(item)
        self.buffer = []


class Data:
    """Description"""

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
