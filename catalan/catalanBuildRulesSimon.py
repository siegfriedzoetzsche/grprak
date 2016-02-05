expandNode = ruleGMLString("""
rule[
        ruleID "expandNode"
        left[
                node[id 0 label "0"]
        ]
        context[]
        right[
                node[id 0 label "A"]
                node[id 1 label "R"]
                node[id 2 label "R"]
                node[id 3 label "R"]
                edge[source 0 target 1 label ""]
                edge[source 0 target 2 label ""]
                edge[source 0 target 3 label ""]
        ]
]
""")

move0_1R = ruleGMLString("""
rule[
       ruleID "move0_1R"
       left[
               edge[source 0 target -1 label ""]
       ]
       context[
               node[id 0 label "A"]
               node[id 1 label "R"]
               node[id 2 label "R"]
               node[id 3 label "R"]
               node[id -1 label "0"]
               edge[source 0 target 1 label ""]
               edge[source 0 target 2 label ""]
               edge[source 0 target 3 label ""]
       ]
       right[
               edge[source -1 target 1 label ""]
       ]
]
""")

move0_2R = ruleGMLString("""
rule[
        ruleID "move0_2R"
        left[
                edge[source 0 target -1 label ""]
        ]
        context[
                node[id 0 label "A"]
                node[id 1 label "R"]
                node[id 2 label "R"]
                node[id 3 label "R"]
                node[id -1 label "0"]
                edge[source 0 target 1 label ""]
                edge[source 0 target 2 label ""]
                edge[source 0 target 3 label ""]
        ]
        right[
                edge[source -1 target 1 label ""]
                edge[source -1 target 2 label ""]
        ]
]
""")

move0_3R = ruleGMLString("""
rule[
       ruleID "move0_3R"
       left[
               edge[source 0 target -1 label ""]
       ]
       context[
               node[id 0 label "A"]
               node[id 1 label "R"]
               node[id 2 label "R"]
               node[id 3 label "R"]
               node[id -1 label "0"]
               edge[source 0 target 1 label ""]
               edge[source 0 target 2 label ""]
               edge[source 0 target 3 label ""]
       ]
       right[
               edge[source -1 target 1 label ""]
               edge[source -1 target 2 label ""]
               edge[source -1 target 3 label ""]
       ]
]
""")

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



# unmark_A = ruleGMLString("""
# rule[
#     ruleID "unmark_A"
#     left[
#         node[id 0 label "A"]
#     ]
#     context[
#     ]
#     right[
#         node[id 0 label "0"]
#     ]
# ]
# """)

# unmark_R = ruleGMLString("""
# rule[
#     ruleID "unmark_R"
#     left[
#         node[id 0 label "R"]
#     ]
#     context[
#     ]
#     right[
#         node[id 0 label "0"]
#     ]
# ]
# """)
