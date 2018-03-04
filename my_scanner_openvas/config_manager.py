from my_commnds import get_configs
import re


class Configs:
    def __init__(self):
        self.configdir = {}
        self.load_configs()
        self.get_configs()

    def get_configs(self):
        output = get_configs('admin', 'admin')
        configs = re.findall('(<config id.*?</config>)', output)
        for i in configs:
            id = re.findall('<config id="(.*?)">', i)[0]
            name = re.findall('</owner><name>(.*?)</name><comment>', i)[0]
            if id not in self.configdir:
                self.configdir[id] = name
        self.save_configs()

    def load_configs(self):
        try:
            file = open('configs.txt', 'r')
        except:
            file = open('configs.txt', 'w')
            file.close()
            return
        line = file.readline()
        while line:
            if len(line) > 1:
                s_line = line.split('\t')
                self.configdir[s_line[0]] = s_line[1]
            line = file.readline()
        file.close()

    def save_configs(self):
        file = open('configs.txt', 'w')
        for i in self.configdir:
            file.write(i)
            file.write('\t')
            file.write(self.configdir[i])
            file.write('\n')
        file.close()
