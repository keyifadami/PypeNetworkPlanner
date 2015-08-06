'''
        This is drawing_panel.py
        it defines a drawing panel widget that is a paint/CAD like interface
        for manipulating a pipeline network graph
        it uses the graph structure defined in the graph module
        found in Pypeline_v2/graph/ look there for details about the graph
        used here

'''
import wx
from wx.lib.floatcanvas import NavCanvas, FloatCanvas, GUIMode, Resources
from drawing import *
from utils import geometry as Geom
from gui.design.colors import *
from graph import graph, edge, node, edge_element


'''
    GUI Modes for DrawingPanel
'''

class GUIGraph(GUIMode.GUIBase):
    def __init__(self, canvas=None, graph=None):
        GUIMode.GUIBase.__init__(self, canvas)
        self.graph = graph

    def update(self):
        draw_graph(self.graph, self.Canvas)
        self.Canvas.Draw()
        self.Canvas.ClearAll(ResetBB=False)

"""
ADD NODES:
    THIS GUI MODE IS FOR ADDING NODES AND OTHERWIZE EXTENDING THE GRAPH
"""

## this GUI mode will simply add a node to the graph anywhere the user clicks
## it will not allow the user to add duplicate nodes

class AddNodes(GUIGraph):
    def __init__(self, canvas=None, graph=None):
        GUIGraph.__init__(self, canvas, graph)


    def OnLeftDown(self, event):
        ## get the position of the click
        pos = self.Canvas.PixelToWorld(event.GetPosition())
        pos = tuple(pos)
        print "AddNodes : LeftDownEvent at : ", pos
        ## try and add a node at this position
        if not self.graph.has_node(pos):
            self.graph.add_node(pos)
        ## because state has likely changes we ReDraw
        self.update()


"""
ADD PIPES
    THIS GUI MODE IS FOR ADDING PIPES BETWEEN NODES
"""

## this GUI Mode adds edges to the graph
## check for selection of two nodes
## create an edge between two nodes (provided that they are not the same)
## draw a line to show where the edge would appear upon selection

class AddPipes(GUIGraph):
    def __init__(self, canvas=None, graph=None):
        GUIGraph.__init__(self, canvas, graph)
        self.first = None
        self.second = None

    def OnLeftDown(self, event):
        ## get the position of the click
        pos = self.Canvas.PixelToWorld(event.GetPosition())
        pos = tuple(pos)
        print "AddPipes : LeftDownEvent at : ", pos
        ## and if this is the first click
        if not self.first:
            ## then set the first selected node to be that node
            self.graph.selection = self.first = self.graph.get_closest_node(pos)
        ## Other wise if it's the second click
        else:
            ## set the second selected node to be that node
            self.graph.selection = self.second = self.graph.get_closest_node(pos)
        ## update the canvas
        self.update()

    def OnLeftUp(self, event):
        ## if two nodes have been selected that are not the same node
        if self.first and self.second and (self.first is not self.second):
            ## check for this edge in the graph
            edge = (self.first.pos, self.second.pos)
            if self.graph.has_edge(edge):
                print "cannot add edge"
                self.second = None
            ## if the edge doesn't already exist then add it
            else:
                self.graph.add_edge(self.first, self.second)
                self.graph.selection = self.first = self.second = None
        ## update the canvas
        self.update()


    def OnMove(self, event):
        ## if just the first node has been selected then draw a temporary
        ## line to show where the edge will be
        if self.first:
            pos = self.Canvas.PixelToWorld(event.GetPosition())
            line = (self.first.pos, pos)
            self.Canvas.AddArrowLine(line, LineWidth=2, LineColor=edgePreviewColor, ArrowHeadSize=10)
            ## update the canvas
            self.update()



"""
ADD NON-PIPE ELEMENTS
    THIS GUI MODE WILL ADD NON-PIPE ELEMENTS TO THE PIPES
"""

## this GUI mode will allow the user to add elements to edges on the
## graph by clicking them and will disallow duplicate elements

