import glob
import os

# Get a list of all C files in the directory
file_list = glob.glob('*.c')

# Open a TeX file
texfile = open('programs.tex', 'w')
texfile.write('''\documentclass[a4paper,11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{listings}

\lstset{breaklines=true, language=c++, tabsize=2}

\\begin{document}\n''')

# Add each program using lstinputlisting
for c_file in file_list:
	texfile.write('    \\thispagestyle{empty}\n')
	texfile.write('    \\flushleft \\textbf{Program}\n')
	texfile.write('    \lstinputlisting{%s}\n' % c_file)
	texfile.write('    \\newpage\n')
texfile.write('\end{document}')
texfile.close()

# Compile TeX file and generate PDF :)
os.system('latex programs.tex')
os.system('dvipdf programs.dvi')


