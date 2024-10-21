import random
import pyttsx3

class graph:
    def __init__(self):
        self.nodeList = []  # Initialize an empty list to store nodes

    def findNode(self, content):
        # Search for a node with the given content in the nodeList
        for node in self.nodeList:
            if node.content == content:
                return node
        return None  # Return None if no node with the given content is found

    def start(self, numberIterations):
        # Randomly select a starting node from the nodeList
        current_node = random.choice(self.nodeList)
        lyric = ""  # Initialize an empty string to build the lyric
        for count in range(numberIterations):
            if count%50==0 and numberIterations!=0:
                lyric+=". \n\n"
            lyric += " " + current_node.content  # Append the current node's content to the lyric
            edgeList = current_node.getEdgeList()  # Get the list of edges from the current node

            if not edgeList:  # If the current node has no edges
                current_node = random.choice(self.nodeList)  # Randomly select a new current node
                continue

            # Create lists of next nodes and their corresponding weights
            nodes = [edge.nodeNext for edge in edgeList]
            weights = [edge.weight for edge in edgeList]

            # Randomly select the next node based on the weights of the edges
            current_node = random.choices(nodes, weights=weights)[0]

        # Initialize the text-to-speech engine
        lyric = lyric.lstrip().capitalize()
        lyric = "\n".join(sentence.lstrip().capitalize() for sentence in lyric.split("\n"))
        lyric += "."
        engine = pyttsx3.init()
        engine.say(lyric)  # Use the engine to say the generated lyric
        print(lyric)  # Print the generated lyric