class AddNonPipeElement(GUIGraph):
    def __init__(self, canvas=None, graph=None, element_type=None):
        GUIGraph.__init__(self, canvas, graph)
        self.element_type = element_type

    def OnLeftDown(self, event):
        ## get the position of the click
        pos = self.Canvas.PixelToWorld(event.GetPosition())
        pos = tuple(pos)
        print "AddNonPipeElement : LeftDownEvent at : ", pos
        ## try and find an edge with that position
        ## the acceptable distance from the line must change with
        ## the amount you are zoomed in or out
        ##if no suitable edge is found then 'edge' will be 'None'
        edge = self.graph.get_closest_edge(pos, dist=10/self.Canvas.Scale)
        ## if the edge is not None
        if edge:
            pos = Geom.snapPointToLine((edge.first.pos, edge.second.pos), pos)
            ## if the pos does not already have an element at it
            if not (pos in edge):
                ##add the edge
                edge.add_element(edge, pos, self.element_type)
        ##update the canvas
        self.update()

"""
SELECTION
    THIS GUIMODE IS FOR SELECTING ANYTHING IN THE GRAPH FROM
    THE CANVAS BY CLICKING ON THEM
"""
class Select(GUIGraph):
    def __init__(self, canvas=None, graph=None):
        GUIGraph.__init__(self, canvas, graph)

    def OnLeftDown(self, event):
        pos = self.Canvas.PixelToWorld(event.GetPosition())
        pos = tuple(pos)
        print "Select : LeftDownEvent at : ", pos
        self.graph.selection = self.graph.get_closest(pos)
        self.update()

"""
MOVE
    THIS GUIMODE IS FOR MOVING ITEMS THAT HAVE BEEN SELECTED
"""

class Move(GUIGraph):
    def __init__(self, canvas = None, graph = None):
        GUIGraph.__init__(self, canvas, graph)
        self.premove_pos = None

    def OnLeftDown(self, event):
        pos = self.Canvas.PixelToWorld(event.GetPosition())
        pos = tuple(pos)
        print "Move : LeftDownEvent at : ", pos
        selection = self.graph.selection = self.graph.get_closest(pos)
        if selection:
            if isinstance(selection, edge.Edge):
                wx.MessageBox("Cannot move edge", "Alert!", wx.OK)
                selection = self.graph.selection = None
            else:
                self.premove_pos = selection.pos
        self.update()

    def OnLeftUp(self, event):
        if self.graph.selection:
            selection = self.graph.selection
            ## We want the message to be current to the present focus so the message must be reset here.
            self.message = "Moving node " + str(selection.label)
            self.message += " will delete all the non-pipe elements on pipes "
            self.message += "connected to it. Are you sure you want to move this node?"
            self.message += " Press 'Ok' to continue moving it"

            connected_edges = self.graph.get_edge(selection.pos)
            if selection.pos != self.premove_pos and connected_edges:
                for edge in connected_edges:
                    if not edge.elements():
                        continue
                    else:
                        decision = wx.MessageBox(self.message, "Move Warning!", wx.OK | wx.CANCEL )
                        if decision == wx.OK:
                            for edge in connected_edges:
                                edge.clear()
                            self.update()
                            return

                        elif decision == wx.CANCEL:
                            self.graph.change_node(selection.pos, new_pos=self.premove_pos)
                            self.update()
                            return



    def OnMove(self, event):
        selection = self.graph.selection
        if self.graph.selection and event.Dragging():
            pos = self.Canvas.PixelToWorld(event.GetPosition())
            pos = tuple(pos)
            if isinstance(selection, node.Node):
                self.graph.change_node(selection.pos, new_pos=pos)
                self.update()


"""
ZOOM
    FOR ZOOMING
"""

class ZoomIn(GUIMode.GUIZoomIn):
    def __init__(self, canvas, graph):
        GUIMode.GUIZoomIn.__init__(self, canvas)
        self.graph = graph

    def UpdateScreen(self):
        #if False:
        if self.PrevRBBox is not None:
            dc = wx.ClientDC(self.Canvas)
            dc.SetPen(wx.Pen('WHITE', 2, wx.SHORT_DASH))
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            dc.SetLogicalFunction(wx.XOR)
            dc.DrawRectanglePointSize(*self.PrevRBBox)
        self.Canvas.ClearAll(ResetBB=False)
        draw_graph(self.graph, self.Canvas)


class ZoomOut(GUIMode.GUIZoomOut):
    def __init__(self, canvas, graph):
        GUIMode.GUIZoomOut.__init__(self, canvas)
        self.graph = graph

    def UpdateScreen(self):
        self.Canvas.ClearAll(ResetBB=False)
        draw_graph(self.graph, self.Canvas)


###############################################################################
## DRAWING PANEL ##############################################################
###############################################################################

