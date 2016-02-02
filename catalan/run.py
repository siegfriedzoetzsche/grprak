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

strat0 = (
        addUniverse(SIMPLE_BLOSSOM)
        # >> 
        #addSubset(SIMPLE_BLOSSOM)
        # >> repeat[1] (
        >> mark
        # )        
)

strat = (
        #addUniverse(SIMPLE_BLOSSOM)
        #>> 
        addSubset(SIMPLE_BLOSSOM)
        >> mark
        >> revive(
                markForFail
        )
        >> unmark
)

dg = dgRuleComp(inputGraphs, strat0)
dg.calc()
dg.print()

