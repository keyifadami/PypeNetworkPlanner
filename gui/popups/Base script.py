import wx

class ElementListDialog(wx.Dialog):
    
    def __init__(self, *args, **kw):
        super(ElementListDialog, self).__init__(*args, **kw)
        self.SetBackgroundColour("WHITE")
        self.InitUI()
        self.SetSize((800, 500))
        self.SetTitle("Element List")
        self.Center(True)
        
        
    def InitUI(self):

        panel = wx.Panel(self)
        panel.SetBackgroundColour("WHITE")

        topsizer = wx.BoxSizer(wx.VERTICAL)
        sizer1 = wx.BoxSizer(wx.VERTICAL)

        panel.SetSizer(sizer1)
       
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
        
        
class Example(wx.Frame):
    
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
            
        self.InitUI()
        
        
    def InitUI(self):    
    
        ID_DEPTH = wx.NewId()

        tb = self.CreateToolBar()
        tb.AddLabelTool(id=ID_DEPTH, label='', 
            bitmap=wx.Bitmap('Symbol-warning-small.png'))
        
        tb.Realize()

        self.Bind(wx.EVT_TOOL, self.OnChangeDepth, 
            id=ID_DEPTH)

        self.SetSize((300, 200))
        self.SetTitle('Custom dialog')
        self.Centre()
        self.Show(True)
        
        
    def OnChangeDepth(self, e):
        
        chgdep = ElementListDialog(None,
            title='Change Color Depth')
        chgdep.ShowModal()
        chgdep.Destroy()        


def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()