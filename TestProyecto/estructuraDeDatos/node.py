class node:
    def __init__(self, content=""):
        # Initialize the node with content and an empty edge list
        self.content = content
        self.edgeList = []

    def addEdgeToList(self, edge):
        # Add an edge to the edge list
        self.edgeList.append(edge)

    def getEdgeList(self):
        # Return the list of edges
        return self.edgeList

    def setEdgeList(self, newList):
        # Set the edge list to a new list
        self.edgeList = newList
