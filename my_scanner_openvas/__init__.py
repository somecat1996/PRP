# coding=utf-8
from my_commnds import *
import os
from task import task
from result_manager import *
import re


class TaskManager:
    def __init__(self, id, user='admin', password='admin'):
        self.ifopenvas = False
        self.id = id
        self.user = user
        self.password = password
        self.task = task()

    def update(self, id):
        if self.ifopenvas:
            self.update0(id)
        else:
            return

    def read(self):
        if self.ifopenvas:
            self.read0()
        else:
            return

    def update0(self, id):
        path = 'tasks/' + self.id + '/openvas/'
        response = my_commnds.get_task(self.user, self.password, id)
        #此处应加入对status_text的判断
        self.task.load(response)
        if not os.path.exists(path):
            os.mkdir(path)
        tmp_path = path + self.task.id + '/'
        if not os.path.exists(tmp_path):
            os.mkdir(tmp_path)
        file = open(tmp_path+'info', 'w')
        file.write(response)
        file.close()
        if self.task.finished == '1':
            self.task.result = result_manager(self.task.report_id, self.user, self.password)
            result = self.task.result.get()
            file = open(tmp_path+'result', 'w')
            file.write(result)
            file.close()
        # task_text = re.findall('(<task.*?</task>)', response)
        # for i in task_text:
        #     tmp = task()
        #     tmp.load(i)
        #     flag = True
        #     for j in self.tasks:
        #         if tmp.id == j.id:
        #             flag = False
        #     if flag:
        #         self.tasks.append(tmp)
        #         if not os.path.exists(path):
        #             os.mkdir(path)
        #         tmp_path = path + tmp.id + '/'
        #         if not os.path.exists(tmp_path):
        #             os.mkdir(tmp_path)
        #         file = open(tmp_path+'info', 'w')
        #         file.write(i)
        #         file.close()
        #         if tmp.finished == '1':
        #             tmp.result = result_manager(tmp.report_id, self.user, self.password)
        #             result = tmp.result.get()
        #             file = open(tmp_path+'result', 'w')
        #             file.write(result)
        #             file.close()



    def read0(self):
        path = 'tasks/' + self.id + '/openvas/'
        if not os.path.exists(path):
            os.mkdir(path)
            return
        id = os.listdir(path)[0]
        tmp_path = path + id + '/'
        text_file = open(tmp_path + 'info', 'r')
        text = text_file.read()
        text_file.close()
        self.task = task()
        self.task.load(text)
        if self.task.finished == '1':
            result_file = open(tmp_path + 'result', 'r')
            result = result_file.read()
            result_file.close()
            self.task.result = result_manager(self.task.id, self.user, self.password)
            self.task.result.load(result)

    def start_task(self):
        start_task(self.user, self.password, self.task.id)

    def delete_task(self):
        delete_task(self.user, self.password, self.task.id)

    def resume_task(self):
        resume_task(self.user, self.password, self.task.id)

    def create_task(self, name, target, config, comment=''):
        responce = create_target(self.user, self.password, name+self.id, target, comment)
        target_id = re.findall('id="(.*?)"', responce, re.S)[0]
        config_dir = {'Discovery':'8715c877-47a0-438d-98a3-27c7a6ab2196',
                      'empty':'085569ce-73ed-11df-83c3-002264764cea',
                      'Full and fast':'daba56c8-73ec-11df-a475-002264764cea',
                      'Full and fast ultimate':'698f691e-7489-11df-9d8c-002264764cea',
                      'Full and very deep':'708f25c4-7489-11df-8094-002264764cea',
                      'Full and very deep ultimate':'74db13d6-7489-11df-91b9-002264764cea',
                      'Host Discovery':'2d3f051c-55ba-11e3-bf43-406186ea4fc5',
                      'System Discovery':'bbca7412-a950-11e3-9109-406186ea4fc5'}
        id = CreateTask(name, target_id, config_dir[config], comment, self.user, self.password)
        self.update(id)


def CreateTask(name, target_id, config_id, comment='', user='admin', password='admin'):
    responce = create_task(user, password, name, config_id, target_id, comment)
    task_id = re.findall('id="(.*?)"', responce, re.S)[0]
    return task_id
