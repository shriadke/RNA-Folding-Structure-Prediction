# RNA-Folding-Structure-Prediction-
Dynamic Programming solution for RNA structure prediction sub-problem

This is the dynamic programming project for structure prediction problem using Python3.

# Prerequisites :

1) Python3
2) package os
3) package argparse

# File Structure :
Under this directory, structPred.py is the script which needs to be run. It takes one argument i.e. input file name which MUST be in the same folder as of the script. Running this will generate output.txt file which will contain the output in the given format.

We can use the default input.txt as input or can pass any other file which contains sequence on each line.

# Running the program :

If using custom text input file, pass it as an argument:
	python3 structPred.py --inputFile="custInput.txt"
Else
	python3 structPred.py
