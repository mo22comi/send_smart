from jinja2 import Environment, FileSystemLoader


class Html:
    def __init__(self, **kwargs):
        self.usage = kwargs['usage']
        self.disks = kwargs['disks']
        self.smart = kwargs['smart']
        self.columns = kwargs['columns']
        self.template_path = kwargs['template_path']

    def build_html(self):
        smart_data_list = []
        for smart_info in self.smart:
            smart_data = []
            for j, smart_row in enumerate(smart_info):
                if j > 0:
                    value = smart_row.split(',')
                    data = {key: val for key, val in zip(self.columns, value)}
                    smart_data.append(data)
            smart_data_list.append(smart_data)

        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(self.template_path)
        contents = template.render(usage=self.usage, smart=zip(self.disks, smart_data_list))

        return contents
