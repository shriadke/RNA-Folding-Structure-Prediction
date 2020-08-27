# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:44:47 2019

@author: shrin
"""

def is_letter_pair_legal(xi,yi):
    if ((xi == 'A' and yi == 'U') or 
        (xi == 'U' and yi == 'A') or 
        (xi == 'G' and yi == 'C') or 
        (xi == 'C' and yi == 'G')):
        return True
    return False

def StructurePrediction(letters):
    n = len(letters)
    M = [[0 for _ in range(n)] for _ in range(n)]
    S = [[0 for _ in range(n)] for _ in range(n)]
    for l in range(1, n+1):
        for i in range(0, n-l+1):
            j = i + l - 1
            M[i][j] = 0
            q = 0
            if is_letter_pair_legal(letters[i], letters[j]):
                q = M[i+1][j-1] + 1
            if q >= M[i][j] and q!=0:
                M[i][j] = q
                S[i][j] = j
            for k in range(i, j):
                sum_k = M[i][k] + M[k+1][j]
                if sum_k > M[i][j]:
                    M[i][j] = sum_k
                    S[i][j] = k
            if M[i][j] == 0:
                S[i][j] = -1
    return M, S

def printParenthesis(i,j,S,string):
    if i>j:
        return
    if (S[i][j] == -1):
        string[i] = '.'
        printParenthesis(i+1, j, S, string)
    elif S[i][j] == j:
        string[i] = '{'
        string[j] = '}'
        printParenthesis(i+1, j-1, S, string)
    elif S[i][j] == i:
        string[i] = '.'
        printParenthesis(i+1, j, S, string)
    else:
        k = S[i][j]
        string[i] = '{'
        string[k] = '}'
        printParenthesis(i+1, k-1, S, string)
        printParenthesis(k+1, j, S, string)
    return

if __name__ == "__main__":
    import argparse
    import os
    ROOT_DIR = os.getcwd()
    parser = argparse.ArgumentParser(description='Find Max Structure Matching')
    parser.add_argument('--inputFile', required=False,
                        default="input.txt",
                        metavar="path/to/input",
                        help='Directory of the input file (default=/input.txt)')
    args = parser.parse_args()
    INPUT_PATH = os.path.join(ROOT_DIR, args.inputFile)
    inputFile = open(INPUT_PATH, "r")
    outputFile = open("output.txt","w+")
    inputlines = inputFile.readlines()
    for line in inputlines:
        outputFile.write("***************************************************************\n")
        letters = list(line.rstrip())
        M, S = StructurePrediction(letters)
        # Uncomment to print table M and S to console
# =============================================================================
#             for a in M:
#                 for b in a:
#                     print(b, end=' ')
#                 print("")
#             print("S")
#             for a in S:
#                 for b in a:
#                     print(b, end=' ')
#                 print("")
# =============================================================================
        string = ['' for _ in range(len(letters))]
        printParenthesis(0,len(letters)-1, S,string)
        outputFile.write("".join(letters)+'\n')
        outputFile.write("".join(string)+'\n')
        strCount = "Max count of pairs: " + str(M[0][len(letters)-1]) + '\n'
        outputFile.write(strCount)
    inputFile.close()
    outputFile.close()
    