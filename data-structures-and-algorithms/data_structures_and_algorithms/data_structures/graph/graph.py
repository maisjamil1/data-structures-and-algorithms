class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        if value in self._adjacency_list:
            return
        self._adjacency_list[node.value] = []





    def add_edge(self, start_node, end_node, weight=1):
        if start_node not in self._adjacency_list.keys():
           return
        elif end_node not in self._adjacency_list.keys():
            return
        else:
            temp = [end_node, weight]
            self._adjacency_list[start_node].append(temp)




    def get_nodes(self):
        if self._adjacency_list:
            return self._adjacency_list

    def get_neighbors(self, node):
        for edges in self._adjacency_list[node]:
               return f"{node} :edge--> {edges[0]} ... weight: {edges[1]}"

    def size(self):
        return len(self._adjacency_list)





if __name__ == "__main__":
    graph = Graph()
    graph.add_node('node1')
    graph.add_node('node2')
    graph.add_node('node3')
    graph.add_node('node4')
    graph.add_node('node2')

    graph.add_edge('node1', 'node2', 5)
    graph.add_edge('node1', 'node4', 3)
    graph.add_edge('node2', 'node4', 1)
    graph.add_edge('node1', 'node1', 2)
    print(graph.get_nodes())

    print(graph.get_neighbors('node1'))
    print(graph.size())
