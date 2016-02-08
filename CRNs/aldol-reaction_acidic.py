aldolreaction_acidic = ruleGMLString("""
rule[
	ruleID "aldolreaction_acidic" 
	left[
		edge[source 3 target 5 label "="]
		edge[source 7 target 14 label "-"]
	]
	context[
		# unmodified part of Aldehyd / Keton 1
		node[id 1 label "*"]
		node[id 2 label "C"]
		node[id 3 label "C"]
		node[id 4 label "*"]	
		node[id 5 label "O"]
		edge[source 1 target 2 label "-"]
		edge[source 2 target 3 label "-"]
		edge[source 3 target 4 label "-"]
		node[id 11 label "H"]
		node[id 12 label "H"]
		edge[source 2 target 11 label "-"]
		edge[source 2 target 12 label "-"]

		# unmodified part of Aldehyd / Keton 2
		node[id 6 label "*"]
		node[id 7 label "C"]
		node[id 8 label "C"]
		node[id 9 label "*"]	
		node[id 10 label "O"]
		edge[source 6 target 7 label "-"]
		edge[source 7 target 8 label "-"]
		edge[source 8 target 9 label "-"]
		edge[source 8 target 10 label "="]
		node[id 13 label "H"]
		node[id 14 label "H"]
		edge[source 7 target 13 label "-"]
	]
	right[
		edge[source 3 target 7 label "-"]		
		edge[source 3 target 5 label "-"]		
		edge[source 5 target 14 label "-"]		
	]
]
""")
