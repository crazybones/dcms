class Container:
    def __init__(self, c_info):
        self.__container_id = c_info['Id']
        self.__tag = c_info['Tag']
        self.__image = c_info['Image']
        self.__command = c_info['Command']
        self.__created = c_info['Created']
        self.__status = c_info['Status']
        self.__state = c_info['State']
        self.__ports = c_info['Ports']
        self.__names = c_info['Names']
        self.__ip = c_info['IpAddress']
        self.__image_id = c_info['ImageId']

    @property
    def container_id(self):
        return self.__container_id

    @container_id.setter
    def container_id(self, container_id):
        self.__container_id = container_id

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image

    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, command):
        self.__command = command

    @property
    def created(self):
        return self.__created

    @created.setter
    def created(self, created):
        self.__created = created

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def ports(self):
        return self.__ports

    @ports.setter
    def ports(self, ports):
        self.__ports = ports

    @property
    def names(self):
        return self.__names

    @names.setter
    def names(self, names):
        self.__names = names

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        self.__ip = ip

    @property
    def image_id(self):
        return self.__image_id

    @image_id.setter
    def image_id(self, image_id):
        self.__image_id = image_id
