include("catalanBuildRules.py")
include("catalanLevels.py")
# postSection("Input Graphs")
# for a in inputGraphs:
#         a.print()

# postSection("Input Rules")
# for a in inputRules:
#  	a.print()

LEVEL = SUCCESS

strat1 = (
    # add just one node with label "0"
    addUniverse(LEVEL)
    >> addSubset(LEVEL)
    # expand a node with vertex degree 0
    >> dZeroExpand
    # add 0, 1, 2 or 3 edges beween the arms of the star
    >> {
        addZeroInterREdges,
        addOneInterREdge,
        addTwoInterREdges,
        addThreeInterREdges,
    }
    # expand further
    >> {dOneExpand, dTwoExpandOne}
    >> {
        addZeroInterREdges,
        addOneInterREdge,
        addTwoInterREdges,
        addThreeInterREdges,
    }
)

strat = strat1

dg = dgRuleComp(inputGraphs, strat)
dg.calc()

dgPrinter = DGPrinter()
dgPrinter.withGraphImages = True # False # be careful, the derivation graphs can become quite large
dg.print(dgPrinter)

# flowPrinter = DGFlowPrinter()
# flowPrinter.printUnfiltered = False
# flow = dgFlow(dg)
# flow.objectiveFunction = DGFlowLinExp() # important, otherwise the default function will min. #edgesUsed which may take a long time
# flow.addSource(LEVEL)
# flow.addSink(SUCCESS)
# flow.addConstraint(inFlow(LEVEL) == 1)
# flow.calc()
# #flow.solutions.print(flowPrinter)

# if SUCCESS in dg.vertices:
#     flow.solutions.print(flowPrinter)
#     print("SUCCESS")
# else:
#     print("no solution found")


