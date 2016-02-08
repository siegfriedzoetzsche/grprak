tautomerization = ruleGMLString("""
rule[
	ruleID "tautomerization"
	left[
		edge[source 3 target 5 label "="]
		edge[source 2 target 3  label "-"]
		edge[source 2 target 6 label "-"]
	]
	context[
		# unmodified part of Aldehyd / Keton 1
		node[id 1 label "*"]
		node[id 2 label "C"]
		node[id 3 label "C"]
		node[id 4 label "*"]	
		node[id 5 label "O"]
		node[id 6 label "H"]
		node[id 7 label "H"]
		edge[source 1 target 2 label "-"]
		edge[source 3 target 4 label "-"]
		edge[source 2 target 7 label "-"]
	]
	right[
		edge[source 2 target 3 label "="]		
		edge[source 3 target 5 label "-"]		
		edge[source 5 target 6 label "-"]
	]
]
""")
