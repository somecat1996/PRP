# coding=utf-8
import os
from setting import *
from my_scanner_openvas import *


class Task:
    def __init__(self):
        self.setting = None
        self.openvas = None
        self.oval = None

    def load(self, id):
        self.setting = Setting(ID=id)
        self.setting.load()
        self.openvas = TaskManager(id=self.setting.id)
        self.openvas.ifopenvas = self.setting.ifopenvas
        if self.setting.ifopenvas:
            self.openvas.read()
        if self.setting.ifoval:
            pass

    def save(self):
        self.setting.save()
        #self.openvas.update(self.setting.openvasid)

    def create0(self):
        self.setting = Setting()

    def create1(self):
        self.openvas = TaskManager(self.setting.id)
        if self.setting.ifopenvas:
            self.openvas.ifopenvas = True
            self.openvas.create_task(self.setting.name, self.setting.IP, self.setting.openvasconfig, self.setting.comment)

    def get_setting(self):
        output = ''
        output += 'id:' + self.setting.id + '\n'
        output += 'name:' + self.setting.name + '\n'
        output += 'target:' + self.setting.IP + '\n'
        output += 'comment:' + self.setting.comment + '\n'
        output += '\n'
        output += 'use openvas:' + str(self.setting.ifopenvas) + '\n'
        if self.setting.ifopenvas:
            output += 'openvas id:' + self.setting.openvasid + '\n'
            output += 'openvas config:' + self.setting.openvasconfig + '\n'
        output += '\n'
        output += 'use oval:' + str(self.setting.ifoval) + '\n'
        if self.setting.ifoval:
            output += 'oval config:' + '\n'
            for i in self.setting.ovalconfig:
                output += '\t' + i + '\n'
        return output

    def start_scanning(self):
        if self.setting.ifoval:
            pass
        if self.setting.ifopenvas:
            self.openvas.start_task()
