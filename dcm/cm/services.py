from .processors import get_container_data_as_list, execute_bash_command, get_json
from .container import Container


class ContainerServices:
    @staticmethod
    def prepare_containers_info():
        bash_cmd = "curl --unix-socket /var/run/docker.sock http://localhost/containers/json"
        containers_json = execute_bash_command(bash_cmd)
        containers = []
        containers += map(Container, get_container_data_as_list(containers_json))
        return containers

    # temp, won't make it static
    def get_test_data(self):
        test_data = []
        test_data += map(Container, get_container_data_as_list(get_json()))
        return test_data
