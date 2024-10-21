import re
import random
from unidecode import unidecode
import os
import networkx as nx
import plotly.graph_objects as go

class Edge:
    def __init__(self, nodePrev, nodeNext):
        self.nodePrev = nodePrev
        self.nodeNext = nodeNext
        self.weight = 1

    def isEdge(self, nodePrevCheck, nodeNextCheck):
        if nodePrevCheck is None or nodeNextCheck is None:
            return False
        return nodeNextCheck.content == self.nodeNext.content and nodePrevCheck.content == self.nodePrev.content

    def increaseWeight(self):
        self.weight += 1

class Node:
    def __init__(self, content=""):
        self.content = content
        self.edgeList = []

    def addEdgeToList(self, edge):
        self.edgeList.append(edge)

    def getEdgeList(self):
        return self.edgeList

    def setEdgeList(self, newList):
        self.edgeList = newList

class Graph:
    def __init__(self):
        self.nodeList = []
        self.nxGraph = nx.Graph()  # Crear un grafo con NetworkX

    def findNode(self, content):
        for node in self.nodeList:
            if node.content == content:
                return node
        return None

    def start(self, numberIterations):
        current_node = random.choice(self.nodeList)
        lyric = ""
        for _ in range(numberIterations):
            lyric += " " + current_node.content
            edgeList = current_node.getEdgeList()
            if not edgeList:
                current_node = random.choice(self.nodeList)
                continue
            nodes = [edge.nodeNext for edge in edgeList]
            weights = [edge.weight for edge in edgeList]
            current_node = random.choices(nodes, weights=weights)[0]
        print(lyric)

    def addEdgeToNxGraph(self, nodePrev, nodeNext, weight):
        """Añade una arista al grafo de NetworkX."""
        self.nxGraph.add_edge(nodePrev.content, nodeNext.content, weight=weight)

    def visualizeGraph3D(self):
        """Genera una visualización en 3D del grafo."""
        pos = nx.spring_layout(self.nxGraph, dim=3)  # Posiciones en 3D
        x_nodes = [pos[key][0] for key in self.nxGraph.nodes()]
        y_nodes = [pos[key][1] for key in self.nxGraph.nodes()]
        z_nodes = [pos[key][2] for key in self.nxGraph.nodes()]

        edge_trace = []
        for edge in self.nxGraph.edges(data=True):
            x0, y0, z0 = pos[edge[0]]
            x1, y1, z1 = pos[edge[1]]
            edge_trace.append(go.Scatter3d(
                x=[x0, x1, None], y=[y0, y1, None], z=[z0, z1, None],
                mode='lines',
                line=dict(width=edge[2]['weight'], color='blue'),
                opacity=0.5
            ))

        node_trace = go.Scatter3d(
            x=x_nodes, y=y_nodes, z=z_nodes,
            mode='markers',
            marker=dict(size=8, color='red'),
            text=list(self.nxGraph.nodes()),
            hoverinfo='text'
        )

        layout = go.Layout(
            title="3D Visualization of Graph",
            scene=dict(
                xaxis=dict(showbackground=False),
                yaxis=dict(showbackground=False),
                zaxis=dict(showbackground=False),
            ),
            margin=dict(l=0, r=0, b=0, t=50)
        )

        fig = go.Figure(data=edge_trace + [node_trace], layout=layout)
        fig.show()

# Función para cargar y procesar archivos de textods    

def fileReading():
    phrases = []

    for x in range(10):
        filename = f"TestProyecto/canciones/doc{x}.txt"

        if not os.path.exists(filename):
            print(f"{filename} Do not exist")
            continue

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    curatedLine = re.sub(r"[,\(\)'\.!]", "", line).strip().lower()
                    curatedLine = unidecode(curatedLine)
                    if curatedLine:
                        phrases.append(curatedLine)
        except Exception as e:
            print(f"Error in {filename}: {e}")

    if not phrases:
        print("Phrases is empty")

    return phrases

phrases = fileReading()

if phrases:
    graph = Graph()

    for lines in phrases:
        words = lines.split(" ")

        for index, word in enumerate(words):

            node = graph.findNode(word)

            if node is None:
                node = Node(word)
                graph.nodeList.append(node)

            nextElement = words[index + 1] if index + 1 < len(words) else None

            nextNode = graph.findNode(nextElement)

            if nextNode is None and nextElement is not None:
                nextNode = Node(nextElement)
                graph.nodeList.append(nextNode)

            nodeEdgeList = node.getEdgeList()
            edge_found = False
            for edge in nodeEdgeList:
                if edge.isEdge(node, nextNode):
                    edge.increaseWeight()
                    edge_found = True
                    break

            if not edge_found and nextNode is not None:
                new_edge = Edge(node, nextNode)
                node.addEdgeToList(new_edge)
                graph.addEdgeToNxGraph(node, nextNode, new_edge.weight)  # Añadir arista al grafo de NetworkX

    graph.start(150)
    graph.visualizeGraph3D()  # Llamar a la función para visualizar el grafo en 3D
else:
    print("No se pudo generar el grafo")
