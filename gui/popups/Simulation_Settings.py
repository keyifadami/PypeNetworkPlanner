import wx

class SimulationSettings(wx.Dialog):
    
    def __init__(self, *args, **kw):
        super(SimulationSettings, self).__init__(*args, **kw)

        self.SetBackgroundColour("WHITE")
        self.InitUI()
        self.SetSize((700, 600))
        self.SetTitle("Simulation Settings")
        self.Centre()
        self.Show(True)
        
    def InitUI(self):

        panel = wx.Panel(self)
        topsizer = wx.BoxSizer(wx.VERTICAL)
        ## upperSizer contains first 2 static boxes
        upperSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        upperSizer2 = wx.BoxSizer(wx.VERTICAL)

        #----------- STATIC BOX 1
        staticBox1 = wx.StaticBox(panel, label='Default Values')
        staticBoxSizer1= wx.StaticBoxSizer(staticBox1, orient=wx.HORIZONTAL)

        # sbs#sizer# represents the respective column of the respective static box
        sbs1sizer1 = wx.BoxSizer(wx.VERTICAL)
        sbs1sizer2 = wx.BoxSizer(wx.VERTICAL)
        sbs1sizer3 = wx.BoxSizer(wx.VERTICAL)

        sb1Text1 = wx.StaticText(panel, -1, "Node Temp", size=wx.DefaultSize)
        sb1Text2 = wx.StaticText(panel, -1, "Base Temp", size=wx.DefaultSize)
        sb1Text3 = wx.StaticText(panel, -1, "Base Pres", size=wx.DefaultSize)
        sb1Text4 = wx.StaticText(panel, -1, "Amb. Temp", size=wx.DefaultSize)
        sb1Text5 = wx.StaticText(panel, -1, "Amb. Pres", size=wx.DefaultSize)

        sb1txtCtrl1 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl2 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl3 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl4 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl5 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)

        unitList = ['Units here']
        sb1ch1 = wx.Choice(panel, -1, (100, 50), choices = unitList, size=wx.DefaultSize)
        sb1ch2 = wx.Choice(panel, -1, (100, 50), choices = unitList, size=wx.DefaultSize)
        sb1ch3 = wx.Choice(panel, -1, (100, 50), choices = unitList, size=wx.DefaultSize)
        sb1ch4 = wx.Choice(panel, -1, (100, 50), choices = unitList, size=wx.DefaultSize)
        sb1ch5 = wx.Choice(panel, -1, (100, 50), choices = unitList, size=wx.DefaultSize)

        sbs1sizer1.Add(sb1Text1, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        sbs1sizer1.Add(sb1Text2, flag=wx.ALIGN_CENTER|wx.TOP, border=12)
        sbs1sizer1.Add(sb1Text3, flag=wx.ALIGN_CENTER|wx.TOP, border=15)
        sbs1sizer1.Add(sb1Text4, flag=wx.ALIGN_CENTER|wx.TOP, border=15)
        sbs1sizer1.Add(sb1Text5, flag=wx.ALIGN_CENTER|wx.TOP, border=15)

        sbs1sizer2.Add(sb1txtCtrl1, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        sbs1sizer2.Add(sb1txtCtrl2, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        sbs1sizer2.Add(sb1txtCtrl3, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        sbs1sizer2.Add(sb1txtCtrl4, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        sbs1sizer2.Add(sb1txtCtrl5, flag=wx.ALIGN_CENTER|wx.ALL, border=5)

        sbs1sizer3.Add(sb1ch1, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        sbs1sizer3.Add(sb1ch2, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        sbs1sizer3.Add(sb1ch3, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        sbs1sizer3.Add(sb1ch4, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        sbs1sizer3.Add(sb1ch5, flag=wx.ALIGN_CENTER|wx.ALL, border=5)

        staticBoxSizer1.Add(sbs1sizer1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        staticBoxSizer1.Add(sbs1sizer2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        staticBoxSizer1.Add(sbs1sizer3, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        #----------- STATIC BOX 2
        staticBox2 = wx.StaticBox(panel, label='Default Settings')
        staticBoxSizer2 = wx.StaticBoxSizer(staticBox2, orient=wx.VERTICAL)

        sb2sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sb2sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        sb2Text1 = wx.StaticText(panel, -1, "Default Pipe Equation", size=wx.DefaultSize)
        sb2txtCtrl1 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        setAllBtn = wx.Button(panel, label='Set All',  size=wx.DefaultSize)

        sb2sizer1.Add(sb2Text1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb2sizer1.Add(sb2txtCtrl1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb2sizer1.Add(setAllBtn, flag=wx.ALIGN_LEFT|wx.ALL, border=5)


        sb2cb1 = wx.CheckBox(panel, -1, "  Open Heat Transfer")
        sb2cb2 = wx.CheckBox(panel, -1, "  Use Altitude Information")

        sb2sizer2.Add(sb2cb1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb2sizer2.Add(sb2cb2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        staticBoxSizer2.Add(sb2sizer1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        staticBoxSizer2.Add(sb2sizer2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        #-------------- STATIC BOX 3

        staticBox3 = wx.StaticBox(panel, label='Steady State Simulation Settings')
        staticBoxSizer3 = wx.StaticBoxSizer(staticBox3, orient=wx.HORIZONTAL)

        sb3sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sb3sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        sb3sizer3 = wx.BoxSizer(wx.VERTICAL)
        sb3sizer4 = wx.BoxSizer(wx.VERTICAL)
        sb3sizer5 = wx.BoxSizer(wx.VERTICAL)
        sb3sizer6 = wx.BoxSizer(wx.VERTICAL)

        sb3Text1 = wx.StaticText(panel, -1, "Maximum Allowed Iterations", size=wx.DefaultSize)
        sb3sc1 = wx.SpinCtrl(panel, -1, "", size=wx.DefaultSize)
        sb3sc1.SetRange(1,100)
        # SET TO A VARIABLE VALUE LATER WHEN DIALOG IS FUNCTIONAL
        sb3sc1.SetValue(1)

        sb3cb1 = wx.CheckBox(panel, -1, "Maximum Allowed Time  ")
        sb3txtCtrl1 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)

        sb3Text2 = wx.StaticText(panel, -1, "Convergence Tolerance", size=wx.DefaultSize)
        sb3txtCtrl2 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)

        sb3cb2 = wx.CheckBox(panel, -1, "Pause with Warnings  ")

        sb3sizer3.Add(sb3Text1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb3sizer3.Add(sb3Text2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        sb3sizer4.Add(sb3sc1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb3sizer4.Add(sb3txtCtrl1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        sb3sizer5.Add(sb3cb1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb3sizer5.Add(sb3cb2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        sb3sizer6.Add(sb3txtCtrl2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        sb3sizer1.Add(sb3sizer3, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb3sizer1.Add(sb3sizer4, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        sb3sizer2.Add(sb3sizer5, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb3sizer2.Add(sb3sizer6, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        staticBoxSizer3.Add(sb3sizer1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        staticBoxSizer3.Add(sb3sizer2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        #-------------- STATIC BOX 4

        staticBox4 = wx.StaticBox(panel, label='Steady State Simulation Settings')
        staticBoxSizer4 = wx.StaticBoxSizer(staticBox4, orient=wx.HORIZONTAL)

        sb4sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sb4sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        sb4sizer3 = wx.BoxSizer(wx.VERTICAL)
        sb4sizer4 = wx.BoxSizer(wx.VERTICAL)
        sb4sizer5 = wx.BoxSizer(wx.VERTICAL)

        sb4Text1 = wx.StaticText(panel, -1, "Reynolds Number", size=wx.DefaultSize)
        sb4Text2 = wx.StaticText(panel, -1, "Velocity", size=wx.DefaultSize)
        # TO CREATE THE DESIRED BLANK SPACE ABOVE UNITS
        sb4Text3 = wx.StaticText(panel, -1, "", size=wx.DefaultSize)
        sb4Text4 = wx.StaticText(panel, -1, "Pressure", size=wx.DefaultSize)

        sb4txtCtrl1 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb4txtCtrl2 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb4txtCtrl3 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)

        sb4ch1 = wx.Choice(panel, -1, (100, 50), choices = unitList, size=wx.DefaultSize)
        sb4ch2 = wx.Choice(panel, -1, (100, 50), choices = unitList, size=wx.DefaultSize)

        sb4sizer3.Add(sb4Text1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb4sizer3.Add(sb4Text2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        sb4sizer4.Add(sb4txtCtrl1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb4sizer4.Add(sb4txtCtrl2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        sb4sizer5.Add(sb4Text3, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb4sizer5.Add(sb4ch1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        sb4sizer1.Add(sb4sizer3, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb4sizer1.Add(sb4sizer4, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb4sizer1.Add(sb4sizer5, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        sb4sizer2.Add(sb4Text4, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb4sizer2.Add(sb4txtCtrl3, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        sb4sizer2.Add(sb4ch2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        staticBoxSizer4.Add(sb4sizer1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        staticBoxSizer4.Add(sb4sizer2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        #################################
        upperSizer1.Add(staticBoxSizer1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        upperSizer1.Add(staticBoxSizer2, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        upperSizer2.Add(upperSizer1, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        upperSizer2.Add(staticBoxSizer3, flag=wx.ALIGN_LEFT|wx.ALL, border=5)
        upperSizer2.Add(staticBoxSizer4, flag=wx.ALIGN_LEFT|wx.ALL, border=5)

        lowerSizer = wx.BoxSizer(wx.HORIZONTAL)

        restoreBtn = wx.Button(self, label='Restore',  size=wx.DefaultSize)
        saveBtn = wx.Button(self, label='Save',  size=wx.DefaultSize)
        cancelBtn = wx.Button(self, label='Cancel',  size=wx.DefaultSize)

        lowerSizer.Add(restoreBtn, flag=wx.LEFT, border=5)
        lowerSizer.Add(saveBtn, flag=wx.LEFT, border=5)
        lowerSizer.Add(cancelBtn, flag=wx.LEFT, border=5)

        topsizer.Add(panel, proportion=1,flag=wx.ALL|wx.EXPAND, border=5)
        topsizer.Add(lowerSizer,proportion=0, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)


        #########################
        panel.SetSizer(upperSizer2)
        #########################

        self.SetSizer(topsizer)

        cancelBtn.Bind(wx.EVT_BUTTON, self.OnClose)
        saveBtn.Bind(wx.EVT_BUTTON, self.OnClose)

        # BIND EVENTS IN RIBBON
        # okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        # closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
        
    def OnClose(self, e):
        
        self.Destroy()
        
        
class WhereRibbonWillGo(wx.Frame):
    
    def __init__(self, *args, **kw):
        super(WhereRibbonWillGo, self).__init__(*args, **kw)
            
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
        self.SetTitle('Ribbon Dummy')
        self.Centre()
        self.Show(True)
        
        
    def OnChangeDepth(self, e):
        
        chgdep = SimulationSettings(None,
            title='Change Color Depth')
        chgdep.ShowModal()
        chgdep.Destroy()        


def main():
    
    ex = wx.App()
    WhereRibbonWillGo(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()