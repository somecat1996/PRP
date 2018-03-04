import my_commnds
from result import Result
import re


class result_manager:
    def __init__(self, task_id, user, password):
        self.user = user
        self.password = password
        self.task_id = task_id
        self.results = []

    def load(self, text):
        results = re.findall("(<result.*?</result>)", text, re.S)
        for i in results:
            tmp = Result(i)
            if tmp.name == '':
                continue
            else:
                flag = True
                for j in self.results:
                    if j.Compare(tmp):
                        flag = False
                if flag:
                    self.results.append(tmp)

    def get(self):
        text = my_commnds.get_results(self.user, self.password, self.task_id)
        self.load(text)
        return text

    def display(self):
        output = ''
        for i in self.results:
            output += "id:%s\n" % i.id
            output += "ownername:%s\n" % i.ownername
            output += "comment:%s\n" % i.comment
            output += "creation_time:%s\n" % i.creation_time
            output += "modification_time:%s\n" % i.modification_time
            output += "host:%s\n" % i.host
            output += "port:%s\n" % i.port
            output += "nvt_oid:%s\n" % i.nvt_oid
            output += "name:%s\n" % i.name
            output += "family:%s\n" % i.family
            output += "summary:%s\n" % i.summary
            output += "solution:%s\n" % i.solution
            output += "scan_nvt_version:%s\n" % i.scan_nvt_version
            output += "threat:%s\n" % i.threat
            output += "severity:%s\n" % i.severity
            output += "type:%s\n" % i.type
            output += "qod:%s\n" % i.qod
            output += "description:%s\n" % i.description
            output += '=' * 50 + '\n'
        return output
