import sys
from FiniteAutomata import FiniteAutomata
#file I/O
f = open(sys.argv[1],'r')
input = f.readlines()
filename = sys.argv[1]
print(input)
# for i in range(len(input)) :
#     checking = FiniteAutomata(input[i])
#     while 1 :
#         if checking.next_string == '\n' :
#             break
#         else :
#             # merged
#             checking.dfa_identifier(checking.next_string)
#             checking.dfa_blank(checking.next_string)
#             checking.dfa_semicolon(checking.next_string)
#             checking.dfa_comma(checking.next_string)



f.close()