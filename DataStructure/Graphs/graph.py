class graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjecentList = {}

    def addVertex(self, node):
        try:
            self.adjecentList[node] = []
        except Exception as e:
            print(e)

    def addEdge(self, node1, node2):
        try:
            self.adjecentList[node1].append(node2)
            self.adjecentList[node2].append(node1)
        except Exception as e:
            print(e)

    def show(self):
        print(self.adjecentList)


myGraph = graph()
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.show()
myGraph.addEdge(1, 2)
myGraph.show()
myGraph.addVertex(3)
myGraph.addVertex(3)
myGraph.addEdge(2, 3)
myGraph.addEdge(2, 4)
myGraph.show()
