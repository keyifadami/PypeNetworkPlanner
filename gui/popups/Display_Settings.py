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

####################################################################

class DisplaySettings(wx.Dialog):

    def __init__(self, *args, **kw):
        super(DisplaySettings, self).__init__(*args, **kw)

        self.InitUI()
        self.SetSize((725, 500))
        self.SetTitle('Display Settings')
        self.Centre()
        self.Show(True)


    def InitUI(self):

        panel1 = wx.Panel(self)
        panel1.SetBackgroundColour('WHITE')
        topsizer = wx.BoxSizer(wx.VERTICAL)

        # CONTROLS

        # COLUMN 1 CONTROLS
        Element_Type = TransparentText(panel1, -1, "Element Type", size=wx.DefaultSize)
        Nodes_Source = TransparentText(panel1, -1, "Nodes (Source)", size=wx.DefaultSize)
        Nodes_Demand = TransparentText(panel1, -1, "Nodes (Demand)", size=wx.DefaultSize)
        Nodes_Wellhead = TransparentText(panel1, -1, "Nodes (Wellhead)", size=wx.DefaultSize)
        Pipes_Text = TransparentText(panel1, -1, "Pipes", size=wx.DefaultSize)
        Valves_Check = TransparentText(panel1, -1, "Valves (Check)", size=wx.DefaultSize)
        Valves_Block = TransparentText(panel1, -1, "Valves (Block)", size=wx.DefaultSize)
        Valves_Resist = TransparentText(panel1, -1, "Valves (Resist.)", size=wx.DefaultSize)
        Compressors_Text = TransparentText(panel1, -1, "Compressors", size=wx.DefaultSize)
        Regulator_Text = TransparentText(panel1, -1, "Regulators", size=wx.DefaultSize)
        Loss_Element_Text = TransparentText(panel1, -1, "Loss Elements", size=wx.DefaultSize)

        # COLUMN 2 CONTROLS
        Color_Text = TransparentText(panel1, -1, "Color", size=wx.DefaultSize)

        nodeSource_color_Button = wx.Button(panel1, label='')
        nodeSource_color_Button.SetBackgroundColour("RED")

        nodeDemand_color_Button = wx.Button(panel1, label='')
        nodeDemand_color_Button.SetBackgroundColour("GREEN")

        nodeWellhead_color_Button = wx.Button(panel1, label='')
        nodeWellhead_color_Button.SetBackgroundColour("BLUE")

        pipes_color_Button = wx.Button(panel1, label='')
        pipes_color_Button.SetBackgroundColour("RED")

        valvesBlock_color_Button = wx.Button(panel1, label='')
        valvesBlock_color_Button.SetBackgroundColour("GREEN")

        valvesCheck_color_Button = wx.Button(panel1, label='')
        valvesCheck_color_Button.SetBackgroundColour("BLUE")

        valvesResist_color_Button = wx.Button(panel1, label='')
        valvesResist_color_Button.SetBackgroundColour("RED")

        compressors_color_Button = wx.Button(panel1, label='')
        compressors_color_Button.SetBackgroundColour("GREEN")

        regulators_color_Button = wx.Button(panel1, label='')
        regulators_color_Button.SetBackgroundColour("BLUE")

        lossElements_color_Button = wx.Button(panel1, label='')
        lossElements_color_Button.SetBackgroundColour("RED")

        # COLUMN 3 CONTROLS

        Highlight_Text = TransparentText(panel1, -1, "Highlight", size=wx.DefaultSize)

        column3_List = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        column3_choice1 = wx.Choice(panel1, -1, (100, 50), choices=column3_List)
        column3_choice2 = wx.Choice(panel1, -1, (100, 50), choices=column3_List)
        column3_choice3 = wx.Choice(panel1, -1, (100, 50), choices=column3_List)
        column3_choice4 = wx.Choice(panel1, -1, (100, 50), choices=column3_List)
        column3_choice5 = wx.Choice(panel1, -1, (100, 50), choices=column3_List)
        column3_choice6 = wx.Choice(panel1, -1, (100, 50), choices=column3_List)
        column3_choice7 = wx.Choice(panel1, -1, (100, 50), choices=column3_List)
        column3_choice8 = wx.Choice(panel1, -1, (100, 50), choices=column3_List)
        column3_choice9 = wx.Choice(panel1, -1, (100, 50), choices=column3_List)
        column3_choice10 = wx.Choice(panel1, -1, (100, 50), choices=column3_List)

        #---------------- COLUMN 4-9 IS ESSENTIALLY THE SAME AS COLUMN 3

        # COLUMN 4 CONTROLS
        size_Text = TransparentText(panel1, -1, "Size", size=wx.DefaultSize)

        column4_List = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        column4_choice1 = wx.Choice(panel1, -1, (100, 50), choices=column4_List)
        column4_choice2 = wx.Choice(panel1, -1, (100, 50), choices=column4_List)
        column4_choice3 = wx.Choice(panel1, -1, (100, 50), choices=column4_List)
        column4_choice4 = wx.Choice(panel1, -1, (100, 50), choices=column4_List)
        column4_choice5 = wx.Choice(panel1, -1, (100, 50), choices=column4_List)
        column4_choice6 = wx.Choice(panel1, -1, (100, 50), choices=column4_List)
        column4_choice7 = wx.Choice(panel1, -1, (100, 50), choices=column4_List)
        column4_choice8 = wx.Choice(panel1, -1, (100, 50), choices=column4_List)
        column4_choice9 = wx.Choice(panel1, -1, (100, 50), choices=column4_List)
        column4_choice10 = wx.Choice(panel1, -1, (100, 50), choices=column4_List)

        # COLUMN 5 CONTROLS
        symbol_Text = TransparentText(panel1, -1, "Symbol", size=wx.DefaultSize)

        column5_List = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        column5_choice1 = wx.Choice(panel1, -1, (100, 50), choices=column5_List)
        column5_choice2 = wx.Choice(panel1, -1, (100, 50), choices=column5_List)
        column5_choice3 = wx.Choice(panel1, -1, (100, 50), choices=column5_List)
        column5_choice4 = wx.Choice(panel1, -1, (100, 50), choices=column5_List)
        column5_choice5 = wx.Choice(panel1, -1, (100, 50), choices=column5_List)
        column5_choice6 = wx.Choice(panel1, -1, (100, 50), choices=column5_List)
        column5_choice7 = wx.Choice(panel1, -1, (100, 50), choices=column5_List)
        column5_choice8 = wx.Choice(panel1, -1, (100, 50), choices=column5_List)
        column5_choice9 = wx.Choice(panel1, -1, (100, 50), choices=column5_List)
        column5_choice10 = wx.Choice(panel1, -1, (100, 50), choices=column5_List)

        # COLUMN 6 CONTROLS
        label1_Text = TransparentText(panel1, -1, "Label 1", size=wx.DefaultSize)

        column6_List = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        column6_choice1 = wx.Choice(panel1, -1, (100, 50), choices=column6_List)
        column6_choice2 = wx.Choice(panel1, -1, (100, 50), choices=column6_List)
        column6_choice3 = wx.Choice(panel1, -1, (100, 50), choices=column6_List)
        column6_choice4 = wx.Choice(panel1, -1, (100, 50), choices=column6_List)
        column6_choice5 = wx.Choice(panel1, -1, (100, 50), choices=column6_List)
        column6_choice6 = wx.Choice(panel1, -1, (100, 50), choices=column6_List)
        column6_choice7 = wx.Choice(panel1, -1, (100, 50), choices=column6_List)
        column6_choice8 = wx.Choice(panel1, -1, (100, 50), choices=column6_List)
        column6_choice9 = wx.Choice(panel1, -1, (100, 50), choices=column6_List)
        column6_choice10 = wx.Choice(panel1, -1, (100, 50), choices=column6_List)

        # COLUMN 7 CONTROLS
        label2_Text = TransparentText(panel1, -1, "Label 2", size=wx.DefaultSize)

        column7_List = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        column7_choice1 = wx.Choice(panel1, -1, (100, 50), choices=column7_List)
        column7_choice2 = wx.Choice(panel1, -1, (100, 50), choices=column7_List)
        column7_choice3 = wx.Choice(panel1, -1, (100, 50), choices=column7_List)
        column7_choice4 = wx.Choice(panel1, -1, (100, 50), choices=column7_List)
        column7_choice5 = wx.Choice(panel1, -1, (100, 50), choices=column7_List)
        column7_choice6 = wx.Choice(panel1, -1, (100, 50), choices=column7_List)
        column7_choice7 = wx.Choice(panel1, -1, (100, 50), choices=column7_List)
        column7_choice8 = wx.Choice(panel1, -1, (100, 50), choices=column7_List)
        column7_choice9 = wx.Choice(panel1, -1, (100, 50), choices=column7_List)
        column7_choice10 = wx.Choice(panel1, -1, (100, 50), choices=column7_List)

        # COLUMN 8 CONTROLS
        label3_Text = TransparentText(panel1, -1, "Label 3", size=wx.DefaultSize)

        column8_List = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        column8_choice1 = wx.Choice(panel1, -1, (100, 50), choices=column8_List)
        column8_choice2 = wx.Choice(panel1, -1, (100, 50), choices=column8_List)
        column8_choice3 = wx.Choice(panel1, -1, (100, 50), choices=column8_List)
        column8_choice4 = wx.Choice(panel1, -1, (100, 50), choices=column8_List)
        column8_choice5 = wx.Choice(panel1, -1, (100, 50), choices=column8_List)
        column8_choice6 = wx.Choice(panel1, -1, (100, 50), choices=column8_List)
        column8_choice7 = wx.Choice(panel1, -1, (100, 50), choices=column8_List)
        column8_choice8 = wx.Choice(panel1, -1, (100, 50), choices=column8_List)
        column8_choice9 = wx.Choice(panel1, -1, (100, 50), choices=column8_List)
        column8_choice10 = wx.Choice(panel1, -1, (100, 50), choices=column8_List)

        # COLUMN 9 CONTROLS
        label4_Text = TransparentText(panel1, -1, "Label 4", size=wx.DefaultSize)

        column9_List = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        column9_choice1 = wx.Choice(panel1, -1, (100, 50), choices=column9_List)
        column9_choice2 = wx.Choice(panel1, -1, (100, 50), choices=column9_List)
        column9_choice3 = wx.Choice(panel1, -1, (100, 50), choices=column9_List)
        column9_choice4 = wx.Choice(panel1, -1, (100, 50), choices=column9_List)
        column9_choice5 = wx.Choice(panel1, -1, (100, 50), choices=column9_List)
        column9_choice6 = wx.Choice(panel1, -1, (100, 50), choices=column9_List)
        column9_choice7 = wx.Choice(panel1, -1, (100, 50), choices=column9_List)
        column9_choice8 = wx.Choice(panel1, -1, (100, 50), choices=column9_List)
        column9_choice9 = wx.Choice(panel1, -1, (100, 50), choices=column9_List)
        column9_choice10 = wx.Choice(panel1, -1, (100, 50), choices=column9_List)


        # COLUMN SIZERS
        column1_sizer = wx.BoxSizer(wx.VERTICAL)
        column2_sizer = wx.BoxSizer(wx.VERTICAL)
        column3_sizer = wx.BoxSizer(wx.VERTICAL)
        column4_sizer = wx.BoxSizer(wx.VERTICAL)
        column5_sizer = wx.BoxSizer(wx.VERTICAL)
        column6_sizer = wx.BoxSizer(wx.VERTICAL)
        column7_sizer = wx.BoxSizer(wx.VERTICAL)
        column8_sizer = wx.BoxSizer(wx.VERTICAL)
        column9_sizer = wx.BoxSizer(wx.VERTICAL)

        # COLUMN 1 ADDING
        column1_sizer.Add(Element_Type, flag=wx.ALL | wx.ALIGN_BOTTOM, border=5)
        column1_sizer.Add(Nodes_Source, flag=wx.ALL | wx.ALIGN_BOTTOM, border=10)
        column1_sizer.Add(Nodes_Demand, flag=wx.ALL | wx.ALIGN_BOTTOM, border=10)
        column1_sizer.Add(Nodes_Wellhead, flag=wx.ALL | wx.ALIGN_BOTTOM, border=10)
        column1_sizer.Add(Pipes_Text, flag=wx.ALL | wx.ALIGN_BOTTOM, border=10)
        column1_sizer.Add(Valves_Check, flag=wx.ALL | wx.ALIGN_BOTTOM, border=10)
        column1_sizer.Add(Valves_Block, flag=wx.ALL | wx.ALIGN_BOTTOM, border=10)
        column1_sizer.Add(Valves_Resist, flag=wx.ALL | wx.ALIGN_BOTTOM, border=10)
        column1_sizer.Add(Compressors_Text, flag=wx.ALL | wx.ALIGN_BOTTOM, border=10)
        column1_sizer.Add(Regulator_Text, flag=wx.ALL | wx.ALIGN_BOTTOM, border=10)
        column1_sizer.Add(Loss_Element_Text, flag=wx.ALL | wx.ALIGN_BOTTOM, border=10)

        # COLUMN 2 ADDING
        column2_sizer.Add(Color_Text, flag=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, border=5)
        column2_sizer.Add(nodeSource_color_Button, flag=wx.ALL, border=5)
        column2_sizer.Add(nodeDemand_color_Button, flag=wx.ALL, border=5)
        column2_sizer.Add(nodeWellhead_color_Button, flag=wx.ALL, border=5)
        column2_sizer.Add(pipes_color_Button, flag=wx.ALL, border=5)
        column2_sizer.Add(valvesBlock_color_Button, flag=wx.ALL, border=5)
        column2_sizer.Add(valvesCheck_color_Button, flag=wx.ALL, border=5)
        column2_sizer.Add(valvesResist_color_Button, flag=wx.ALL, border=5)
        column2_sizer.Add(compressors_color_Button, flag=wx.ALL, border=5)
        column2_sizer.Add(regulators_color_Button, flag=wx.ALL, border=5)
        column2_sizer.Add(lossElements_color_Button, flag=wx.ALL, border=5)

        # COLUMN 3 ADDING
        column3_sizer.Add(Highlight_Text, flag=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, border=5)
        column3_sizer.Add(column3_choice1, flag=wx.ALL, border=5)
        column3_sizer.Add(column3_choice2, flag=wx.ALL, border=5)
        column3_sizer.Add(column3_choice3, flag=wx.ALL, border=5)
        column3_sizer.Add(column3_choice4, flag=wx.ALL, border=5)
        column3_sizer.Add(column3_choice5, flag=wx.ALL, border=5)
        column3_sizer.Add(column3_choice6, flag=wx.ALL, border=5)
        column3_sizer.Add(column3_choice7, flag=wx.ALL, border=5)
        column3_sizer.Add(column3_choice8, flag=wx.ALL, border=5)
        column3_sizer.Add(column3_choice9, flag=wx.ALL, border=5)
        column3_sizer.Add(column3_choice10, flag=wx.ALL, border=5)

        # COLUMN 4 ADDING
        column4_sizer.Add(size_Text, flag=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, border=5)
        column4_sizer.Add(column4_choice1, flag=wx.ALL, border=5)
        column4_sizer.Add(column4_choice2, flag=wx.ALL, border=5)
        column4_sizer.Add(column4_choice3, flag=wx.ALL, border=5)
        column4_sizer.Add(column4_choice4, flag=wx.ALL, border=5)
        column4_sizer.Add(column4_choice5, flag=wx.ALL, border=5)
        column4_sizer.Add(column4_choice6, flag=wx.ALL, border=5)
        column4_sizer.Add(column4_choice7, flag=wx.ALL, border=5)
        column4_sizer.Add(column4_choice8, flag=wx.ALL, border=5)
        column4_sizer.Add(column4_choice9, flag=wx.ALL, border=5)
        column4_sizer.Add(column4_choice10, flag=wx.ALL, border=5)

        # COLUMN 5 ADDING
        column5_sizer.Add(symbol_Text, flag=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, border=5)
        column5_sizer.Add(column5_choice1, flag=wx.ALL, border=5)
        column5_sizer.Add(column5_choice2, flag=wx.ALL, border=5)
        column5_sizer.Add(column5_choice3, flag=wx.ALL, border=5)
        column5_sizer.Add(column5_choice4, flag=wx.ALL, border=5)
        column5_sizer.Add(column5_choice5, flag=wx.ALL, border=5)
        column5_sizer.Add(column5_choice6, flag=wx.ALL, border=5)
        column5_sizer.Add(column5_choice7, flag=wx.ALL, border=5)
        column5_sizer.Add(column5_choice8, flag=wx.ALL, border=5)
        column5_sizer.Add(column5_choice9, flag=wx.ALL, border=5)
        column5_sizer.Add(column5_choice10, flag=wx.ALL, border=5)

        # COLUMN 6 ADDING
        column6_sizer.Add(label1_Text, flag=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, border=5)
        column6_sizer.Add(column6_choice1, flag=wx.ALL, border=5)
        column6_sizer.Add(column6_choice2, flag=wx.ALL, border=5)
        column6_sizer.Add(column6_choice3, flag=wx.ALL, border=5)
        column6_sizer.Add(column6_choice4, flag=wx.ALL, border=5)
        column6_sizer.Add(column6_choice5, flag=wx.ALL, border=5)
        column6_sizer.Add(column6_choice6, flag=wx.ALL, border=5)
        column6_sizer.Add(column6_choice7, flag=wx.ALL, border=5)
        column6_sizer.Add(column6_choice8, flag=wx.ALL, border=5)
        column6_sizer.Add(column6_choice9, flag=wx.ALL, border=5)
        column6_sizer.Add(column6_choice10, flag=wx.ALL, border=5)

        # COLUMN 7 ADDING
        column7_sizer.Add(label2_Text, flag=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, border=5)
        column7_sizer.Add(column7_choice1, flag=wx.ALL, border=5)
        column7_sizer.Add(column7_choice2, flag=wx.ALL, border=5)
        column7_sizer.Add(column7_choice3, flag=wx.ALL, border=5)
        column7_sizer.Add(column7_choice4, flag=wx.ALL, border=5)
        column7_sizer.Add(column7_choice5, flag=wx.ALL, border=5)
        column7_sizer.Add(column7_choice6, flag=wx.ALL, border=5)
        column7_sizer.Add(column7_choice7, flag=wx.ALL, border=5)
        column7_sizer.Add(column7_choice8, flag=wx.ALL, border=5)
        column7_sizer.Add(column7_choice9, flag=wx.ALL, border=5)
        column7_sizer.Add(column7_choice10, flag=wx.ALL, border=5)

         # COLUMN 8 ADDING
        column8_sizer.Add(label3_Text, flag=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, border=5)
        column8_sizer.Add(column8_choice1, flag=wx.ALL, border=5)
        column8_sizer.Add(column8_choice2, flag=wx.ALL, border=5)
        column8_sizer.Add(column8_choice3, flag=wx.ALL, border=5)
        column8_sizer.Add(column8_choice4, flag=wx.ALL, border=5)
        column8_sizer.Add(column8_choice5, flag=wx.ALL, border=5)
        column8_sizer.Add(column8_choice6, flag=wx.ALL, border=5)
        column8_sizer.Add(column8_choice7, flag=wx.ALL, border=5)
        column8_sizer.Add(column8_choice8, flag=wx.ALL, border=5)
        column8_sizer.Add(column8_choice9, flag=wx.ALL, border=5)
        column8_sizer.Add(column8_choice10, flag=wx.ALL, border=5)

         # COLUMN 8 ADDING
        column9_sizer.Add(label4_Text, flag=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, border=5)
        column9_sizer.Add(column9_choice1, flag=wx.ALL, border=5)
        column9_sizer.Add(column9_choice2, flag=wx.ALL, border=5)
        column9_sizer.Add(column9_choice3, flag=wx.ALL, border=5)
        column9_sizer.Add(column9_choice4, flag=wx.ALL, border=5)
        column9_sizer.Add(column9_choice5, flag=wx.ALL, border=5)
        column9_sizer.Add(column9_choice6, flag=wx.ALL, border=5)
        column9_sizer.Add(column9_choice7, flag=wx.ALL, border=5)
        column9_sizer.Add(column9_choice8, flag=wx.ALL, border=5)
        column9_sizer.Add(column9_choice9, flag=wx.ALL, border=5)
        column9_sizer.Add(column9_choice10, flag=wx.ALL, border=5)

        TopHalfSizer = wx.BoxSizer(wx.HORIZONTAL)

        TopHalfSizer.Add(column1_sizer, flag=wx.RIGHT, border=10)
        TopHalfSizer.Add(column2_sizer)
        TopHalfSizer.Add(column3_sizer)
        TopHalfSizer.Add(column4_sizer)
        TopHalfSizer.Add(column5_sizer)
        TopHalfSizer.Add(column6_sizer)
        TopHalfSizer.Add(column7_sizer)
        TopHalfSizer.Add(column8_sizer)
        TopHalfSizer.Add(column9_sizer)


        lowerHalfSizer = wx.BoxSizer(wx.HORIZONTAL)
        restoreButton = wx.Button(self, label='Restore Defaults')
        closeButton = wx.Button(self, label='Save')
        cancelButton = wx.Button(self, label='Cancel')

        lowerHalfSizer.Add(restoreButton, flag=wx.LEFT, border=5)
        lowerHalfSizer.Add(closeButton, flag=wx.LEFT, border=5)
        lowerHalfSizer.Add(cancelButton)

        topsizer.Add(panel1, proportion=1,
            flag=wx.ALL|wx.EXPAND, border=10)
        topsizer.Add(lowerHalfSizer,
            flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        # SETTING SIZERS
        panel1.SetSizer(TopHalfSizer)
        self.SetSizer(topsizer)

        cancelButton.Bind(wx.EVT_BUTTON, self.OnClose)
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

        chgdep = DisplaySettings(None,
            title='Change Color Depth')
        chgdep.ShowModal()
        chgdep.Destroy()


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()