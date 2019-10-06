import socket
from jinja2 import Environment, FileSystemLoader
import consts


def build_html(usage, disks, smart):
    hostname = socket.gethostname()
    smart_data_list = []
    for i in range(len(smart)):
        smart_data = []
        for j in range(len(smart[i])):
            if j > 0:
                value = smart[i][j].split(',')
                data = {key: val for key, val in zip(consts.SMART_TABLE_COLUMN, value)}
                smart_data.append(data)
        smart_data_list.append(smart_data)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(consts.TEMPLATE_PATH)
    disp_text = template.render(hostname=hostname, usage=usage, smart=zip(disks, smart_data_list))

    return disp_text

