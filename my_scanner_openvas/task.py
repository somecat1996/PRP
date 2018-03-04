import re


class task:
    def __init__(self):
        self.id = None
        self.ownername = None
        self.name = None
        self.comment = None
        self.creation_time = None
        self.modification_time = None
        self.writable = None
        self.in_use = None
        self.config_id = None
        self.config_name = None
        self.target_id = None
        self.target_name = None
        self.scanner_id = None
        self.scanner_name = None
        self.progress = None
        self.finished = None
        self.report_id = None
        self.result = None

    def load(self, text):
        self.id = re.findall('<task id="(.*?)">', text)[0]
        self.ownername = re.findall('<owner><name>(.*?)</name></owner>', text)[0]
        self.name = re.findall('</owner><name>(.*?)</name><comment>', text)[0]
        self.comment = re.findall('<comment>(.*?)</comment>', text)[0]
        self.creation_time = re.findall('<creation_time>(.*?)</creation_time>', text)[0]
        self.modification_time = re.findall('<modification_time>(.*?)</modification_time>', text)[0]
        self.writable = re.findall('<writable>(.*?)</writable>', text)[0]
        self.in_use = re.findall('<in_use>(.*?)</in_use>', text)[0]

        config = re.findall('(<config.*?</config>)', text)[0]
        self.config_id = re.findall('<config id="(.*?)">', config)[0]
        self.config_name = re.findall('<name>(.*?)</name>', config)[0]

        target = re.findall('(<target.*?</target>)', text)[0]
        self.target_id = re.findall('<target id="(.*?)">', target)[0]
        self.target_name = re.findall('<name>(.*?)</name>', target)[0]

        scanner = re.findall('(<scanner.*?</scanner>)', text)[0]
        self.scanner_id = re.findall('<scanner id="(.*?)">', scanner)[0]
        self.scanner_name = re.findall('<name>(.*?)</name>', scanner)[0]

        self.progress = re.findall('<progress>(.*?)</progress>', text)[0]
        self.finished = re.findall('<finished>(.*?)</finished>', text)[0]
        if self.finished == '1':
            self.report_id = re.findall('<report id="(.*?)">', text)[0]

    def display(self):
        print self.id
        print self.ownername
        print self.name
        print self.comment
        print self.creation_time
        print self.modification_time
        print self.writable
        print self.in_use
        print self.config_id
        print self.config_name
        print self.target_id
        print self.target_name
        print self.scanner_id
        print self.scanner_name
        print self.progress
        print self.finished
