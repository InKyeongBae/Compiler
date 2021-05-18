import sys

f = open(sys.argv[1], 'r')
inputline = f.readlines()
filename = sys.argv[1]

file_out = open(f"{filename.replace('.out', '')}.txt", 'w')


for inputStr in inputline:
    print(inputStr)