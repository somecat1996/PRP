# -*- coding: utf-8 -*-

import wx
import wx.py.images
import settings
from my_scanner_openvas import *
from tasks_manager import *


class MyFrame(wx.Frame):
    def __init__(self, Parent=None, ID=-1, Title=None, Pos=(100, 100), Size=(800, 600)):
        self.task_id = []
        self.tasks = TaskManager()

        self.frame = wx.Frame.__init__(self, parent=Parent, id=ID, title=Title, pos=Pos, size=Size)

        self.top_splitter = wx.SplitterWindow(self, -1, style=wx.SP_3D)
        self.sec_splitter = wx.SplitterWindow(self.top_splitter, -1, style=wx.SP_3D)

        self.panel1 = wx.Panel(self.sec_splitter, -1)
        self.panel2 = wx.Panel(self.top_splitter, -1)
        self.panel3 = wx.Panel(self.sec_splitter, -1)

        self.lst = wx.ListBox(self.panel2, style=wx.LB_SINGLE)
        self.a = wx.BoxSizer(wx.HORIZONTAL)
        self.b = wx.BoxSizer(wx.HORIZONTAL)
        self.text1 = wx.TextCtrl(self.panel1, style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.text2 = wx.TextCtrl(self.panel3, style=wx.TE_MULTILINE|wx.TE_READONLY)

        self.Splitter()

        self.toolbar = self.CreateToolBar()
        self.statusbar = self.CreateStatusBar()
        self.menubar = wx.MenuBar()

        self.ToolBar()
        self.StatusBar()
        self.MenuBar()

        self.Centre()

    def Splitter(self):
        self.Panel1()
        self.Panel2()
        self.Panel3()

        self.sec_splitter.SplitHorizontally(self.panel3, self.panel1)
        self.sec_splitter.SetSashGravity(0.5)
        self.top_splitter.SplitVertically(self.panel2, self.sec_splitter)
        self.top_splitter.SetSashGravity(0.2)

    def Panel1(self):
        self.b.Add(self.text1, 1, wx.EXPAND)
        self.panel1.SetSizerAndFit(self.b)

    def OnTreeListCtrlClickFunc(self, event):
        num = self.lst.GetSelection()
        self.text2.SetValue(self.tasks.tasks[num].get_setting())

    def Panel2(self):
        self.update_lst()
        self.lst.Bind(wx.EVT_LISTBOX, self.OnTreeListCtrlClickFunc)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(self.lst, 1, wx.EXPAND)
        self.panel2.SetSizer(hbox1, wx.ALL)

    def update_lst(self):
        print 'done'
        self.lst.Clear()
        tasks = []
        self.task_id = []
        self.tasks.load()
        for i in self.tasks.tasks:
            tasks.append(i.setting.name)
            self.task_id.append(i.setting.id)
        self.lst.Set(tasks)

    def Panel3(self):
        self.a.Add(self.text2, 1, wx.EXPAND)
        self.panel3.SetSizerAndFit(self.a)

    def ToolBar(self):
        img1 = wx.Image('bitmaps/setting.png', wx.BITMAP_TYPE_PNG).Rescale(25, 25)
        img2 = wx.Image('bitmaps/start.png', wx.BITMAP_TYPE_PNG).Rescale(25, 25)
        img3 = wx.Image('bitmaps/pause.png', wx.BITMAP_TYPE_PNG).Rescale(25, 25)
        img4 = wx.Image('bitmaps/stop.png', wx.BITMAP_TYPE_PNG).Rescale(25, 25)
        img5 = wx.Image('bitmaps/report.png', wx.BITMAP_TYPE_PNG).Rescale(25, 25)
        img6 = wx.Image('bitmaps/assistance.png', wx.BITMAP_TYPE_PNG).Rescale(25, 25)
        img7 = wx.Image('bitmaps/quit.png', wx.BITMAP_TYPE_PNG).Rescale(25, 25)

        toobar1 = self.toolbar.AddSimpleTool(wx.NewId(), img1.ConvertToBitmap(), u"参数设置", u"设置扫描参数")
        self.toolbar.AddSeparator()
        toobar2 = self.toolbar.AddSimpleTool(wx.NewId(), img2.ConvertToBitmap(), u"开始", u"开始当前扫描")
        toobar3 = self.toolbar.AddSimpleTool(wx.NewId(), img3.ConvertToBitmap(), u"暂停", u"暂停当前扫描")
        toobar4 = self.toolbar.AddSimpleTool(wx.NewId(), img4.ConvertToBitmap(), u"停止", u"暂停当前扫描")
        self.toolbar.AddSeparator()
        toobar5 = self.toolbar.AddSimpleTool(wx.NewId(), img5.ConvertToBitmap(), u"检测报告", u"打开检测报告")
        self.toolbar.AddSeparator()
        toobar6 = self.toolbar.AddSimpleTool(wx.NewId(), img6.ConvertToBitmap(), u"帮助", u"打开使用说明")
        self.toolbar.AddSeparator()
        toobar7 = self.toolbar.AddSimpleTool(wx.NewId(), img7.ConvertToBitmap(), u"退出", u"退出程序")

        self.Bind(wx.EVT_TOOL, self.open_setting, toobar1)
        self.Bind(wx.EVT_TOOL, self.start_scanning, toobar2)
        self.Bind(wx.EVT_TOOL, self.pause_scanning, toobar3)
        self.Bind(wx.EVT_TOOL, self.stop_scanning, toobar4)
        self.Bind(wx.EVT_TOOL, self.open_reports, toobar5)
        self.Bind(wx.EVT_TOOL, self.open_assistance, toobar6)
        self.Bind(wx.EVT_TOOL, self.menu_quit, toobar7)

        self.toolbar.Realize()

    def StatusBar(self):
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([-1, -1])

    def MenuBar(self):
        menu_f = wx.Menu()
        menu_f1 = menu_f.Append(wx.NewId(), u'开始扫描(&S)', u'开始一个扫描')
        menu_f2 = menu_f.Append(wx.NewId(), u'暂停扫描(&P)', u'暂停当前扫描')
        menu_f3 = menu_f.Append(wx.NewId(), u'停止扫描(&K)', u'停止当前扫描')
        menu_f.AppendSeparator()
        menu_f4 = menu_f.Append(wx.NewId(), u'退出(&Q)', u'退出本程序')

        menu_s = wx.Menu()
        menu_s1 = menu_s.Append(wx.NewId(), u'扫描设置', u'配置扫描选项')

        menu_c = wx.Menu()
        menu_c1 = menu_c.Append(wx.NewId(), u'(&R)扫描报告', u'查看扫描报告')

        menu_t = wx.Menu()
        menu_t1 = menu_t.Append(wx.NewId(), u'物理地址查询')
        menu_t2 = menu_t.Append(wx.NewId(), u'ARP query')
        menu_t3 = menu_t.Append(wx.NewId(), u'Whois')
        menu_t4 = menu_t.Append(wx.NewId(), u'Trace route')
        menu_t5 = menu_t.Append(wx.NewId(), u'Ping')
        menu_t.AppendSeparator()
        menu_t6 = menu_t.Append(wx.NewId(), u'Install WinPCap')

        menu_l = wx.Menu()
        menu_l1 = menu_l.Append(wx.NewId(), u'简体中文', u'更换语言为简体中文')
        menu_l2 = menu_l.Append(wx.NewId(), u'English', u'Change the language into English')

        menu_h = wx.Menu()
        menu_h1 = menu_h.Append(wx.NewId(), u'使用说明', u'打开使用说明')

        self.menubar.Append(menu_f, u'文件')
        self.menubar.Append(menu_s, u'设置')
        self.menubar.Append(menu_c, u'查看')
        self.menubar.Append(menu_t, u'工具')
        self.menubar.Append(menu_l, u'语言')
        self.menubar.Append(menu_h, u'帮助')
        self.SetMenuBar(self.menubar)

        self.Bind(wx.EVT_MENU, self.start_scanning, menu_f1)
        self.Bind(wx.EVT_MENU, self.pause_scanning, menu_f2)
        self.Bind(wx.EVT_MENU, self.stop_scanning, menu_f3)
        self.Bind(wx.EVT_MENU, self.menu_quit, menu_f4)
        self.Bind(wx.EVT_MENU, self.open_setting, menu_s1)
        self.Bind(wx.EVT_MENU, self.open_reports, menu_c1)
        self.Bind(wx.EVT_MENU, self.set_simplified_chinese, menu_l1)
        self.Bind(wx.EVT_MENU, self.set_english, menu_l1)
        self.Bind(wx.EVT_MENU, self.open_assistance, menu_h1)

    def start_scanning(self, event):
        num = self.lst.GetSelection()
        if num == -1:
            dlg = wx.MessageDialog(None, u'未选择扫描任务', u'提示')
            result = dlg.ShowModal()
            dlg.Destroy()
            return
        dlg = wx.MessageDialog(None, u'您确定要开始扫描吗？', u'提示')
        result = dlg.ShowModal()
        dlg.Destroy()
        if not result:
            return
        else:
            self.tasks.tasks[num].start_scanning()

    def pause_scanning(self, event):
        dlg = wx.MessageDialog(None, u'您确定要暂停扫描吗？', u'提示')

    def stop_scanning(self, event):
        dlg = wx.MessageDialog(None, u'您确定要停止扫描吗？', u'提示')

    def menu_quit(self, event):
        dlg = wx.MessageDialog(None, u'您确定要退出吗？', u'提示')
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Close()

    def open_setting(self, event):
        self.Disable()
        setting = settings.MySetting(self)
        setting.Show(True)

    def test(self, event):
        print 'aaa'
        event.Skip()

    def open_reports(self, event):
        pass

    def set_simplified_chinese(self, event):
        pass

    def set_english(self, event):
        pass

    def open_assistance(self, event):
        pass


class MyApp(wx.App):
    def OnInit(self):
        self.myframe = MyFrame(Title=u'漏洞扫描')
        self.SetTopWindow(self.myframe)
        self.myframe.Show(True)
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
