include("catalanRules.py")
include("catalanLevels.py")
postSection("Input Graphs")
for a in inputGraphs:
	a.print()
postSection("Input Rules")
for a in inputRules:
	a.print()

# strat = (
# 	addUniverse(formaldehyde)
# 	>> addSubset(glycolaldehyde)
# 	# iterate the rule application 4 times
# 	>> repeat[4](
# 		inputRules
# 	)
# )
# dg = dgRuleComp(inputGraphs, strat)
# dg.calc()
# dg.print()
