include("catalanRules.py")
include("catalanLevels.py")
# postSection("Input Graphs")
# for a in inputGraphs:
#         a.print()

postSection("Input Rules")
for a in inputRules:
 	a.print()

# LEVEL = FIRST_LEVEL
# LEVEL = SIMPLE_BLOSSOM
# LEVEL = HONEY_SUCKLE
LEVEL = DRAGON
strat1 = (
    #addUniverse(LEVEL)
    #>> 
    addSubset(LEVEL)
    >> repeat(
        mark
        >> repeat(reattachExternal)
        >> repeat(removeAttached)
        >> repeat(removeInterR)
        >> removeR
        >> unmark
    )
)

test = (
    addUniverse(LEVEL)
    >> addSubset(LEVEL)
    >> mark   
    >> rightPredicate[
        lambda d: all(a.vLabelCount("FAIL") == 0 for a in d.right)
    ](
        markForFail
        # repeat(removeAttached)
        # >> repeat(reattachExternal)
        # >> repeat(removeInterR)
    )
    >> unmark
    # >> markForFail
    # >> leftPredicate[
    #     lambda d: all(a.vLabelCount("FAIL") == 0 for a in d.left)
    # ](
    #     test
    #     # repeat(removeAttached)
    #     # >> repeat(reattachExternal)
    #     # >> repeat(removeInterR)
    # )
    # >> removeR
    # >> unmark
)

strat = strat1

dg = dgRuleComp(inputGraphs, strat)
dg.calc()
dg.print()

