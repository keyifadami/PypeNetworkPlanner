from edge_element import Valve, Compressor, Regulator, LossElement

###############################################################################
##EDGE#########################################################################
###############################################################################

class Edge(object):
    def __init__(self, n1, n2, label, name="Unnamed"):
        self.first = n1
        self.second = n2
        self.label = label
        self.name = name
        self._elements = {}
        ## for auto creating labels
        self._element_label = 0

    def elements(self):
        return self._elements

    ## this will check
    def add_element(self, edge, pos, element_type, label=None):
        ## We won't allow duplicate elements or elements in the same place
        ## however trying will not cause and error
        if (pos in self._elements):
            return
        ## add the approriate element to the dict
        ## keyed by pos
        if element_type == "valve":
            if not label:
                self._elements[pos] = Valve(edge, pos, self._element_label, self.label)
                self._element_label += 1
            else:
                self._elements[pos] = Valve(edge, pos, label, self.label)
        elif element_type == "compressor":
            if not label:
                self._elements[pos] = Compressor(edge, pos, self._element_label, self.label)
                self._element_label += 1
            else:
                self._elements[pos] = Compressor(edge, pos, label, self.label)
        elif element_type == "regulator":
            if not label:
                self._elements[pos] = Regulator(edge, pos, self._element_label, self.label)
                self._element_label += 1
            else:
                self._elements[pos] = Regulator(edge, pos, label, self.label)
        elif element_type == "lossElement":
            if not label:
                self._elements[pos] = LossElement(edge, pos, self._element_label, self.label)
                self._element_label += 1
            else:
                self._elements[pos] = LossElement(edge, pos, label, self.label)
        ## if a bad type was used then raise a name error
        else:
            error = "'" + str(element_type) + "' is not a recognized element type"
            raise ValueError(error)

    def delete(self, element):
        del self._elements[element.pos]

    def clear(self):
        self._elements.clear()

    def __contains__(self, key):
        return (key in self._elements)
