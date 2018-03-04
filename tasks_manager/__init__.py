# -*- coding: utf-8
from Task import *


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load()

    def load(self):
        self.tasks = []
        path = 'tasks/'
        if not os.path.exists(path):
            os.mkdir(path)
        files = os.listdir(path)
        for id in files:
            task = Task()
            task.load(id)
            self.tasks.append(task)

    def get(self, id):
        for i in self.tasks:
            if id == i.setting.id:
                return i
        return None
