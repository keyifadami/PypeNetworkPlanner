import wx

class TransparentText(wx.StaticText):
  def __init__(self, parent, id=wx.ID_ANY, label='',
               pos=wx.DefaultPosition, size=wx.DefaultSize,
               style=wx.TRANSPARENT_WINDOW, name='transparenttext'):
    wx.StaticText.__init__(self, parent, id, label, pos, size, style, name)

    self.Bind(wx.EVT_PAINT, self.on_paint)
    self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
    self.Bind(wx.EVT_SIZE, self.on_size)

  def on_paint(self, event):
    bdc = wx.PaintDC(self)
    dc = wx.GCDC(bdc)

    font_face = self.GetFont()
    font_color = self.GetForegroundColour()

    dc.SetFont(font_face)
    dc.SetTextForeground(font_color)
    dc.DrawText(self.GetLabel(), 0, 0)

  def on_size(self, event):
    self.Refresh()
    event.Skip()


class UnitSettingsDialog(wx.Dialog):

    def __init__(self, *args, **kw):
        super(UnitSettingsDialog, self).__init__(*args, **kw)

        self.InitUI()
        self.SetSize((525, 650))
        self.SetTitle('Unit Settings')
        self.Centre()
        self.Show(True)

    def InitUI(self):

        panel = wx.Panel(self)
        topsizer = wx.BoxSizer(wx.VERTICAL)

        top_sb = wx.StaticBox(panel, label='Default Units')
        top_sb.SetBackgroundColour("WHITE")
        top_sbs = wx.StaticBoxSizer(top_sb, orient=wx.HORIZONTAL)
        sizer_left_side = wx.BoxSizer(wx.VERTICAL)
        sizer_right_side = wx.BoxSizer(wx.VERTICAL)
        top_sbs.Add(sizer_left_side, flag=wx.ALL, border=5)
        top_sbs.Add(sizer_right_side, flag=wx.ALL, border=5)

        sb1 = wx.StaticBox(panel, label='Tanks, Nodes, Controls and Components')
        sb1.SetBackgroundColour("WHITE")
        sbs1 = wx.StaticBoxSizer(sb1, orient=wx.HORIZONTAL)

        sb2 = wx.StaticBox(panel, label='Tanks, Nodes, Controls and Components')
        sb2.SetBackgroundColour("WHITE")
        sbs2 = wx.StaticBoxSizer(sb2, orient=wx.HORIZONTAL)

        sb3 = wx.StaticBox(panel, label='Tanks, Nodes, Controls and Components')
        sb3.SetBackgroundColour("WHITE")
        sbs3 = wx.StaticBoxSizer(sb3, orient=wx.HORIZONTAL)

        sb4 = wx.StaticBox(panel, label='Pipes')
        sb4.SetBackgroundColour("WHITE")
        sbs4 = wx.StaticBoxSizer(sb4, orient=wx.HORIZONTAL)

        pressure1 = TransparentText(panel, -1, "Pressure", size=wx.DefaultSize)
        liquid1 = TransparentText(panel, -1, "Liquid Level", size=wx.DefaultSize)
        elevation1 = TransparentText(panel, -1, "Elevation", size=wx.DefaultSize)

        pressure2 = TransparentText(panel, -1, "Pressure", size=wx.DefaultSize)
        liquid2 = TransparentText(panel, -1, "Liquid Level", size=wx.DefaultSize)
        elevation2 = TransparentText(panel, -1, "Elevation", size=wx.DefaultSize)

        pressure3 = TransparentText(panel, -1, "Pressure", size=wx.DefaultSize)
        liquid3 = TransparentText(panel, -1, "Liquid Level", size=wx.DefaultSize)
        elevation3 = TransparentText(panel, -1, "Elevation", size=wx.DefaultSize)

        length = TransparentText(panel, -1, "Length", size=wx.DefaultSize)
        diameter = TransparentText(panel, -1, "Diameter", size=wx.DefaultSize)
        roughness = TransparentText(panel, -1, "Roughness", size=wx.DefaultSize)
        headloss = TransparentText(panel, -1, "Headloss", size=wx.DefaultSize)
        flowrate = TransparentText(panel, -1, "Flow rate", size=wx.DefaultSize)
        massflow = TransparentText(panel, -1, "Mass flow", size=wx.DefaultSize)
        velocity = TransparentText(panel, -1, "Velocity", size=wx.DefaultSize)
        weight = TransparentText(panel, -1, "Weight", size=wx.DefaultSize)
        volume = TransparentText(panel, -1, "Volume", size=wx.DefaultSize)
        surfacearea = TransparentText(panel, -1, "Surface Area", size=wx.DefaultSize)
        energy = TransparentText(panel, -1, "Energy", size=wx.DefaultSize)

        # ---------- CHOICE LISTS
        pressure_List = ['bar', 'ati', 'psi', 'kpa']
        length_List_big = ['meters', 'feet']
        length_List_small = ['inches', 'centimeters', 'millimeters']
        volumetricFlow_rate_List = ['ft^3/sec', 'm^3/sec']
        massFlow_rate_List = ['slugs/sec', 'kg/sec']
        velocity_list = ['ft/s', 'm/s']
        weight_list = ['lbs', 'kg']
        volume_list = ['ft^3', 'm^3']
        surface_area_list = ['ft^2', 'm^2']
        energy_list = ['kilowatts']

        pressure_cb1 = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=pressure_List,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        liquid_cb1 = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=length_List_big,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        elevation_cb1 = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=length_List_big,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )

        pressure_cb2 = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=pressure_List,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        liquid_cb2 = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=length_List_big,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        elevation_cb2 = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=length_List_big,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        pressure_cb3 = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=pressure_List,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        liquid_cb3 = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=length_List_big,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        elevation_cb3 = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=length_List_big,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        #----------------------------------------------

        length_cb = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=length_List_small,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )

        diameter_cb = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=length_List_small,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        roughness_cb = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=length_List_small,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )

        headloss_cb = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=pressure_List,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )

        vol_flow_cb = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=volumetricFlow_rate_List,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        mass_flow_cb = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=massFlow_rate_List,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        velocity_cb = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=velocity_list,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )

        weight_cb = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=weight_list,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )

        vol_cb = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=volume_list,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        surface_area_cb = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=surface_area_list,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        energy_cb = wx.ComboBox(panel, -1, "default value", pos=wx.DefaultPosition, size=(100,-1),
                         choices=energy_list,
                         style=wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )

        sizer_box1_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_box1_2 = wx.BoxSizer(wx.VERTICAL)

        sizer_box1_1.Add(pressure1,1, wx.ALL, 10)
        sizer_box1_1.Add(liquid1, 1, wx.ALL, 10)
        sizer_box1_1.Add(elevation1, 1, wx.ALL, 10)

        sizer_box1_2.Add(pressure_cb1, 1, wx.ALL, 10)
        sizer_box1_2.Add(liquid_cb1, 1, wx.ALL, 10)
        sizer_box1_2.Add(elevation_cb1, 1, wx.ALL, 10)

        sbs1.Add(sizer_box1_1)
        sbs1.Add(sizer_box1_2)

        #---------- BOX 2

        sizer_box2_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_box2_2 = wx.BoxSizer(wx.VERTICAL)

        sizer_box2_1.Add(pressure2,1, wx.ALL, 10)
        sizer_box2_1.Add(liquid2, 1, wx.ALL, 10)
        sizer_box2_1.Add(elevation2, 1, wx.ALL, 10)

        sizer_box2_2.Add(pressure_cb2, 1, wx.ALL, 10)
        sizer_box2_2.Add(liquid_cb2, 1, wx.ALL, 10)
        sizer_box2_2.Add(elevation_cb2, 1, wx.ALL, 10)

        sbs2.Add(sizer_box2_1)
        sbs2.Add(sizer_box2_2)

        #---------- BOX 3
        sizer_box3_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_box3_2 = wx.BoxSizer(wx.VERTICAL)

        sizer_box3_1.Add(pressure3,1, wx.ALL, 10)
        sizer_box3_1.Add(liquid3, 1, wx.ALL, 10)
        sizer_box3_1.Add(elevation3, 1, wx.ALL, 10)

        sizer_box3_2.Add(pressure_cb3, 1, wx.ALL, 10)
        sizer_box3_2.Add(liquid_cb3, 1, wx.ALL, 10)
        sizer_box3_2.Add(elevation_cb3, 1, wx.ALL, 10)

        sbs3.Add(sizer_box3_1)
        sbs3.Add(sizer_box3_2)

        #---------- BOX 4
        sizer_box4_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_box4_2 = wx.BoxSizer(wx.VERTICAL)

        sizer_box4_1.Add(length,1, wx.ALL, 10)
        sizer_box4_1.Add(diameter, 1, wx.ALL, 10)
        sizer_box4_1.Add(roughness, 1, wx.ALL, 10)
        sizer_box4_1.Add(headloss,1, wx.ALL, 10)
        sizer_box4_1.Add(flowrate, 1, wx.ALL, 10)
        sizer_box4_1.Add(massflow, 1, wx.ALL, 10)
        sizer_box4_1.Add(velocity,1, wx.ALL, 10)
        sizer_box4_1.Add(weight, 1, wx.ALL, 10)
        sizer_box4_1.Add(volume, 1, wx.ALL, 10)
        sizer_box4_1.Add(surfacearea, 1, wx.ALL, 10)
        sizer_box4_1.Add(energy, 1, wx.ALL, 10)

        sizer_box4_2.Add(length_cb, 1, wx.ALL, 10)
        sizer_box4_2.Add(diameter_cb, 1, wx.ALL, 10)
        sizer_box4_2.Add(roughness_cb, 1, wx.ALL, 10)
        sizer_box4_2.Add(headloss_cb, 1, wx.ALL, 10)
        sizer_box4_2.Add(vol_flow_cb, 1, wx.ALL, 10)
        sizer_box4_2.Add(mass_flow_cb, 1, wx.ALL, 10)
        sizer_box4_2.Add(velocity_cb, 1, wx.ALL, 10)
        sizer_box4_2.Add(weight_cb, 1, wx.ALL, 10)
        sizer_box4_2.Add(vol_cb, 1, wx.ALL, 10)
        sizer_box4_2.Add(surface_area_cb, 1, wx.ALL, 10)
        sizer_box4_2.Add(energy_cb, 1, wx.ALL, 10)

        sbs4.Add(sizer_box4_1)
        sbs4.Add(sizer_box4_2)

        #---------- ADDING TO LEFT SIDE SIZER

        sizer_left_side.Add(sbs1, flag=wx.ALL, border=5)
        sizer_left_side.Add(sbs2, flag=wx.ALL, border=5)
        sizer_left_side.Add(sbs3, flag=wx.ALL, border=5)

        #---------- ADDING TO RIGHT SIDE SIZER
        sizer_right_side.Add(sbs4, flag=wx.ALL, border=5)


        #########################################################
        # YOU HAVE TO SET EACH STATIC BOX SIZER
        panel.SetSizer(top_sbs)
        #########################################################


        #########################################################
        # Lower Buttons and sizer
        #########################################################
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        saveButton = wx.Button(self, label='Save')
        cancelButton = wx.Button(self, label='Cancel')
        restoreButton = wx.Button(self, label='Restore Defaults')

        hbox2.Add(restoreButton, flag=wx.ALL, border=10)
        hbox2.Add(saveButton, flag=wx.ALL, border=10)
        hbox2.Add(cancelButton, flag=wx.ALL, border=10)

        topsizer.Add(panel, proportion=1,
            flag=wx.ALL|wx.EXPAND, border=5)
        topsizer.Add(hbox2,
            flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(topsizer)

        saveButton.Bind(wx.EVT_BUTTON, self.OnClose)
        restoreButton.Bind(wx.EVT_BUTTON, self.OnClose)
        cancelButton.Bind(wx.EVT_BUTTON, self.OnClose)

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

        chgdep = UnitSettingsDialog(None,
            title='Change Color Depth')
        chgdep.ShowModal()
        chgdep.Destroy()


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()