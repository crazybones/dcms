from .processors import BashProcessor, JsonProcessor
from .container import Container


class ContainerServices:
    __containers = []

    def prepare_containers_info(self):
        bash_cmd = "curl --unix-socket /var/run/docker.sock http://localhost/containers/json"
        containers_json = BashProcessor.execute(bash_cmd)
        for elem in JsonProcessor.prepare_container_data(containers_json):
            self.__containers.append(Container(elem))

    def get_containers_info(self):
        return self.__containers

    # temp, won't make it static
    def get_test_data(self):
        j = JsonProcessor.prepare_container_data(JsonProcessor.get_json())
        test_data = []
        for elem in j:
            test_data.append(Container(elem))
        return test_data
