# coding=utf-8
import os
import uuid
from xml.dom import minidom, Node


class Setting:
    def __init__(self, ID=str(uuid.uuid1())):
        self.id = ID
        self.path = 'tasks/' + self.id + '/'
        self.mkpath()
        self.name = 'unnamed'
        self.IP = ''
        self.comment = ''
        self.ifopenvas = False
        self.openvasconfig = ''
        self.openvasid = ''
        self.ifoval = False
        self.ovalconfig = []

    def mkpath(self):
        path = 'tasks/'
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def save(self):
        f = minidom.Document()
        setting = f.createElement('setting')
        setting.setAttribute('id', self.id)
        name = f.createElement('name')
        name.appendChild(f.createTextNode(self.name))
        setting.appendChild(name)
        host = f.createElement('host')
        host.appendChild(f.createTextNode(self.IP))
        setting.appendChild(host)
        comment = f.createElement('comment')
        comment.appendChild(f.createTextNode(self.comment))
        setting.appendChild(comment)

        openvas = f.createElement('openvas')
        openvas.setAttribute('using', str(int(self.ifopenvas)))
        if self.ifopenvas:
            openvas.setAttribute('id', self.openvasid)
            openvas_config = f.createElement('config')
            openvas_config.appendChild(f.createTextNode(self.openvasconfig))
            openvas.appendChild(openvas_config)
        setting.appendChild(openvas)

        oval = f.createElement('oval')
        oval.setAttribute('using', str(int(self.ifoval)))
        if self.ifoval:
            num = len(self.ovalconfig)
            oval.setAttribute('num', str(num))
            for i in range(num):
                config = f.createElement('config')
                config.setAttribute('name', self.ovalconfig[i])
                oval.appendChild(config)
        setting.appendChild(oval)

        with open(self.path + 'setting.set', 'w') as f:
            f.write(setting.toprettyxml(indent='\t', encoding='utf-8'))
        return

    def load(self):
        try:
            f = minidom.parse(self.path+'setting.set')
        except:
            __import__('shutil').rmtree(self.path)
            return 1
        root = f.documentElement
        name = root.getElementsByTagName('name')[0]
        host = root.getElementsByTagName('host')[0]
        comment = root.getElementsByTagName('comment')[0]
        openvas = root.getElementsByTagName('openvas')[0]
        oval = root.getElementsByTagName('oval')[0]

        self.name = name.childNodes[0].nodeValue
        self.IP = host.childNodes[0].nodeValue
        try:
            self.comment = comment.childNodes[0].nodeValue
        except:
            self.comment = ''
        self.ifopenvas = bool(int(openvas.getAttribute('using')))
        if self.ifopenvas:
            config = openvas.getElementsByTagName('config')[0]
            self.openvasconfig = config.childNodes[0].nodeValue
            self.openvasid = openvas.getAttribute('id')
        self.ifoval = bool(int(oval.getAttribute('using')))
        if self.ifoval:
            config = oval.getElementsByTagName('config')
            for i in config:
                self.ovalconfig.append(i.getAttribute('name'))
        return 0
