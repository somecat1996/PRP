# -*- coding: utf-8 -*-

import wx
import os
import wx.grid


class MySetting(wx.Frame):
    def __init__(self, Parent=None, Title=u'设置'):
        self.frame = wx.Frame.__init__(self, parent=Parent, title=Title, size=(600, 400),
                                       style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_FLOAT_ON_PARENT)

        self.items = {u'openvas设置': [], u'oval设置': [],
                      u'监听设置': [u'端口相关设置', u'SNMP相关设置', u'NETBIOS相关设置', u'漏洞检测脚本设置', u'CGI相关设置', u'字典文件设置']}

        self.all()
        self.CentreOnParent()
        self.parent = Parent

        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnTreeListCtrlClickFunc(self, event):
        if self.TC.GetItemData(event.GetItem()) is not None:
            num1, num2 = str(self.TC.GetItemData(event.GetItem()).GetData()).split("|")
            num1, num2 = int(num1), int(num2)
            if num1 == 2:
                self.listbox_0()
            elif num1 == 0:
                if num2 == 0:
                    self.listbox_1()
                elif num2 == 1:
                    self.listbox_2()
                elif num2 == 2:
                    self.listbox_3()
                elif num2 == 3:
                    self.listbox_4()
                elif num2 == 4:
                    self.listbox_5()
            elif num1 == 1:
                if num2 == 0:
                    self.listbox_6()
                elif num2 == 1:
                    self.listbox_7()
                elif num2 == 2:
                    self.listbox_8()
                elif num2 == 3:
                    self.listbox_9()
                elif num2 == 4:
                    self.listbox_10()
                elif num2 == 5:
                    self.listbox_11()
                elif num2 == 6:
                    self.listbox_12()

    def OnClose(self, event):
        self.Parent.Enable(True)
        event.Skip()

    def cancel_close(self, event):
        self.Parent.Enable(True)
        self.Close()

    def save_close(self, event):
        self.Parent.Enable(True)
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
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*"
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
        IDs = self.items.keys()
        for item in [2, 0, 1]:
            data = wx.TreeItemData(str(item) + "|0")
            child = self.TC.AppendItem(self.TC.root, IDs[item], data=data)
            lastList = self.items.get(IDs[item], [])
            childTitle = IDs[item]
            self.TC.SetItemText(child, childTitle)
            for index in range(len(lastList)):
                college = lastList[index]
                # TreeItemData是每一个ChildItem的唯一标示
                # 以便在点击事件中获得点击项的位置信息
                data = wx.TreeItemData(str(item) + "|" + str(index + 1))
                last = self.TC.AppendItem(child, str(index), data=data)
                self.TC.SetItemText(last, college)
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

    def listbox_0(self):
        self.all_invisible()

        self.CheckBox_0_0.Show()
        self.ExampleButton_0_0.Show()
        self.IPList_0_0.Show()
        self.gridTable_0.Show()
        self.FileLoad_0_0.Show()

        self.CheckBox_0_1.Show()
        self.ExampleButton_0_1.Show()
        self.IPList_0_1.Show()
        self.gridTable_1.Show()
        self.FileLoad_0_1.Show()
        pass

    def listbox_1(self):
        self.all_invisible()
        self.lable.SetLabel(u'本设置模块包含所有全局性扫描选项')
        self.lable.Show()

    def listbox_2(self):
        self.all_invisible()
        pass

    def listbox_3(self):
        self.all_invisible()
        pass

    def listbox_4(self):
        self.all_invisible()

        self.Lable_1_3_1.Show()
        self.Label_1_3_2.Show()
        self.Label_1_3_3.Show()

        self.CheckBox_1_3_1.Show()
        self.CheckBox_1_3_2.Show()

        self.TextCtrl_1_3_1.Show()
        self.TextCtrl_1_3_2.Show()
        pass

    def listbox_5(self):
        self.all_invisible()

        self.RadioBox_1_4.Show()
        self.CheckButton_1_4_1.Show()
        self.CheckButton_1_4_2.Show()
        self.CheckButton_1_4_3.Show()
        pass

    def listbox_6(self):
        self.all_invisible()
        self.lable.SetLabel(u'本设置模块包含各扫描插件的相关选项')
        self.lable.Show()

    def listbox_7(self):
        self.all_invisible()
        pass

    def listbox_8(self):
        self.all_invisible()
        pass

    def listbox_9(self):
        self.all_invisible()
        pass

    def listbox_10(self):
        self.all_invisible()
        pass

    def listbox_11(self):
        self.all_invisible()
        pass

    def listbox_12(self):
        self.all_invisible()
        pass

    def all_invisible(self):
        self.lable.Hide()
        self.lable_0.Hide()



        self.CheckBox_0_0.Hide()
        self.ExampleButton_0_0.Hide()
        self.IPList_0_0.Hide()
        self.gridTable_0.Hide()
        self.FileLoad_0_0.Hide()

        self.CheckBox_0_1.Hide()
        self.ExampleButton_0_1.Hide()
        self.IPList_0_1.Hide()
        self.gridTable_1.Hide()
        self.FileLoad_0_1.Hide()

        self.RadioBox_1_4.Hide()
        self.CheckButton_1_4_1.Hide()
        self.CheckButton_1_4_2.Hide()
        self.CheckButton_1_4_3.Hide()

        self.Lable_1_3_1.Hide()
        self.Label_1_3_2.Hide()
        self.Label_1_3_3.Hide()

        self.CheckBox_1_3_1.Hide()
        self.CheckBox_1_3_2.Hide()

        self.TextCtrl_1_3_1.Hide()
        self.TextCtrl_1_3_2.Hide()

    def settings_0_0_add(self, event):
        self.gridTable_0.AppendRows(numRows=1)

    def settings_0_1_add(self, event):
        self.gridTable_1.AppendRows(numRows=1)

    def disable_settings_0_0(self, event):
        cb = event.GetEventObject()
        if cb.GetValue():
            self.ExampleButton_0_0.Enable()
            self.IPList_0_0.Enable()
            self.gridTable_0.Enable()
            self.FileLoad_0_0.Enable()
        else:
            self.ExampleButton_0_0.Disable()
            self.IPList_0_0.Disable()
            self.gridTable_0.Disable()
            self.FileLoad_0_0.Disable()

    def disable_settings_0_1(self, event):
        cb = event.GetEventObject()
        if cb.GetValue():
            self.ExampleButton_0_1.Enable()
            self.IPList_0_1.Enable()
            self.gridTable_1.Enable()
            self.FileLoad_0_1.Enable()
        else:
            self.ExampleButton_0_1.Disable()
            self.IPList_0_1.Disable()
            self.gridTable_1.Disable()
            self.FileLoad_0_1.Disable()

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

    def settings_0(self):

        self.lable_0 = wx.StaticText(self.panel1, -1, u'指定IP范围', (10, 10))
        self.lable_0.Hide()

        self.CheckBox_0_0 = wx.CheckBox(self.panel1, -1, u'使用OVAL框架扫描', (10, 30))
        self.CheckBox_0_0.SetValue(True)
        self.Bind(wx.EVT_CHECKBOX, self.disable_settings_0_0, self.CheckBox_0_0)
        self.CheckBox_0_0.Hide()

        self.ExampleButton_0_0 = wx.Button(self.panel1, -1, u'示例', (160, 25), (60, 25))
        self.ExampleButton_0_0.Hide()
        self.Bind(wx.EVT_BUTTON, self.examples, self.ExampleButton_0_0)

        self.IPList_0_0 = wx.Button(self.panel1, -1, u'添加', (230, 25), (60, 25))
        self.IPList_0_0.Hide()
        self.Bind(wx.EVT_BUTTON, self.settings_0_0_add, self.IPList_0_0)

        self.FileLoad_0_0 = wx.Button(self.panel1, -1, u'从文件中导入', (300, 25), (90, 25))
        self.FileLoad_0_0.Hide()
        self.Bind(wx.EVT_BUTTON, self.IPLoad, self.FileLoad_0_0)

        self.gridTable_0 = wx.grid.Grid(self.panel1, -1, pos=(10, 60), size=(380, 117), style=wx.WANTS_CHARS)
        self.gridTable_0.CreateGrid(4, 2)
        self.gridTable_0.SetColLabelValue(0, u"名称" )
        self.gridTable_0.SetColLabelValue(1, u"IP地址")
        self.gridTable_0.SetRowLabelSize(20)
        self.gridTable_0.EnableDragRowSize(False)
        self.gridTable_0.SetColSize(0, 80)
        self.gridTable_0.SetColSize(1, 280)
        self.gridTable_0.Hide()

        self.CheckBox_0_1 = wx.CheckBox(self.panel1, -1, u'使用OpenVas框架扫描', (10, 200))
        self.CheckBox_0_1.SetValue(True)
        self.Bind(wx.EVT_CHECKBOX, self.disable_settings_0_1, self.CheckBox_0_1)
        self.CheckBox_0_1.Hide()

        self.ExampleButton_0_1 = wx.Button(self.panel1, -1, u'示例', (160, 195), (60, 25))
        self.ExampleButton_0_1.Hide()
        self.Bind(wx.EVT_BUTTON, self.examples, self.ExampleButton_0_1)

        self.IPList_0_1 = wx.Button(self.panel1, -1, u'添加', (230, 195), (60, 25))
        self.IPList_0_1.Hide()
        self.Bind(wx.EVT_BUTTON, self.settings_0_1_add, self.IPList_0_1)

        self.FileLoad_0_1 = wx.Button(self.panel1, -1, u'从文件中导入', (300, 195), (90, 25))
        self.FileLoad_0_1.Hide()
        self.Bind(wx.EVT_BUTTON, self.IPLoad, self.FileLoad_0_1)

        self.gridTable_1 = wx.grid.Grid(self.panel1, -1, pos=(10, 230), size=(380, 117), style=wx.WANTS_CHARS)
        self.gridTable_1.CreateGrid(4, 2)
        self.gridTable_1.SetColLabelValue(0, u"名称")
        self.gridTable_1.SetColLabelValue(1, u"IP地址")
        self.gridTable_1.SetRowLabelSize(20)
        self.gridTable_1.EnableDragRowSize(False)
        self.gridTable_1.SetColSize(0, 80)
        self.gridTable_1.SetColSize(1, 280)
        self.gridTable_1.Hide()

    def settings_1_1(self):
        pass

    def settings_1_2(self):
        pass

    def hostlist_if(self, event):
        flag = event.GetEventObject()
        if flag.GetValue():
            self.TextCtrl_1_3_2.Enable()
        else:
            self.TextCtrl_1_3_2.Disable()

    def settings_1_3(self):
        self.Lable_1_3_1 = wx.StaticText(self.panel1, -1, u'报告文件：', (30, 30))
        self.Label_1_3_2 = wx.StaticText(self.panel1, -1, u'报告文件类型：', (30, 80))
        self.Label_1_3_3 = wx.StaticText(self.panel1, -1, u'列表文件：', (30, 200))

        self.CheckBox_1_3_1 = wx.CheckBox(self.panel1, -1, u'保存主机列表', (30, 170))
        self.CheckBox_1_3_1.SetValue(False)
        self.CheckBox_1_3_2 = wx.CheckBox(self.panel1, -1, u'扫描完成后自动生成并显示报告', (30, 300))
        self.CheckBox_1_3_2.SetValue(True)

        self.TextCtrl_1_3_1 = wx.TextCtrl(self.panel1, -1, 'report', (30, 50), (250, 25))
        self.TextCtrl_1_3_2 = wx.TextCtrl(self.panel1, -1, 'hostlist', (30, 220), (250, 25))
        self.TextCtrl_1_3_2.Disable()
        self.Bind(wx.EVT_CHECKBOX, self.hostlist_if, self.CheckBox_1_3_1)

        self.Lable_1_3_1.Hide()
        self.Label_1_3_2.Hide()
        self.Label_1_3_3.Hide()

        self.CheckBox_1_3_1.Hide()
        self.CheckBox_1_3_2.Hide()

        self.TextCtrl_1_3_1.Hide()
        self.TextCtrl_1_3_2.Hide()
        pass

    def settings_1_4(self):
        lblList = [u'跳过没有响应的主机', u'无条件扫描']
        self.RadioBox_1_4 = wx.RadioBox(self.panel1, label='', pos=(30, 30), choices=lblList,
                                majorDimension=1, style=wx.RA_SPECIFY_COLS)

        self.CheckButton_1_4_1 = wx.CheckBox(self.panel1, -1, u'跳过没有检测到开放端口的主机', (30, 150))
        self.CheckButton_1_4_1.SetValue(True)
        self.CheckButton_1_4_2 = wx.CheckBox(self.panel1, -1, u'使用NMAP判断远程操作系统', (30, 180))
        self.CheckButton_1_4_2.SetValue(True)

        self.CheckButton_1_4_3 = wx.CheckBox(self.panel1, -1, u'显示详细扫描进度', (30, 250))
        self.CheckButton_1_4_3.SetValue(False)

        self.RadioBox_1_4.Hide()
        self.CheckButton_1_4_1.Hide()
        self.CheckButton_1_4_2.Hide()
        self.CheckButton_1_4_3.Hide()
        pass

    def settings_2_1(self):
        pass

    def settings_2_2(self):
        pass

    def settings_2_3(self):
        pass

    def settings_2_4(self):
        pass

    def settings_2_5(self):
        pass

    def settings_2_6(self):
        pass

    def all(self):
        self.Splitter()
        self.settings_0()
        self.settings_1_1()
        self.settings_1_3()
        self.settings_1_4()
