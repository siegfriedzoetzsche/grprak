K1 = graphGMLString("""
graph [
    node[id 0 label "0"]
]
""", name="K1")

ZeroInterR = graphGMLString("""
graph[
    node[id 0 label "0"]
    node[id 1 label "0"]
    node[id 2 label "0"]
    node[id 3 label "0"]
    edge[source 0 target 1 label ""]
    edge[source 0 target 2 label ""]
    edge[source 0 target 3 label ""]
]
""", name="ZeroInterR")

OneInterR = graphGMLString("""
graph[
    node[id 0 label "0"]
    node[id 1 label "0"]
    node[id 2 label "0"]
    node[id 3 label "0"]
    edge[source 0 target 1 label ""]
    edge[source 0 target 2 label ""]
    edge[source 0 target 3 label ""]
    edge[source 1 target 3 label ""]
]
""", name="OneInterR")

TwoInterR = graphGMLString("""
graph[
    node[id 0 label "0"]
    node[id 1 label "0"]
    node[id 2 label "0"]
    node[id 3 label "0"]
    edge[source 0 target 1 label ""]
    edge[source 0 target 2 label ""]
    edge[source 0 target 3 label ""]
    edge[source 1 target 3 label ""]
    edge[source 2 target 3 label ""]
]
""", name="TwoInterR")

ThreeInterR = graphGMLString("""
graph[
    node[id 0 label "0"]
    node[id 1 label "0"]
    node[id 2 label "0"]
    node[id 3 label "0"]
    edge[source 0 target 1 label ""]
    edge[source 0 target 2 label ""]
    edge[source 0 target 3 label ""]
    edge[source 1 target 2 label ""]
    edge[source 1 target 3 label ""]
    edge[source 2 target 3 label ""]
]
""", name="ThreeInterR")

###############################
# Non-catalan-solvable graphs #
###############################

K2 = graphGMLString("""
graph[
    node[id 0 label "0"]
    node[id 1 label "0"]
    edge[source 0 target 1 label ""]
]
""", name="K2")

# NThreeEOne = graphGMLString("""
# graph[
#     node[id 0 label "0"]
#     node[id 1 label "0"]
#     node[id 2 label "0"]
#     edge[source 0 target 1 label ""]
# ]
# """, name="NThreeEOne")

N3E2 = graphGMLString("""
graph[
    node[id 0 label "0"]
    node[id 1 label "0"]
    node[id 2 label "0"]
    edge[source 0 target 1 label ""]
    edge[source 2 target 1 label ""]
]
""", name="N3E2")


K3 = graphGMLString("""
graph[
    node[id 0 label "0"]
    node[id 1 label "0"]
    node[id 2 label "0"]
    edge[source 0 target 1 label ""]
    edge[source 2 target 1 label ""]
    edge[source 0 target 2 label ""]
]
""", name="K3")
