addThreeNodes = ruleGMLString("""
rule[
    ruleID "addThreeNodes"
    left[
    ]
    context[
        node[id 0 label "0"]
    ]
    right[
        node[id 1 label "0"]
        node[id 2 label "0"]
        node[id 3 label "0"]
        edge[source 0 target 1 label""]
        edge[source 0 target 2 label""]
        edge[source 0 target 3 label""]
    ]
]
""")

addEdge = ruleGMLString("""
rule[
    ruleID "addEdge"
    left[
    ]
    context[
        node[id 0 label "0"]
        node[id 1 label "0"]
        node[id 2 label "0"]
        edge[source 0 target 1 label""]
        edge[source 0 target 2 label""]        
    ]
    right[
        edge[source 1 target 2 label""]
    ]
    #constrainNoEdge[source 1 target 2]
]
""")