class DrawingPanel(wx.Panel):
    def __init__(self, parent, graph=None):
        wx.Panel.__init__(self, parent)

        self.graph = graph

        self.SetBackgroundColour('WHITE')
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

        self.Canvas = FloatCanvas.FloatCanvas(self, BackgroundColor=backgroundColor)



        # InitAll() sets everything in the Canvas to default state.
        # It can be used to reset the Canvas
        self.Canvas.InitAll()

        # This is all from Navcanvas, to keep funtionality, I'll take these calls to FloatCanvas.GUIMode and bind them
        # to the actual GUI Toolbar, later...
        self.Modes = {
                      "AddNodes": AddNodes(self.Canvas, self.graph),
                      "AddPipes": AddPipes(self.Canvas, self.graph),
                      "AddValves" : AddNonPipeElement(self.Canvas, self.graph, element_type="valve"),
                      "AddRegulators" : AddNonPipeElement(self.Canvas, self.graph, element_type="regulator"),
                      "AddCompressors" : AddNonPipeElement(self.Canvas, self.graph, element_type="compressor"),
                      "AddLossElements" : AddNonPipeElement(self.Canvas, self.graph, element_type="lossElement"),
                      "ZoomIn" :  ZoomIn(self.Canvas, self.graph),
                      "ZoomOut": ZoomOut(self.Canvas, self.graph),
                      "Pan" :  GUIMode.GUIMove(),
                      "Select" : Select(self.Canvas, self.graph),
                      "Move" : Move(self.Canvas, self.graph)
                     }


        # self.BuildToolbar()

        ## Create the vertical sizer for the toolbar and Panel
        # Remember that verticial means the widgets will stack vertically
        # You need to have a sizer for all widgets in the GUI
        # In general the hierarchy needs to be followed container --> widget
        box_sizer = wx.BoxSizer(wx.VERTICAL)
        # box_sizer.Add(self.ToolBar, 0, wx.ALL | wx.ALIGN_LEFT | wx.GROW, 4)

        # second parameter refers to "proportionality" so the toolbar to drawing area will be 1:6
        box_sizer.Add(self.Canvas, 1, wx.GROW)

        # Top most sizer has to be set
        self.SetSizerAndFit(box_sizer)

        self.Canvas.SetMode(GUIMode.GUIMouse())


    def update(self):
        draw_graph(self.graph, self.Canvas)
        self.Canvas.Draw()
        self.Canvas.ClearAll(ResetBB=False)
        # draw_graph(self.graph, self.Canvas)
    # REMOVE LATER, MOVE FUNCTIONALITY TO RIBBON TOOLBAR

    # def BuildToolbar(self):
    #     """
    #     This is here so it can be over-ridden in a ssubclass, to add extra tools, etc
    #     """
    #     tb = wx.ToolBar(self)
    #     self.ToolBar = tb
    #
    #     tb.SetToolBitmapSize((24, 24))
    #     self.AddToolbarModeButtons(tb, self.Modes)
    #
    #     tb.Realize()

    # def AddToolbarModeButtons(self, tb, Modes):
    #     self.ModesDict = {}
    #     for Mode in Modes:
    #         tool = tb.AddRadioTool(wx.ID_ANY, shortHelp=Mode[0], bitmap=Mode[2])
    #         self.Bind(wx.EVT_TOOL, self.SetMode, tool)
    #         self.ModesDict[tool.GetId()]=Mode[1]
    #     #self.ZoomOutTool = tb.AddRadioTool(wx.ID_ANY, bitmap=Resources.getMagMinusBitmap(), shortHelp = "Zoom Out")
    #     #self.Bind(wx.EVT_TOOL, lambda evt : self.SetMode(Mode=self.GUIZoomOut), self.ZoomOutTool)
    #
    #
    #
    # def HideShowHack(self):
    #     ##fixme: remove this when the bug is fixed!
    #     """
    #     Hack to hide and show button on toolbar to get around OS-X bug on
    #     wxPython2.8 on OS-X
    #     """
    #     self.ZoomButton.Hide()
    #     self.ZoomButton.Show()

    ## takes a string argument that is a key to the modes
    ## dictionary
    def SetMode(self, arg_mode):
        self.Canvas.SetMode(self.Modes[arg_mode])
        draw_graph(self.graph, self.Canvas)
        self.Canvas.Draw()
        self.Canvas.ClearAll(ResetBB=False)
