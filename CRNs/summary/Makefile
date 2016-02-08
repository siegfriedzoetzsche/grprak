SHELL=/bin/bash
summary/all.tex: gen
	echo -n '\summaryGraph' >> summary/all.tex
	echo '{\texttt{Test}}{out/000_g_0.10100000}{\texttt{out/000\_g\_0.10100000}}{out/000_g_0.11110100}{\texttt{out/000\_g\_0.11110100}}' >> summary/all.tex
summary.pdf: summary/all.tex
	/homes/brauerei2/jlandersen/shared/bin/../bin/mod_post --mode compileSummary
include summary/MakefileImpl
include summary/MakefileDep
include summary/MakefileAllTarget
include summary/MakefileClean
