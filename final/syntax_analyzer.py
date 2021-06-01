import sys
from SLR import *
from rules import *


# l = "['IDENTIFIER', 'numOfelements']"
# list_str = l.split("'")
# nowList = []
# nowList.append(list_str[1])
# nowList.append(list_str[3])
# print(nowList)
# print(len(nowList))
# print(type(nowList))


# file I/O
f = open(sys.argv[1], 'r')
inputline = f.readlines()
filename = sys.argv[1]

file_out = open(f"{filename.replace('.out', '')}_final.out", 'w')

def filewrite(file, string):
    file.write(string)

# error report
# error_line = 0
# is_error = 0

for inputStr in inputline:
    if inputStr[0] == "E" :
        filewrite(file_out, "ERROR : input file(Lexical Analysis Result) error")
        break
    if inputStr[0] == "[" :
        list_str = inputStr.split("'")
        nowList = []
        nowList.append(list_str[1])
        nowList.append(list_str[3])

    