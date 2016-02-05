include("catalanBuildRulesSimon.py")
postSection("Input Rules")
for a in inputRules:
        a.print()

# dg = dgRuleComp(inputGraphs, strat)
# dg.calc()

# dgPrinter = DGPrinter()
# dgPrinter.withGraphImages = True # be careful, the derivation graphs can become quite large
# dg.print(dgPrinter)
