#############
# d(v) == 0 #
#############
dZeroExpand = ruleGMLString("""
rule[
    ruleID "dZeroExpand"
    left[
        node[id 0 label "0"]
    ]
    context[
    ]
    right[
        node[id 0 label "A"]
        node[id 1 label "R"]
        node[id 2 label "R"]
        node[id 3 label "R"]
        edge[source 0 target 1 label ""]
        edge[source 0 target 2 label ""]
        edge[source 0 target 3 label ""]
    ]
    constrainAdj[
        id 0 op = count 0
    ]
]
""")

#############
# d(v) == 1 #
#############
dOneExpand = ruleGMLString("""
rule[
    ruleID "dZeroExpand"
    left[
        node[id 0 label "0"]
        edge[source -1 target 0 label ""]
    ]
    context[
        node[id -1 label "0"]
    ]
    right[
        node[id 0 label "A"]
        node[id 1 label "R"]
        node[id 2 label "R"]
        node[id 3 label "R"]

        edge[source -1 target 1 label ""]

        edge[source 0 target 1 label ""]
        edge[source 0 target 2 label ""]
        edge[source 0 target 3 label ""]
    ]
    constrainAdj[
        id 0 op = count 1
    ]
]
""")

#############
# d(v) == 2 #
#############
dTwoExpandOne = ruleGMLString("""
rule[
    ruleID "dTwoExpandOne"
    left[
        node[id 0 label "0"]
        edge[source -1 target 0 label ""]
        edge[source -2 target 0 label ""]
    ]
    context[
        node[id -1 label "0"]
        node[id -2 label "0"]
    ]
    right[
        node[id 0 label "A"]
        node[id 1 label "R"]
        node[id 2 label "R"]
        node[id 3 label "R"]

        edge[source -1 target 1 label ""]
        edge[source -2 target 1 label ""]

        edge[source 0 target 1 label ""]
        edge[source 0 target 2 label ""]
        edge[source 0 target 3 label ""]
    ]
    constrainAdj[
        id 0 op = count 2
    ]
]
""")

##################
# add star edges #
##################

addZeroInterREdges = ruleGMLString("""
rule[
    ruleID "addZeroInterREdges"
    left[
        node[id 0 label "A"]
        node[id 1 label "R"]
        node[id 2 label "R"]
        node[id 3 label "R"]
    ]
    context[
        edge[source 0 target 1 label ""]
        edge[source 0 target 2 label ""]
        edge[source 0 target 3 label ""]
    ]
    right[
        node[id 0 label "0"]
        node[id 1 label "0"]
        node[id 2 label "0"]
        node[id 3 label "0"]
    ]
]
""")

addOneInterREdge = ruleGMLString("""
rule[
    ruleID "addOneInterREdge"
    left[
        node[id 0 label "A"]
        node[id 1 label "R"]
        node[id 2 label "R"]
        node[id 3 label "R"]
    ]
    context[
        edge[source 0 target 1 label ""]
        edge[source 0 target 2 label ""]
        edge[source 0 target 3 label ""]
    ]
    right[
        node[id 0 label "0"]
        node[id 1 label "0"]
        node[id 2 label "0"]
        node[id 3 label "0"]

        edge[source 1 target 2 label ""]
    ]
]
""")

addTwoInterREdges = ruleGMLString("""
rule[
    ruleID "addTwoInterREdges"
    left[
        node[id 0 label "A"]
        node[id 1 label "R"]
        node[id 2 label "R"]
        node[id 3 label "R"]
    ]
    context[
        edge[source 0 target 1 label ""]
        edge[source 0 target 2 label ""]
        edge[source 0 target 3 label ""]
    ]
    right[
        node[id 0 label "0"]
        node[id 1 label "0"]
        node[id 2 label "0"]
        node[id 3 label "0"]

        edge[source 1 target 2 label ""]
        edge[source 1 target 3 label ""]
    ]
]
""")

addThreeInterREdges = ruleGMLString("""
rule[
    ruleID "addThreeInterREdges"
    left[
        node[id 0 label "A"]
        node[id 1 label "R"]
        node[id 2 label "R"]
        node[id 3 label "R"]
    ]
    context[
        edge[source 0 target 1 label ""]
        edge[source 0 target 2 label ""]
        edge[source 0 target 3 label ""]
    ]
    right[
        node[id 0 label "0"]
        node[id 1 label "0"]
        node[id 2 label "0"]
        node[id 3 label "0"]

        edge[source 1 target 2 label ""]
        edge[source 1 target 3 label ""]
        edge[source 2 target 3 label ""]
    ]
]
""")

