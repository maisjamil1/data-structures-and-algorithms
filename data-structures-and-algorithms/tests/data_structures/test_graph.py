from data_structures_and_algorithms.data_structures.graph.graph import Graph


def test_add_to_graph():
    graph = Graph()
    graph.add_node('node1')
    actual = graph.get_nodes()
    expected = {'node1': []}
    assert expected == actual

def test_edge():
    graph=Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_edge('a', 'b', 8)

    actual = graph.get_neighbors('a')
    expected = 'a :edge--> b ... weight: 8'
    assert actual == expected

def test_nodes_retrived():
    graph=Graph()
    graph.add_node('a')
    graph.add_node('b')
    actual = graph.get_nodes()
    expected = {'a': [],'b': []}
    assert expected == actual

def test_neighbors_retrived():
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
    actual = graph.get_nodes()
    expected = {'node1': [['node2', 5], ['node4', 3], ['node1', 2]], 'node2': [['node4', 1]], 'node3': [], 'node4': []}
    assert expected == actual


def test_size():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')


    actual = graph.size()
    expected = 2
    assert expected == actual

def test_one_node():
    graph = Graph()
    graph.add_node('node1')
    graph.add_edge('node1','node1')
    actual = graph.get_neighbors('node1')
    expected = 'node1 :edge--> node1 ... weight: 1'
    assert expected == actual

def test_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    excepted = None
    assert excepted == actual