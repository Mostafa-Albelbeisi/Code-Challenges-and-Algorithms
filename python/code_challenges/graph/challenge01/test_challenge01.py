# Write your test here

import pytest
from challenge01 import Graph


def test3():
    g = Graph()
    nodeA = g.add_node("a")
    nodeB = g.add_node("b")
    nodeC = g.add_node("c")
    nodeD = g.add_node("d")
    nodeE = g.add_node("e")
    nodeF = g.add_node("f")
    nodeG = g.add_node("g")
    g.add_edge(nodeA, nodeB)
    g.add_edge(nodeA, nodeC)
    g.add_edge(nodeB, nodeC)
    g.add_edge(nodeC, nodeD)
    g.add_edge(nodeC, nodeE)
    g.add_edge(nodeD, nodeF)
    g.add_edge(nodeE, nodeF)
    g.add_edge(nodeF, nodeG)
    actual = g.BF(nodeC)
    expected = ["c", "a", "b", "d", "e", "f", "g"]
    assert actual == expected


def test4():
    g = Graph()
    nodeA = g.add_node("a")
    nodeB = g.add_node("b")
    nodeC = g.add_node("c")
    nodeD = g.add_node("d")
    nodeE = g.add_node("e")
    nodeF = g.add_node("f")
    nodeG = g.add_node("g")
    g.add_edge(nodeA, nodeB)
    g.add_edge(nodeA, nodeC)
    g.add_edge(nodeB, nodeC)
    g.add_edge(nodeC, nodeD)
    g.add_edge(nodeC, nodeE)
    g.add_edge(nodeD, nodeF)
    g.add_edge(nodeE, nodeF)
    g.add_edge(nodeF, nodeG)
    actual = g.BF(nodeG)
    expected = ["g", "f", "d", "e", "c", "a", "b"]
    assert actual == expected
