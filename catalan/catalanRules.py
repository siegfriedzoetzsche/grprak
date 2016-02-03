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
    constrainAdj [
        id 0
        op = count 3
    ]
]
""")

helper = ruleGMLString("""
rule[
    ruleID "mark"
    left[
        edge[source 0 target 1 label ""]
    ]
    context[
        node[id 0 label "A"]
        node[id 1 label "0"]
    ]
    right[
        edge[source 0 target 1 label "FAIL"]
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
        edge[source 1 target 2 label ""]
    ]
    context[
        node[id 0 label "A"]
        node[id 1 label "R"]
        node[id 2 label "0"]
        edge[source 0 target 1 label ""]
        edge[source 0 target 2 label ""]
    ]
    right[
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
        edge[source 0 target 2 label ""]
        edge[source 0 target 3 label ""]
    ]
    right[
        edge[source 1 target 0 label ""]
    ]
    constrainAdj[
        id 1
        op = count 0 nodeLabels [label "A"]
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

hasFailed = ruleGMLString("""
rule[
    ruleID "hasFailed"
    left[
        node[id 0 label "FAIL"]
    ]
    context[
    ]
    right[
        node[id 0 label "SUPERFAIL"]
    ]
]
""")

test = ruleGMLString("""
rule[
    ruleID "test"
    left[
        node[id 0 label "0"]
    ]
    context[
    ]
    right[
        node[id 0 label "passed!"]
    ]
]
""")

finished = ruleGMLString("""
rule[
    ruleID "finished"
    left[
    ]
    context[
        node[id 0 label "0"]
    ]
    right[
    ]
    constrainAdj [
        id 0
        op = count 0
    ]
]
""")
