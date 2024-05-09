WHITE = "white"
BLACK = "black"
GRAY = "gray"
import math
class Graph:
    def _buildAdjMatrix(self):
        self.adjMat = [[0 for v in range(len(self.vertexes))] for v in range(len(self.vertexes))] #V2
        for relation in self.relations:
            row, col = self.encoder[relation[0]], self.encoder[relation[1]]
            # Que se hace aquí y por qué es igual a 1?
            self.adjMat[row][col] = 1

    def _buildEncoding(self):
        self.encoder, self.decoder = {}, {}
        index = 0
        for v in self.vertexes:
            self.encoder[v] = index
            self.decoder[index] = v
            index = index + 1
    def _buildAdjList(self):
        self.adjList = {}
        for v in self.vertexes:
            self.adjList[v] = []
        for relation in self.relations:
            self.adjList[relation[0]].append(relation[1])