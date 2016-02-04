include("catalanRules.py")
include("catalanLevels.py")
# postSection("Input Graphs")
# for a in inputGraphs:
#         a.print()

# postSection("Input Rules")
# for a in inputRules:
#  	a.print()

#LEVEL = FIRST_LEVEL
#LEVEL = SIMPLE_BLOSSOM
LEVEL = HONEY_SUCKLE
#LEVEL = DRAGON
#LEVEL = TRIAD
#LEVEL = TREE
#LEVEL = MASK
#LEVEL = FLOTSAM
#LEVEL = SHALLOW_GRAVE
#LEVEL = SUBWAY
postSection("Catalan level to solve")
LEVEL.print()

strat1 = (
    addUniverse(LEVEL)
    >> addSubset(LEVEL)
    >> repeat(
        mark
        >> repeat(revive(reattachExternal))
        >> repeat(revive(removeAttached))
        >> repeat(revive(removeInterR))
        >> removeR
        >> unmark
    )
)

strat = strat1

dg = dgRuleComp(inputGraphs, strat)
dg.calc()

dgPrinter = DGPrinter()
dgPrinter.withGraphImages = False # be careful, the derivation graphs can become quite large
dg.print(dgPrinter)

flowPrinter = DGFlowPrinter()
flowPrinter.printUnfiltered = False
flow = dgFlow(dg)
flow.objectiveFunction = DGFlowLinExp() # important, otherwise the default function will min. #edgesUsed which may take a long time
flow.addSource(LEVEL)
flow.addSink(SUCCESS)
flow.addConstraint(inFlow(LEVEL) == 1)
flow.calc()
#flow.solutions.print(flowPrinter)

if SUCCESS in dg.vertices:
    flow.solutions.print(flowPrinter)
    print("SUCCESS")
else:
    print("no solution found")


