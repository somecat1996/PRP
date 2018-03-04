# -*- coding: utf-8 -*-

import wx
import os
import wx.grid
from tasks_manager import Task
from my_scanner_openvas.my_commnds import create_task, create_target


class MySetting(wx.Frame):
    def __init__(self, Parent=None, Title=u'设置'):
        self.frame = wx.Frame.__init__(self, parent=Parent, title=Title, size=(600, 400),
                                       style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT)

        self.items = [u'扫描任务设置', u'oval设置', u'openvas设置']

        self.all()
        self.CentreOnParent()
        self.parent = Parent

        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnTreeListCtrlClickFunc(self, event):
        if self.TC.GetItemData(event.GetItem()) is not None:
            num1 = str(self.TC.GetItemData(event.GetItem()).GetData())
            num1 = int(num1)
            if num1 == 2:
                self.listbox_2()
            elif num1 == 0:
                self.listbox_0()
            elif num1 == 1:
                self.listbox_1()

    def OnClose(self, event):
        self.Parent.Enable(True)
        event.Skip()

    def cancel_close(self, event):
        self.Parent.Enable(True)
        self.Close()

    def save_close(self, event):
        task = Task()
        task.create0()
        task.setting.name = self.textctrl_0_0.GetValue()
        task.setting.IP = self.textctrl_0_1.GetValue()
        task.setting.comment = self.textctrl_0_2.GetValue()
        task.setting.ifopenvas = self.CheckBox_0_1.GetValue()
        task.setting.ifoval = self.CheckBox_0_0.GetValue()
        task.setting.openvasid = ''
        task.setting.openvasconfig = ''
        if task.setting.ifopenvas:
            task.setting.openvasconfig = self.choice.GetStringSelection()
            task.create1()
            task.setting.openvasid = task.openvas.task.id
        task.setting.ovalconfig = []
        if task.setting.ifoval:
            tmp = self.checkbox.GetCheckedStrings()
            for i in tmp:
                task.setting.ovalconfig.append(i)
        task.save()

        self.Parent.Enable(True)
        self.Parent.tasks.load()
        self.Parent.update_lst()

        self.Close()

    def load(self, event):
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "Open paint file...",
                            os.getcwd(),
                            style=wx.OPEN,
                            wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            pass
        dlg.Destroy()

    def save(self, event):

        file_wildcard = "Setting files(*.set)|*.set"
        dlg = wx.FileDialog(self,
                            "Save paint as ...",
                            os.getcwd(),
                            style=wx.SAVE | wx.OVERWRITE_PROMPT,
                            wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            pass
        dlg.Destroy()

    def Splitter(self):

        self.top_splitter = wx.SplitterWindow(self)
        self.sec_splitter = wx.SplitterWindow(self.top_splitter)

        self.panel1 = wx.Panel(self.top_splitter, -1, size=(400, 400))
        self.panel2 = wx.Panel(self.sec_splitter, -1, size=(200, 280))
        self.panel3 = wx.Panel(self.sec_splitter, -1, size=(200, 120))

        self.lable = wx.StaticText(self.panel1, -1, u'扫描设置')

        self.TC = wx.TreeCtrl(self.panel2, -1)
        self.TC.root = self.TC.AddRoot(u'设置')
        IDs = self.items
        for item in range(3):
            data = wx.TreeItemData(str(item))
            child = self.TC.AppendItem(self.TC.root, IDs[item], data=data)
            childTitle = IDs[item]
            self.TC.SetItemText(child, childTitle)
        self.TC.Expand(self.TC.root)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnTreeListCtrlClickFunc, self.TC)

        self.button_load = wx.Button(self.panel3, -1, u'载入', (10, 10), (80, 40))
        self.button_save = wx.Button(self.panel3, -1, u'保存', (100, 10), (80, 40))
        self.button_ok = wx.Button(self.panel3, -1, u'确定', (10, 70), (80, 40))
        self.button_cancel = wx.Button(self.panel3, -1, u'取消', (100, 70), (80, 40))

        self.Bind(wx.EVT_BUTTON, self.load, self.button_load)
        self.Bind(wx.EVT_BUTTON, self.save, self.button_save)
        self.Bind(wx.EVT_BUTTON, self.save_close, self.button_ok)
        self.Bind(wx.EVT_BUTTON, self.cancel_close, self.button_cancel)

        # self.Bind(wx.EVT_LISTBOX, self.listbox_click, self.lst)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # hbox1.Add(self.lst, 1, wx.EXPAND)
        hbox1.Add(self.TC, 1, wx.EXPAND)

        self.panel2.SetSizer(hbox1, wx.ALL)
        self.sec_splitter.SetSashGravity(0.3)
        self.sec_splitter.SplitHorizontally(self.panel2, self.panel3)
        self.top_splitter.SplitVertically(self.sec_splitter, self.panel1)
        self.top_splitter.SetSashGravity(0.3)
        pass

    def settings_0(self):
        self.CheckBox_0_0 = wx.CheckBox(self.panel1, -1, u'使用OVAL框架扫描', (10, 10))
        self.CheckBox_0_0.SetValue(True)
        self.Bind(wx.EVT_CHECKBOX, self.disable_settings_0, self.CheckBox_0_0)


        self.CheckBox_0_1 = wx.CheckBox(self.panel1, -1, u'使用openvas框架扫描', (180, 10))
        self.CheckBox_0_1.SetValue(True)
        self.Bind(wx.EVT_CHECKBOX, self.disable_settings_1, self.CheckBox_0_1)

        self.label_0_0 = wx.StaticText(self.panel1, -1, u'名称', (10, 33))

        self.textctrl_0_0 = wx.TextCtrl(self.panel1, pos=(10, 60), size=(360, 24))
        self.textctrl_0_0.SetValue('unnamed')

        self.label_0_1 = wx.StaticText(self.panel1, -1, u'指定IP范围', (10, 93))

        self.ExampleButton_0_0 = wx.Button(self.panel1, -1, u'示例', (90, 90), (60, 25))
        self.Bind(wx.EVT_BUTTON, self.examples, self.ExampleButton_0_0)

        self.textctrl_0_1 = wx.TextCtrl(self.panel1, pos=(10, 120), size=(360, 24))

        self.label_0_3 = wx.StaticText(self.panel1, -1, u'添加备注（选填）', (10, 153))

        self.textctrl_0_2 = wx.TextCtrl(self.panel1, pos=(10, 180), size=(360, 180), style=wx.TE_MULTILINE)

        self.CheckBox_0_0.Hide()
        self.CheckBox_0_1.Hide()
        self.label_0_0.Hide()
        self.textctrl_0_0.Hide()
        self.label_0_1.Hide()
        self.ExampleButton_0_0.Hide()
        self.textctrl_0_1.Hide()
        self.label_0_3.Hide()
        self.textctrl_0_2.Hide()
        pass

    def disable_settings_0(self, event):
        an = event.GetEventObject()
        if an.GetValue():
            self.checkbox.Enable()
        else:
            self.checkbox.Disable()


    def disable_settings_1(self, event):
        an = event.GetEventObject()
        if an.GetValue():
            self.choice.Enable()
        else:
            self.choice.Disable()

    def listbox_0(self):
        self.all_invisible()

        self.CheckBox_0_0.Show()
        self.CheckBox_0_1.Show()
        self.label_0_0.Show()
        self.textctrl_0_0.Show()
        self.label_0_1.Show()
        self.ExampleButton_0_0.Show()
        self.textctrl_0_1.Show()
        self.label_0_3.Show()
        self.textctrl_0_2.Show()
        pass

    def settings_1(self):
        self.lable_1_0 = wx.StaticText(self.panel1, -1, u'选择扫描类型列表', (10, 13))
        self.checkbox = wx.CheckListBox(self.panel1, -1, (10, 40), (200, 300),
                                        ['test0', 'test1', 'test2', 'test3', 'test4'])

        self.lable_1_0.Hide()
        self.checkbox.Hide()

    def listbox_1(self):
        self.all_invisible()

        self.lable_1_0.Show()
        self.checkbox.Show()
        return

    def settings_2(self):
        self.label_2_0 = wx.StaticText(self.panel1, -1, u'选择扫描方式', (10, 13))

        self.choice = wx.Choice(self.panel1, -1, (10, 40), (200, 24),
                                choices=['empty', 'Discovery', 'System Discovery', 'Host Discovery', 'Full and fast', 'Full and very deep', 'Full and fast ultimate', 'Full and very deep ultimate'])
        self.choice.SetSelection(0)

        self.label_2_0.Hide()
        self.choice.Hide()

    def listbox_2(self):
        self.all_invisible()

        self.label_2_0.Show()
        self.choice.Show()

    def all_invisible(self):
        self.lable.Hide()

        self.CheckBox_0_0.Hide()
        self.CheckBox_0_1.Hide()
        self.label_0_0.Hide()
        self.textctrl_0_0.Hide()
        self.label_0_1.Hide()
        self.ExampleButton_0_0.Hide()
        self.textctrl_0_1.Hide()
        self.label_0_3.Hide()
        self.textctrl_0_2.Hide()

        self.lable_1_0.Hide()
        self.checkbox.Hide()

        self.label_2_0.Hide()
        self.choice.Hide()

    def examples(self, event):
        text = u'''有效格式：
    192.168.0.1
    192.168.0.1/24
    192.168.1.1-192.168.2.100
    192.168.0.1,192.168.1.1-10,192.186.2.1/24

无效格式：
    192.168.0-1.1
    192.168.0.1-1.254
    192.168.0/24.1
    192.168.0.*'''
        dlg = wx.MessageDialog(None, text, u'示例')
        result = dlg.ShowModal()
        dlg.Destroy()
        pass

    def IPLoad(self, event):
        file_wildcard = "Txt files(*.txt)|*.txt"
        dlg = wx.FileDialog(self, "Open paint file...",
                            os.getcwd(),
                            style=wx.OPEN,
                            wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            pass
        dlg.Destroy()

    def all(self):
        self.Splitter()
        self.settings_0()
        self.settings_1()
        self.settings_2()
