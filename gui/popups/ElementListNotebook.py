import sys
import wx
import wx.lib.mixins.listctrl as listmix


# FOR USE LATER IN GREATER GUI
listctrldata = {
1 : ("", "", ""),
2 : ("", "", ""),
3 : ("", "", ""),
4 : ("", "", ""),
5 : ("", "", ""),
6 : ("", "", ""),
}


class ElementListCtrl(wx.ListCtrl,
                   listmix.ListCtrlAutoWidthMixin,
                   listmix.TextEditMixin):

    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self.Populate()
        listmix.TextEditMixin.__init__(self)

    def Populate(self):
        # for normal, simple columns, you can add them like this:
        self.InsertColumn(0, "Node No.")
        self.InsertColumn(1, "Name")
        self.InsertColumn(2, "Type")
        self.InsertColumn(3, "Label")
        self.InsertColumn(4, "Method")
        self.InsertColumn(5, "Pressure")
        self.InsertColumn(5, "Temperature")
        self.InsertColumn(5, "W. Cut-Off Pres.")
        self.InsertColumn(5, "W. Exp.")


        items = listctrldata.items()
        for key, data in items:
            index = self.InsertStringItem(sys.maxint, data[0])
            self.SetStringItem(index, 1, data[1])
            self.SetStringItem(index, 2, data[2])
            self.SetItemData(index, key)

        self.SetColumnWidth(0, 80)
        self.SetColumnWidth(1, 80)
        self.SetColumnWidth(2, 80)
        self.SetColumnWidth(3, 80)
        self.SetColumnWidth(4, 80)
        self.SetColumnWidth(5, 80)
        self.SetColumnWidth(6, 80)
        self.SetColumnWidth(7, 80)
        self.SetColumnWidth(8, 80)
        self.currentItem = 0


class ElementListCtrlPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)

        tID = wx.NewId()

        sizer = wx.BoxSizer(wx.VERTICAL)

        if wx.Platform == "__WXMAC__" and \
               hasattr(wx.GetApp().GetTopWindow(), "LoadDemo"):
            self.useNative = wx.CheckBox(self, -1, "Use native listctrl")
            self.useNative.SetValue(
                not wx.SystemOptions.GetOptionInt("mac.listctrl.always_use_generic") )
            self.Bind(wx.EVT_CHECKBOX, self.OnUseNative, self.useNative)
            sizer.Add(self.useNative, 0, wx.ALL | wx.ALIGN_RIGHT, 4)

        self.list = ElementListCtrl(self, tID,
                                 style=wx.LC_REPORT
                                 | wx.BORDER_NONE
                                 | wx.LC_SORT_ASCENDING
                                 )

        sizer.Add(self.list, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetAutoLayout(True)


    def OnUseNative(self, event):
        wx.SystemOptions.SetOptionInt("mac.listctrl.always_use_generic", not event.IsChecked())
        wx.GetApp().GetTopWindow().LoadDemo("ListCtrl_edit")


class ElementListDialog(wx.Dialog):

    def __init__(self, *args, **kw):
        super(ElementListDialog, self).__init__(*args, **kw)
        self.SetBackgroundColour("WHITE")
        self.InitUI()
        self.SetSize((800, 500))
        self.SetTitle("Element List")
        self.Center(True)


    def InitUI(self):

        panel = ElementListCtrlPanel(self)
        panel.SetBackgroundColour("WHITE")

        topsizer = wx.BoxSizer(wx.VERTICAL)
        sizer1 = wx.BoxSizer(wx.VERTICAL)

        # panel.SetSizer(sizer1)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        closeButton = wx.Button(self, label='Close')
        hbox2.Add(closeButton, flag=wx.ALIGN_RIGHT | wx.ALL, border=5)

        topsizer.Add(panel, proportion=1,
            flag=wx.ALL|wx.EXPAND, border=5)
        topsizer.Add(hbox2,
            flag=wx.ALIGN_RIGHT|wx.ALL, border=10)

        self.SetSizer(topsizer)

        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)


    def OnClose(self, e):

        self.Destroy()

########################################################################
class DemoFrame(wx.Frame):
    """
    Frame that holds all other widgets
    """

    #----------------------------------------------------------------------
    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Element List",
                          size=(800, 600)
                          )
        panel = wx.Panel(self)
        self.tab_num = 3

        self.notebook = wx.Notebook(panel)
        NodeTab = ElementListCtrlPanel(self.notebook)
        self.notebook.AddPage(NodeTab, "Nodes")

        PipesTab = ElementListCtrlPanel(self.notebook)
        self.notebook.AddPage(PipesTab, "Pipes")

        ValvesTab = ElementListCtrlPanel(self.notebook)
        self.notebook.AddPage(ValvesTab, "Valves")

        CompressorsTab = ElementListCtrlPanel(self.notebook)
        self.notebook.AddPage(CompressorsTab, "Compressors")

        RegulatorsTab = ElementListCtrlPanel(self.notebook)
        self.notebook.AddPage(RegulatorsTab, "Regulators")

        LossElementsTab = ElementListCtrlPanel(self.notebook)
        self.notebook.AddPage(LossElementsTab, "Loss Elements")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.ALL|wx.EXPAND, 5)

        btn = wx.Button(panel, label="Close")
        # PUT IN CLOSE METHOD
        sizer.Add(btn, flag=wx.ALIGN_RIGHT|wx.ALL, border=10)

        panel.SetSizer(sizer)
        self.Layout()
        self.Centre(True)
        self.Show()

    #----------------------------------------------------------------------


#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = DemoFrame()
    app.MainLoop()