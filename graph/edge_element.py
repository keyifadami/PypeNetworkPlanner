###############################################################################
##EDGE ELEMENT#################################################################
###############################################################################

## the Edge element is a parent class for
## Valve, Compressor, Regulator and Loss Element
## it's Constructor takes a position tuple( x, y) coordinate
## and a flow switch (a positive or negative number (+1/-1) to signify
## the direction of flow on the Edge(pipe) )
class EdgeElement(object):
    def __init__(self, edge, pos, label, edgeLabel):
        self.edge = edge
        self.pos = pos
        self.label = label
        self.edgeLabel = edgeLabel


class Valve(EdgeElement):
    def __init__(self, edge, pos, label, edgeLabel):
        EdgeElement.__init__(self, edge, pos, label, edgeLabel)

class Compressor(EdgeElement):
    def __init__(self, edge, pos, label, edgeLabel):
        EdgeElement.__init__(self, edge, pos, label, edgeLabel)

class Regulator(EdgeElement):
    def __init__(self, edge, pos, label, edgeLabel):
        EdgeElement.__init__(self, edge, pos, label, edgeLabel)

class LossElement(EdgeElement):
    def __init__(self, edge, pos, label, edgeLabel):
        EdgeElement.__init__(self, edge, pos, label, edgeLabel)
