class edge:
    def __init__(self, nodePrev, nodeNext):
        # Initialize the edge with previous and next nodes
        self.nodePrev = nodePrev
        self.nodeNext = nodeNext
        # Default weight of the edge is set to 1
        self.weight = 1

    def isEdge(self, nodePrevCheck, nodeNextCheck):
        # Check if the provided nodes are None
        if nodePrevCheck is None or nodeNextCheck is None:
            return False
        # Check if the content of the provided nodes matches the edge's nodes
        return nodeNextCheck.content == self.nodeNext.content and nodePrevCheck.content == self.nodePrev.content

    def increaseWeight(self):
        # Increase the weight of the edge by 1
        self.weight += 1
