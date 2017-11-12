class Container:
    def __init__(self, c_info):
        self.container_id = c_info['Id']
        self.tag = c_info['Tag']
        self.image = c_info['Image']
        self.image_id = c_info['ImageId']
        self.command = c_info['Command']
        self.created = c_info['Created']
        self.status = c_info['Status']
        self.state = c_info['State']
        self.ports = c_info['Ports']
        self.names = c_info['Names']
        self.ip = c_info['IpAddress']
