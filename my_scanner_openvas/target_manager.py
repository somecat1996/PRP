from my_commnds import get_targets
import re


class Targets:
    def __init__(self):
        self.targetdir = {}
        self.load_targets()
        self.get_targets()

    def get_targets(self):
        output = get_targets('admin', 'admin')
        targets = re.findall('(<target id.*?</target>)', output)
        for i in targets:
            id = re.findall('<target id="(.*?)">', i)[0]
            name = re.findall('</owner><name>(.*?)</name><comment>', i)[0]
            host = re.findall('<hosts>(.*?)</hosts>', i)[0]
            if id not in self.targetdir:
                self.targetdir[id] = [name, host]
        self.save_taregts()

    def load_targets(self):
        try:
            file = open('targets.txt', 'r')
        except:
            file = open('targets.txt', 'w')
            file.close()
            return
        line = file.readline()
        while line:
            if len(line) > 1:
                s_line = line.split('\t')
                self.targetdir[s_line[0]] = [s_line[1], s_line[2]]
            line = file.readline()
        file.close()

    def save_taregts(self):
        file = open('targets.txt', 'w')
        for i in self.targetdir:
            file.write(i)
            file.write('\t')
            file.write(self.targetdir[i][0])
            file.write('\t')
            file.write(self.targetdir[i][1])
            file.write('\n')
        file.close()
