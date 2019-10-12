import socket
from jinja2 import Environment, FileSystemLoader
import consts


class Html:
    def __init__(self, usage, disks, smart):
        self.usage = usage
        self.disks = disks
        self.smart = smart

    def build_html(self):
        hostname = socket.gethostname()
        smart_data_list = []
        for i in range(len(self.smart)):
            smart_data = []
            for j in range(len(self.smart[i])):
                if j > 0:
                    value = self.smart[i][j].split(',')
                    data = {key: val for key, val in zip(consts.SMART_TABLE_COLUMN, value)}
                    smart_data.append(data)
            smart_data_list.append(smart_data)

        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(consts.TEMPLATE_PATH)
        contents = template.render(hostname=hostname, usage=self.usage, smart=zip(self.disks, smart_data_list))

        return contents
