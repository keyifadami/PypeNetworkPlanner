from multi_key_dict import multi_key_dict
from utils import geometry as Geom
from node import Node
from edge import Edge
from edge_element import EdgeElement

import wx.dataview as dv
import copy

###############################################################################
##GRAPH########################################################################
###############################################################################

'''
    This is the graph structure
    and these are it's contracts
    CONTRACTS:
    1)
        the graph disallows adding duplicate nodes
    2)
        the graph will auto label the graph if the label argument given
        to addNode is equal to -1, which it is by default
    3)
        if the focus node is deleted the focus node becomes
        the last node in the list
'''

class Graph(object):
    def __init__(self):
        ##an empty dict of nodes keyed by pos (x,y) and label
        self._nodes = {}
        ## an empty dict of edges keyed by pos of ((x1,y1),(x2,y2)) and label
        self._edges = {}
        ## integer for automatically assigning node Labels
        self._node_label = 0
        ## integer for automatically assigning edge labels
        self._edge_label = 0
        ## because I don't have to worry about type I'll just put this here
        self.selection = None
        ## this is for the nodeTabPanel's listctrl


    def nodes(self):
        return copy.copy(self._nodes)

    def edges(self):
        return copy.copy(self._edges)

    ###########################################################################
    ## NODE mutators and accessors ############################################
    ###########################################################################

    def get_node_count(self):
        return len(self._nodes)

    ## add node will automatically label the nodes
    ## if no label argument is given other wise it will
    ## just construct a node with the given information
    def add_node(self, pos, label=None):
        ## this function adds a node to the dictionary
        ## using the node's label and pos as keys
        ## it will not add a duplicate node
        ## it will simply return without doing anything
        ## NO ERROR is RAISED
        ## this will disallow adding a node too close to another node
        node = self.get_closest_node(pos)
        if self._nodes.has_key(pos) or node:
            return
        else:
            if not label:
                node = Node(pos, self._node_label)
                self._node_label+=1
            else:
                node = Node(pos, label)

            self._nodes[node.pos] = node


    ## if you pass a bad key into either of these you will get an Error
    ## so don't do that
    def delete_node(self, key):
        del self._nodes[key]

    ## this is nessecary because if we change the pos
    ## then we have to rekey the node
    def change_node(self, key, new_pos=None, new_label=None, new_name=None):
        if new_pos is None and new_label is None:
            return
        node = self._nodes[key]
        if new_pos:
            if not self.get_closest_node(new_pos):
                node.pos = new_pos
                self._nodes[new_pos] = node
                del self._nodes[key]
        if new_label:
            node.label = new_label
        if new_name:
            node.name = new_name

        ## because we changed the node's position and rekeyed it we also have to
        ## change the key of any edges connected to it

        ## So basically I am just rekeying the whole dictionary here but
        ## attempts to do something "more" efficient have failed so far
        ## so I'll just flag it for future revisiting
        ## !!!!!!!!!!!!!!!!!!!!! REVISIT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        edge_keys = self._edges.keys()
        new_edge_dict = {}
        for k in edge_keys:
            edge = self._edges[k]
            new_key = (edge.first.pos, edge.second.pos)
            new_edge_dict[new_key] = edge

        self._edges = new_edge_dict

    def get_node(self, key):
        return self._nodes[key]

    def has_node(self, key):
        return self._nodes.has_key(key)

    def get_closest_node(self, point, dist = 8):
        for node in self._nodes.itervalues():
            distance = Geom.dist(point, node.pos)
            if distance <= dist:
                return node
        return None

    ###########################################################################
    ## EDGE mutators and accessors ############################################
    ###########################################################################

    def get_edge_count(self):
        return len(self._edges)

    ## add edge similar to add node will automatically label
    ## the edges if no label argument is given
    def add_edge(self, first , second, label=None):
        ## this function adds an edge to the edge dictionary
        ## using the edges label and an a tuple of tuples
        ## that is ((N1x, N1y), (N2x,N2y))
        ## it will not add duplicvate nodes
        ## nor will it add a back-edge (n1,n2) and (n2,n1)
        ## it will simply return without doing anything
        ## NO ERROR IS RAISED
        pos = (first.pos, second.pos)
        if self._edges.has_key((first.pos,second.pos)) or self._edges.has_key((second.pos, first.pos)):
            return
        else:
            if not label:
                edge = Edge(first, second, self._edge_label)
                self._edge_label+=1
            else:
                edge = Edge(first, second, label)

            self._edges[pos] = edge



    def delete_edge(self, key):
        del self._edges[key]

    ## this function is nessecary because if we chage the nodes then
    ## we have to rekey the edge
    def change_edge(self, key, new_first=None, new_second=None, new_label=None):
        edge = self._edges[key]
        if new_first and new_first is not edge.first:
            edge.first = new_first
            self._edges[(edge.first.pos, edge.second.pos)] = edge
            del self._edges[key]
        elif new_second and new_second is not edge.second:
            edge.first = new_first
            self._edges[(edge.first.pos, edge.second.pos)] = edge
            del self._edges[key]
        elif new_first and new_second and new_first is not edge.first and new_second is not edge.second:
            edge.first = new_first
            edge.second = new_second
            self._edges[(edge.first.pos, edge.second.pos)] = edge
            del self._edges[key]
        if new_label:
            edge.label = new_label

    ## if an edge key is given this will return a single edge
    ## if a node key is give it will return a list of all edges
    ## connceted to that node
    ## if there are no edges found then an empty list is returned
    def get_edge(self, key):
        if self._edges.has_key(key):
            return self._edges[key]
        edges = []
        for node_key in self._nodes.iterkeys():
            if node_key is key:
                continue
            elif self._edges.has_key((node_key, key)):
                edges.append(self._edges[(node_key,key)])
            elif self._edges.has_key((key, node_key)):
                edges.append(self._edges[(key, node_key)])
            else:
                continue
        return edges

    ## this can take a node key, or edge key
    def has_edge(self, key):
        if self._edges.has_key(key):
            return True
        else:
            for node_key in self._nodes.iterkeys():
                if node_key is key:
                    continue
                elif self._edges.has_key((node_key, key)):
                    return True
                elif self._edges.has_key((key, node_key)):
                    return True
                else:
                    continue
            return False


    ## this function is a little weird but nesseccary
    ## it will find an edge that is closest to a given
    ## point within a certain distance
    def get_closest_edge(self, point, dist = 8):
        for edge in self._edges.itervalues():
            line = (edge.first.pos, edge.second.pos)
            distance = Geom.distFromLineSeg(line, point)
            if distance <= dist:
                return edge
        return None

    def get_closest_edge_element(self, point, dist = 8):
        for edge in self._edges.itervalues():
            for element in edge.elements().itervalues():
                distance = Geom.dist(point, element.pos)
                if distance <= dist:
                    return element
        return None

    ###########################################################################
    ## GRAPH mutators and accessors ############################################
    ###########################################################################

    def delete_selection(self):
        if self.selection:
            if isinstance(self.selection, Node):
                self.delete_node(self.selection.pos)
                edges = self.get_edge(self.selection.pos)
                for edge in edges:
                    self.delete_edge((edge.first.pos, edge.second.pos))
                self.selection = None
            elif isinstance(self.selection, Edge):
                self.delete_edge((self.selection.first.pos, self.selection.second.pos))
                self.selection = None
            elif isinstance(self.selection, EdgeElement):
                self.selection.edge.delete(self.selection)
                self.selection = None
            else:
                return

    def __getitem__(self, key):
        if self._nodes.has_key(key):
            return self._nodes[key]
        elif self._edges.has_key(key):
            return self._edges[key]
        else:
            raise KeyError(str(key))

    def get_closest(self, point, dist = 8):
        node = self.get_closest_node(point)
        if node:
            return node
        edgeElement = self.get_closest_edge_element(point)
        if edgeElement:
            return edgeElement
        edge = self.get_closest_edge(point)
        if edge:
            return edge
        return None
