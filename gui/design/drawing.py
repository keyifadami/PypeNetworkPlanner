## drawing is a module that provides an interface between the
## graph and the drawingPanel. Much of the code here is simple
## math for translating and moving lines and points
## not very interesting but necessary

import graph.edge_element as EE
import utils.geometry as Geom
import types
from colors import *

NODE_SIZE = 8
EDGE_SIZE = 2

def draw_edge_element(element, line, Canvas, isSelected = False):
    if isinstance(element, EE.Valve):
        t_size =  8 / Canvas.Scale
        point = element.pos
        ## Make the T shape with lines
        downPoint = (point[0] , point[1]-t_size/2)
        upPoint = (point[0], point[1]+t_size)
        rightPoint = (point[0]+t_size, point[1]+t_size)
        leftPoint = (point[0]-t_size, point[1]+t_size)

        ## rotate the T shape to always be normal to the edge
        theta = Geom.angleFromXaxis(line)
        lines = [leftPoint, rightPoint , upPoint, downPoint]
        lines = Geom.rotatePointList(lines, theta, point)

        if isSelected:
            Canvas.AddLine(
                [lines[0], lines[1]],
                LineWidth=16,
                LineColor=highLightColor
            )
            Canvas.AddLine(
                [lines[2], lines[3]],
                LineWidth=16,
                LineColor=highLightColor
            )
        Canvas.AddLine(
            [lines[0], lines[1]],
            LineWidth=4,
            LineColor="BLUE"
        )
        Canvas.AddLine(
            [lines[2], lines[3]],
            LineWidth=4,
            LineColor="BLUE"
        )

    elif isinstance(element, EE.Compressor):
        c_w = 8 / Canvas.Scale
        c_h_long = 10 /Canvas.Scale
        c_h_short = 3 / Canvas.Scale
        point = element.pos
        leftPoint = (point[0]-c_w, point[1])
        rightPoint = (point[0]+c_w, point[1])



        def rightCompressor(l_point, r_point):
            upLeftPoint = (l_point[0], l_point[1]+c_h_long)
            downLeftPoint = (l_point[0], l_point[1]-c_h_long)
            upRightPoint = (r_point[0], r_point[1]+c_h_short)
            downRightPoint = (r_point[0], r_point[1]-c_h_short)
            return [upLeftPoint, downLeftPoint, downRightPoint, upRightPoint]

        def leftCompressor(l_point, r_point):
            upLeftPoint = (l_point[0], l_point[1]+c_h_short)
            downLeftPoint = (l_point[0], l_point[1]-c_h_short)
            upRightPoint = (r_point[0], r_point[1]+c_h_long)
            downRightPoint = (r_point[0], r_point[1]- c_h_long)
            return [upLeftPoint, downLeftPoint, downRightPoint, upRightPoint]


        ## find the change in x on the line to determine the
        ## direction of the edge
        delta_x = Geom.delta_x(*line)

        ## get the angle that the line makes with the x-axis
        theta = Geom.angleFromXaxis(line)

        ## if it's negative the direction in the x is right justified
        if delta_x < 0:
            ## so we construct a right justified shape
            compressor = rightCompressor(leftPoint, rightPoint)

        ## if it's positive the direction in the x is left justified
        elif delta_x > 0:
            ## so we construct a left justified shape
            compressor = leftCompressor(leftPoint, rightPoint)

        ## Uh Oh Vertical lines, now we have to think about the change in y
        elif delta_x == 0:
            ## the change in y
            delta_y = Geom.delta_y(*line)

            ## if it's positive then the direction in the y is up
            if delta_y < 0:
                ## since we will ultimately be rotating 90 degrees
                ## for a vertical line pointing up
                ## we want the shape to be right justified
                ## (think about it)
                compressor = rightCompressor(leftPoint, rightPoint)

            ##if it's negative then the direction in the y is down
            elif delta_y > 0:
                ## and we construct a left justified shape
                compressor = leftCompressor(leftPoint, rightPoint)

        ## if the delta y is also zero then our line is two of
        ## the same point and we have some bad input
        ## since this code is just for prototyping and fast development
        ## we will make due with a descriptive warning message printed
        ## to the console, and we'll make compressor right justified
        ## don't worry if this happens it will be obvious
        else:
            compressor = rightCompressor(leftPoint, rightPoint)


        ## and then we rotate it acordingly
        compressor = Geom.rotatePointList(compressor, theta, point)

        ## finally we draw this darned thing to the Canvas
        if isSelected:
            Canvas.AddPolygon(
                compressor,
                LineWidth=16,
                LineColor=highLightColor,
            )
        Canvas.AddPolygon(
            compressor,
            LineWidth=1,
            LineColor="BLUE",
            FillColor="BLUE",
        )

    elif isinstance(element, EE.Regulator):
        r_size = 8 / Canvas.Scale
        point = element.pos
        rightPoint = (point[0] - r_size, point[1])
        leftPoint = (point[0] + r_size, point[1])
        upRightPoint = (rightPoint[0], rightPoint[1]+ r_size)
        downRightPoint = (rightPoint[0], rightPoint[1]-r_size)
        upLeftPoint = (leftPoint[0], leftPoint[1]+r_size)
        downLeftPoint = (leftPoint[0], leftPoint[1]-r_size)

        theta = Geom.angleFromXaxis(line)

        firstTriangle = [point, upRightPoint, downRightPoint]
        secondTriangle = [point, upLeftPoint, downLeftPoint]

        firstTriangle = Geom.rotatePointList(firstTriangle, theta, point)
        secondTriangle = Geom.rotatePointList(secondTriangle, theta, point)

        if isSelected:
            Canvas.AddPolygon(
                firstTriangle,
                LineWidth=16,
                LineColor=highLightColor,
            )
            Canvas.AddPolygon(
                secondTriangle,
                LineWidth=16,
                LineColor=highLightColor,
            )
        Canvas.AddPolygon(
            firstTriangle,
            LineWidth=1,
            LineColor="BLUE",
            FillColor="BLUE",
        )
        Canvas.AddPolygon(
            secondTriangle,
            LineWidth=1,
            LineColor="BLUE",
            FillColor="BLUE",
        )

    elif isinstance(element, EE.LossElement):
        l_size = 8 / Canvas.Scale
        point = element.pos
        upPoint = (point[0], point[1]+ l_size)
        downPoint = (point[0], point[1] - l_size)
        rightPoint = (point[0] + l_size, point[1] - l_size)
        lines = [upPoint, downPoint, rightPoint]
        theta = Geom.angleFromXaxis(line)
        lines = Geom.rotatePointList(lines, theta, point)
        if isSelected:
            Canvas.AddLine(
                [lines[0], lines[1]],
                LineWidth=16,
                LineColor=highLightColor
            )
            Canvas.AddLine(
                [lines[1], lines[2]],
                LineWidth=16,
                LineColor=highLightColor
            )
        Canvas.AddLine(
            [lines[0], lines[1]],
            LineWidth=4,
            LineColor="BLUE"
        )
        Canvas.AddLine(
            [lines[1], lines[2]],
            LineWidth=4,
            LineColor="BLUE"
        )

    else:
        error = str(type(element)) + " as element in draw_edge_element(element, line, Canvas, isSelected=False)"
        raise ValueError(error)

    label = "edge : " + str(element.edgeLabel) + "\nelement : " + str(element.label)
    Canvas.AddScaledText(label, element.pos, Size = 10, Color = labelColor)


