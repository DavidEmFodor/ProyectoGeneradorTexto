import re
from unidecode import unidecode
import os
import pyttsx3
from estructuraDeDatos.graph import graph
from estructuraDeDatos.edge import edge
from estructuraDeDatos.node import node

""" Returns list of strings

Go through 10 .txt docs in the canciones folder, if it doesn't find it, it tells you,
it cleans all the unwanted characters and appends it to the phrases list that will be returned
"""
def fileReading(): 
    phrases = []
    for x in range(0, 10):
        filename = f"TestProyecto/canciones/doc{x}.txt"
        if not os.path.exists(filename):
            print(f"{filename} don't found")
            continue
        
        with open(filename, 'r', encoding='utf-8') as lyric:
            for line in lyric:
                # Clean unwanted characters, normalize, and convert to lowercase
                curatedLine = re.sub(r"[,\(\)'\.!?\s]+", " ", line).strip().lower()
                curatedLine = unidecode(curatedLine)  
                if curatedLine: 
                    phrases.append(curatedLine)
    if not phrases:
        print("txt files empty.")
    return phrases

# Read phrases from files
phrases = fileReading()
if phrases:
    Maingraph = graph()

    for lines in phrases:
        words = lines.split(" ")

        for index, word in enumerate(words):
            # Find or create the current node
            nodes = Maingraph.findNode(word)
            if nodes is None:
                nodes = node(word)
                Maingraph.nodeList.append(nodes)

            # Find or create the next node
            nextElement = words[index + 1] if index + 1 < len(words) else None
            nextNode = Maingraph.findNode(nextElement)
            if nextNode is None and nextElement is not None:
                nextNode = node(nextElement)
                Maingraph.nodeList.append(nextNode)

            # Check if an edge exists between the current node and the next node
            nodeEdgeList = nodes.getEdgeList()
            edge_found = False
            for edges in nodeEdgeList:
                if edges.isEdge(nodes, nextNode):
                    edges.increaseWeight() 
                    edge_found = True
                    break

            # If no edge exists, create a new edge
            if not edge_found and nextNode is not None:
                new_edge = edge(nodes, nextNode)
                nodes.addEdgeToList(new_edge)
    
    # Start the graph with a parameter (e.g., 1000) that will be the number of words generated
    Maingraph.start(1000)
else:
    print("Graph couldn't be created")
