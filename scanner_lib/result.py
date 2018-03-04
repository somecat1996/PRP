import re


class Result:
    def __init__(self, string):
        self.id = None
        self.ownername = None
        self.comment = None
        self.creation_time = None
        self.modification_time = None
        self.host = None
        self.port = None
        self.nvt_oid = None
        self.name = None
        self.family = None
        self.summary = None
        self.solution = None
        self.scan_nvt_version = None
        self.threat = None
        self.severity = None
        self.type = None
        self.qod = None
        self.description = None

        self.load(string)

    def load(self, string):
        Qod = transfer(re.findall('(<qod>.*?</qod>)', string, re.S))
        Nvt = transfer(re.findall('(<nvt oid=.*?</nvt>)', string, re.S))
        Owner = transfer(re.findall('(<owner>.*?</owner>)', string, re.S))

        self.id = transfer(re.findall('<result id="(.*?)">', string, re.S))
        self.ownername = transfer(re.findall('<name>(.*?)</name>', Owner, re.S))
        self.comment = transfer(re.findall('<comment>(.*?)</comment>', string, re.S))
        self.creation_time = transfer(re.findall('<creation_time>(.*?)</creation_time>', string, re.S))
        self.modification_time = transfer(re.findall('<modification_time>(.*?)</modification_time>', string, re.S))
        self.host = transfer(re.findall('<host>(.*?)</host>', string, re.S))
        self.port = transfer(re.findall('<port>(.*?)</port>', string, re.S))
        self.nvt_oid = transfer(re.findall('<nvt oid="(.*?)">', Nvt, re.S))
        self.name = transfer(re.findall('<name>(.*?)</name>', Nvt, re.S))
        self.family = transfer(re.findall('<family>(.*?)</family>', Nvt, re.S))
        self.scan_nvt_version = transfer(re.findall('<scan_nvt_version>(.*?)</scan_nvt_version>', string, re.S))
        self.threat = transfer(re.findall('<threat>(.*?)</threat>', string, re.S))
        self.severity = transfer(re.findall('<severity>(.*?)</severity>', string, re.S))
        self.type = transfer(re.findall('<type>(.*?)</type>', Qod, re.S))
        self.qod = transfer(re.findall('<value>(.*?)</value>', Qod, re.S))
        self.description = transfer(re.findall('<description>(.*?)</description>', string, re.S))

        self.summary = transfer(re.findall('summary=(.*?)\|', string, re.S))
        self.solution = transfer(re.findall('solution=(.*?)\|', string, re.S))

    def Compare(self, other):
        if self.port != other.port:
            return False
        if self.name != other.name:
            return False
        if self.description != other.description:
            return False
        return True




def transfer(alist):
    if len(alist) == 0:
        return 'None'
    else:
        return alist[0]