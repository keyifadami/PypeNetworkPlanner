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

class DisplaySettings(wx.Panel):
    def __init__(self, parent):
        super(DisplaySettings, self).__init__(parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.InitUI()

    def InitUI(self):

        panel1 = wx.Panel(self)
        panel1.SetBackgroundColour('WHITE')
        topsizer = wx.BoxSizer(wx.VERTICAL)

        # CONTROLS

        # COLUMN 1 CONTROLS
        Element_Type = wx.StaticText(panel1, -1, "Element Type", size=wx.DefaultSize)
        Nodes_Source = wx.StaticText(panel1, -1, "Nodes (Source)", size=wx.DefaultSize)
        Nodes_Demand = wx.StaticText(panel1, -1, "Nodes (Demand)", size=wx.DefaultSize)
        Nodes_Wellhead = wx.StaticText(panel1, -1, "Nodes (Wellhead)", size=wx.DefaultSize)
        Pipes_Text = wx.StaticText(panel1, -1, "Pipes", size=wx.DefaultSize)
        Valves_Check = wx.StaticText(panel1, -1, "Valves (Check)", size=wx.DefaultSize)
        Valves_Block = wx.StaticText(panel1, -1, "Valves (Block)", size=wx.DefaultSize)
        Valves_Resist = wx.StaticText(panel1, -1, "Valves (Resist.)", size=wx.DefaultSize)
        Compressors_Text = wx.StaticText(panel1, -1, "Compressors", size=wx.DefaultSize)
        Regulator_Text = wx.StaticText(panel1, -1, "Regulators", size=wx.DefaultSize)
        Loss_Element_Text = wx.StaticText(panel1, -1, "Loss Elements", size=wx.DefaultSize)

        # COLUMN 2 CONTROLS
        Color_Text = wx.StaticText(panel1, -1, "Color", size=wx.DefaultSize)

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

        lowerHalfSizer.Add(restoreButton, flag=wx.RIGHT, border=5)

        topsizer.Add(panel1, proportion=1,
            flag=wx.ALL|wx.EXPAND, border=10)
        topsizer.Add(lowerHalfSizer,
            flag=wx.ALIGN_RIGHT|wx.ALL, border=20)

        # SETTING SIZERS
        panel1.SetSizer(TopHalfSizer)
        self.SetSizer(topsizer)

class ElementListDialog(wx.Dialog):

    def __init__(self, *args, **kw):
        super(ElementListDialog, self).__init__(*args, **kw)
        self.SetBackgroundColour("WHITE")
        self.InitUI()
        self.SetSize((1100, 600))
        self.SetTitle("Element List")
        self.Center(True)


    def InitUI(self):

        panel = wx.Panel(self)
        ##########################
        panel2 = DisplaySettings(panel)
        ##########################
        panel.SetBackgroundColour("WHITE")

        topSizer = wx.BoxSizer(wx.VERTICAL)
        upperSizer = wx.BoxSizer(wx.HORIZONTAL)
        lowerSizer = wx.BoxSizer(wx.HORIZONTAL)

        #-----------------------------------
        # LHS STATIC BOX
        staticBox1 = wx.StaticBox(panel, label='Pipe Pressure Color Variation')
        staticBoxSizer1 = wx.StaticBoxSizer(staticBox1, orient=wx.VERTICAL)

        sbSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sbSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        sbSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        sbSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        sbSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        sbSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        sbSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        sbSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        # STATIC BOX CONTROLS
        sbRadio1 = wx.RadioButton(panel, -1, " SI Units ")
        sbRadio2 = wx.RadioButton(panel, -1, " Brittish Units ")

        sb1txtCtrl1 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl2 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl3 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl4 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl5 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl6 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl7 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl8 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl9 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)
        sb1txtCtrl10 = wx.TextCtrl(panel, -1, "", size=wx.DefaultSize)

        max_pressure_Button = wx.Button(panel, label='', size=wx.DefaultSize)
        max_pressure_Button.SetBackgroundColour("RED")

        pressure_Button2 = wx.Button(panel, label='', size=wx.DefaultSize)
        pressure_Button2.SetBackgroundColour("BLUE")

        pressure_Button3 = wx.Button(panel, label='',size=wx.DefaultSize)
        pressure_Button3.SetBackgroundColour("LIGHT BLUE")

        pressure_Button4 = wx.Button(panel, label='', size=wx.DefaultSize)
        pressure_Button4.SetBackgroundColour("GREEN")

        lowest_pressure_Button = wx.Button(panel, label='',size=wx.DefaultSize)
        lowest_pressure_Button.SetBackgroundColour("GRAY")

        change_design_Button = wx.Button(panel, label='Change to Design Color', size=wx.DefaultSize)
        restore_default_Button = wx.Button(panel, label='Restore Defaults', size=wx.DefaultSize)

        #-----------------------------------

        saveButton = wx.Button(self, label='Save')
        cancelButton = wx.Button(self, label='Cancel')

        # ADD AND SET SIZERS
        # LHS SB
        sbSizer1.Add(sbRadio1, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        sbSizer1.Add(sbRadio2, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)

        sbSizer2.Add(sb1txtCtrl1, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        sbSizer2.Add(sb1txtCtrl2, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        sbSizer2.Add(max_pressure_Button, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)

        sbSizer3.Add(sb1txtCtrl3, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        sbSizer3.Add(sb1txtCtrl4, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        sbSizer3.Add(pressure_Button2, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)

        sbSizer4.Add(sb1txtCtrl5, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        sbSizer4.Add(sb1txtCtrl6, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        sbSizer4.Add(pressure_Button3, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)

        sbSizer5.Add(sb1txtCtrl7, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        sbSizer5.Add(sb1txtCtrl8, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        sbSizer5.Add(pressure_Button4, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)

        sbSizer6.Add(sb1txtCtrl9, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        sbSizer6.Add(sb1txtCtrl10, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        sbSizer6.Add(lowest_pressure_Button, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)

        sbSizer7.Add(change_design_Button, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)

        sbSizer8.Add(restore_default_Button, flag=wx.ALIGN_RIGHT | wx.ALL, border=5)

        staticBoxSizer1.Add(sbSizer1, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        staticBoxSizer1.Add(sbSizer2, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        staticBoxSizer1.Add(sbSizer3, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        staticBoxSizer1.Add(sbSizer4, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        staticBoxSizer1.Add(sbSizer5, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        staticBoxSizer1.Add(sbSizer6, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        staticBoxSizer1.Add(sbSizer7, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        staticBoxSizer1.Add(sbSizer8, flag=wx.ALIGN_RIGHT | wx.ALL, border=5)

        upperSizer.Add(panel2, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)
        upperSizer.Add(staticBoxSizer1, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)

        #---------------------------
        lowerSizer.Add(saveButton, flag=wx.ALIGN_RIGHT | wx.ALL, border=5)
        lowerSizer.Add(cancelButton, flag=wx.ALIGN_RIGHT | wx.ALL, border=5)

        topSizer.Add(panel, proportion=1,
            flag=wx.ALL|wx.EXPAND, border=5)

        topSizer.Add(lowerSizer,
            flag=wx.ALIGN_RIGHT|wx.ALL, border=10)

        #########################
        panel.SetSizer(upperSizer)
        #########################

        self.SetSizer(topSizer)

        saveButton.Bind(wx.EVT_BUTTON, self.OnClose)


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