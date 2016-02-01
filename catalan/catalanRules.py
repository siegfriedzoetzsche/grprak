mark = ruleGMLString("""
rule[
    ruleID "Mark a star"
    left[
        node[id 0 label "0"]
        node[id 1 label "0"]
        node[id 2 label "0"]
        node[id 3 label "0"]       
    ]
    context[
        edge[source 0 target 1 label ""]
        edge[source 0 target 2 label ""]
        edge[source 0 target 3 label ""]
    ]
    right[
        node[id 0 label "A"]
        node[id 1 label "R"]
        node[id 2 label "R"]
        node[id 3 label "R"]               
    ]
]
""")

markForFail = ruleGMLString("""
rule[
    ruleID ""
    left[
        node[id 1 label "0"]
    ]
    context[
        node[id 0 label "A"]
        edge[source 0 target 1 label ""]
    ]
    right[
        node[id 1 label "FAIL"]
    ]
]
""")


 = ruleGMLString("""
rule[
    ruleID ""
    left[
        node[id 1 label "0"]
    ]
    context[
        node[id 0 label "A"]
        edge[source 0 target 1 label ""]
    ]
    right[
        node[id 1 label "FAIL"]
    ]
]
""")

