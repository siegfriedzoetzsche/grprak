mark = ruleGMLString("""
rule[
    ruleID "mark"
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
    ruleID "markForFail"
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


removeInterR = ruleGMLString("""
rule[
    ruleID "removeInterR"
    left[
        node[id 1 label "0"]
    ]
    context[
        node[id 0 label "A"]
    ]
    right[
        node[id 1 label "FAIL"]
    ]
]
""")

reattachExternal = ruleGMLString("""
rule[
    ruleID "reattachExternal"
    left[
        edge[source 1 target 2 label ""]
    ]
    context[
        node[id 0 label "A"]
        node[id 1 label "0"]
        node[id 2 label "R"]
        node[id 3 label "R"]
    ]
    right[
        edge[source 1 target 0 label ""]
    ]
]
""")

removeAttached = ruleGMLString("""
rule[
    ruleID "removeAttached"
    left[
        edge[source 1 target 2 label ""]
    ]
    context[
        node[id 0 label "A"]
        node[id 1 label "R"]
        node[id 2 label "R"]
        edge[source 0 target 1 label ""]
        edge[source 0 target 2 label ""]
    ]
    right[
    ]
]
""")

removeR = ruleGMLString("""
rule[
    ruleID "removeR"
    left[
        node[id 1 label "R"]
        node[id 2 label "R"]
        node[id 3 label "R"]
        edge[source 0 target 1 label ""]
        edge[source 0 target 2 label ""]
        edge[source 0 target 3 label ""]
    ]
    context[
        node[id 0 label "A"]
    ]
    right[
    ]
]
""")

unmark = ruleGMLString("""
rule[
    ruleID "unmark"
    left[
        node[id 0 label "A"]
    ]
    context[
    ]
    right[
        node[id 0 label "0"]
    ]
]
""")

