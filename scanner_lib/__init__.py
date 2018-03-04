from openvas_lib import VulnscanManager
import commands
import re
from result import Result


class ScannerManager:
    def __init__(self, host, user, password, port0=9390, timeout0=None):
        self.scanner_manager = VulnscanManager(host, user, password, port0, timeout0)
        self.scanner_list = {}
        self.user = user
        self.password = password

    def launch_scan(self, target, **kwargs):
        task_id, target_id = self.scanner_manager.launch_scan(target, **kwargs)
        name = kwargs.get("name", 'nunamed')
        self.scanner_list[task_id] = Scanner(target, target_id, name)
        return task_id

    def delete_scan(self, task_id):
        self.scanner_manager.delete_scan(task_id)
        del self.scanner_list[task_id]

    def get_results(self, task_id):
        if task_id in self.scanner_list:
            tmp = commands.getoutput("omp -u "+self.user+" -w "+self.password+" -iX '<get_results task_id=\""+task_id+"\"/>'")
            results = re.findall("(<result.*?</result>)", tmp, re.S)
            for i in results:
                tmp = Result(i)
                if tmp.name == '':
                    continue
                else:
                    flag = True
                    for j in self.scanner_list[task_id].result:
                        if j.id == tmp.id:
                            flag = False
                    if flag:
                        self.scanner_list[task_id].result.append(tmp)
        else:
            return "Error: my_scanner doesn't exist."

    def display_result(self, task_id):
        results = self.scanner_list[task_id].result
        for i in results:
            print "id:%s" % i.id
            print "ownername:%s" % i.ownername
            print "comment:%s" % i.comment
            print "creation_time:%s" % i.creation_time
            print "modification_time:%s" % i.modification_time
            print "host:%s" % i.host
            print "port:%s" % i.port
            print "nvt_oid:%s" % i.nvt_oid
            print "name:%s" % i.name
            print "family:%s" % i.family
            print "summary:%s" % i.summary
            print "solution:%s" % i.solution
            print "scan_nvt_version:%s" % i.scan_nvt_version
            print "threat:%s" % i.threat
            print "severity:%s" % i.severity
            print "type:%s" % i.type
            print "qod:%s" % i.qod
            print "description:%s" % i.description
            print ''




class Scanner:
    def __init__(self, target, target_id, name, result=[]):
        self.target = target
        self.target_id = target_id
        self.result = result
        self.name = name