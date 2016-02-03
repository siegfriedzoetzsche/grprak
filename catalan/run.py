include("catalanRules.py")
include("catalanLevels.py")
postSection("Input Graphs")

#SIMPLE_BLOSSOM.print()
# LANDSCAPE.print()
# for a in inputGraphs:
#         a.print()

# postSection("Input Rules")
# for a in inputRules:
#  	a.print()

# LEVEL = FIRST_LEVEL
LEVEL = SIMPLE_BLOSSOM

strat = (
        addUniverse(LEVEL)
        >> addSubset(LEVEL)
        >> mark
        # >> revive(markForFail)
        # >> #repeat[1](
        #         revive(
        #                 reattachExternal
        #         )
        #)
        # >> removeInterR
        # >> reattachExternal
        # >> removeAttached
        # >> removeR
        # >> unmark
)

dg = dgRuleComp(inputGraphs, strat)
dg.calc()
dg.print()

