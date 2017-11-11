import datetime
import json
import subprocess


class BashProcessor:
    @staticmethod
    def execute(bash_command):
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        return output


class JsonProcessor:
    @staticmethod
    def prepare_container_data(jsn):
        short_container_info = []
        json_list = JsonProcessor.get_json_as_list(jsn)
        for cont in json_list:
            inner_map = {'Id': cont['Id'], 'Image': cont['Image'], 'Command': cont['Command'],
                         'Created': datetime.datetime.fromtimestamp(cont['Created']).strftime('%Y-%m-%d %H:%M:%S'),
                         'Status': cont['Status'], 'Ports': ';'.join(cont['Ports']), 'Names': ';'.join(cont['Names']),
                         'ImageId': cont['ImageID'], 'Tag': ';'.join(cont['Labels']), 'State': cont['State'],
                         'IpAddress': cont['NetworkSettings']['Networks']['bridge']['IPAddress']}
            short_container_info.append(inner_map)
        return short_container_info

    @staticmethod
    def get_json_as_list(jsn):
        return json.loads(jsn)

    # temp as testing data
    @staticmethod
    def get_json():
        return '[{"Id":"b77ded706b470a4b36fa8647c4c74f2d63dccdeb404cca54f78015184eb0755d","Names":["/alp_jcb"],' \
               '"Image":"alp_jcb:latest",' \
               '"ImageID":"sha256:2378590ab4c08d38ae974af28e0c605782f968ad45c01c350f8125de0b44d1ed",' \
               '"Command":"/bin/sh","Created":1507996350,"Ports":[],"Labels":{},"State":"running","Status":"Up About ' \
               'a minute","HostConfig":{"NetworkMode":"default"},"NetworkSettings":{"Networks":{"bridge":{' \
               '"IPAMConfig":null,"Links":null,"Aliases":null,' \
               '"NetworkID":"a5bea23768b5eb4a0f751a9b4827e4c2d07c3537f632f169758d439d0326fc83",' \
               '"EndpointID":"f2a4732bb83a2abe633f1e44f3ab59e3ea27c4b4ff817fba62e423939438fcaa",' \
               '"Gateway":"172.17.0.1","IPAddress":"172.17.0.2","IPPrefixLen":16,"IPv6Gateway":"",' \
               '"GlobalIPv6Address":"","GlobalIPv6PrefixLen":0,"MacAddress":"02:42:ac:11:00:02"}}},"Mounts":[{' \
               '"Type":"bind","Source":"/var/run/docker.sock","Destination":"/var/run/docker.sock","Mode":"",' \
               '"RW":true,"Propagation":""}]},' \
               '{"Id":"c839778321c3c2160188f776282b4356b997861be0fb173366fc049f7df07761","Names":["/alpine_bash"],' \
               '"Image":"alpine_bash:3.6",' \
               '"ImageID":"sha256:bc0d5ef8bd5d75329474a5b4a4a000068d3128e75da0489a88e908778fe91d91",' \
               '"Command":"/bin/sh","Created":1507739449,"Ports":[],"Labels":{},"State":"running","Status":"Up 46 ' \
               'seconds","HostConfig":{"NetworkMode":"default"},"NetworkSettings":{"Networks":{"bridge":{' \
               '"IPAMConfig":null,"Links":null,"Aliases":null,' \
               '"NetworkID":"a5bea23768b5eb4a0f751a9b4827e4c2d07c3537f632f169758d439d0326fc83",' \
               '"EndpointID":"cb7739de13392f0d991480c664a082bd42bead8ce8160c6c49119fecccbc02d7",' \
               '"Gateway":"172.17.0.1","IPAddress":"172.17.0.3","IPPrefixLen":16,"IPv6Gateway":"",' \
               '"GlobalIPv6Address":"","GlobalIPv6PrefixLen":0,"MacAddress":"02:42:ac:11:00:03"}}},"Mounts":[{' \
               '"Type":"bind","Source":"/var/run/docker.sock","Destination":"/var/run/docker.sock","Mode":"",' \
               '"RW":true,"Propagation":""}]}] '
