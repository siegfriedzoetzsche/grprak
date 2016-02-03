include("catalanRules.py")
include("catalanLevels.py")
# postSection("Input Graphs")
# for a in inputGraphs:
#         a.print()

# postSection("Input Rules")
# for a in inputRules:
#  	a.print()

#LEVEL = FIRST_LEVEL
LEVEL = SIMPLE_BLOSSOM
#LEVEL = HONEY_SUCKLE
#LEVEL = DRAGON
#LEVEL = TREE
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
#dg.print()
dgPrinter = DGPrinter()
dgPrinter.withGraphImages =False # be careful, the derivation graphs can become quite large

dg.print(dgPrinter)

if SUCCESS in dg.vertices:
    print("SUCCESS")
else:
    print("no solution found")


