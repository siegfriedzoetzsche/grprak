include("catalanBuildRulesSimon.py")
include("oirSeed.py")
postSection("Input Graphs")
for a in inputGraphs:
        a.print()

LEVEL = OneInterR

strat = (
        addUniverse(LEVEL)
        >> addSubset(LEVEL)
	# expand a few times
        >> repeat[1](
                # expand a node with vertex degree 0
                expandNode
		# move edges of the expanded node to a number of neighbours 
                >> repeat(revive({move0_1R, move0_2R, move0_3R}))
		# add edges between the newly created nodes (that will be consumed on contraction)
                >> {addZeroInterREdges, addOneInterREdge, addTwoInterREdges, addThreeInterREdges}
     )
)

dg = dgRuleComp(inputGraphs, strat)
dg.calc()

dgPrinter = DGPrinter()
dgPrinter.withGraphImages = True # be careful, the derivation graphs can become quite large
dg.print(dgPrinter)