def draw_node(node, Canvas, isSelected = False):
    if isSelected:
        Canvas.AddCircle(
            node.pos,
            NODE_SIZE + 6,
            LineWidth=6,
            LineColor=highLightColor,
        )
    if node.pos:
        Canvas.AddCircle(
            node.pos,
            NODE_SIZE,
            LineWidth=1,
            LineColor='BLACK',
            FillColor='BLACK'
        )
        label = "Node : " + str(node.label) + "\n" + str(node.name)
        Canvas.AddScaledText(label, node.pos, Size = 15, Color = labelColor)



def draw_edge(edge, Canvas, isSelected = False):
    line = (edge.first.pos, edge.second.pos)
    if isSelected:
        Canvas.AddLine(
            line, LineWidth=EDGE_SIZE + 8,
            LineColor = highLightColor,
        )

    Canvas.AddArrowLine(
        line, LineWidth=EDGE_SIZE,
        LineColor="BLACK",
        ArrowHeadSize=10
    )
    label = "Edge : " + str(edge.label) + "\n" + str(edge.name)
    Canvas.AddScaledText(label, Geom.midpoint(line[0], line[1]), Size = 15, Color = labelColor)


def draw_graph(graph, Canvas):
    for edge in graph.edges().itervalues():
            isSelected = edge is graph.selection
            draw_edge(edge, Canvas, isSelected)
            line = (edge.first.pos, edge.second.pos)
            for element in edge.elements().itervalues():
                isSelected = element is graph.selection
                draw_edge_element(element, line, Canvas, isSelected)
    for node in graph.nodes().itervalues():
        isSelected = node is graph.selection
        draw_node(node, Canvas, isSelected)
