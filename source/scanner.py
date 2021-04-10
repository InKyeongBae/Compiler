import sys
from sub_code import sub_code
#file I/O
f = open(sys.argv[1],'r')
input = f.readlines()
filename = sys.argv[1]
print(input)
for i in range(len(input)) :
    checking = FiniteAutomata(input[i])
    while 1 :
        if checking.next_string == '\n' :
            break
        else :
            # merged
            checking.dfa_identifier(checking.next_string)
            checking.dfa_blank(checking.next_string)
            checking.dfa_semicolon(checking.next_string)
            checking.dfa_comma(checking.next_string)



f.close()


#2) 문자가 들어올 때 해결 X
    elif text1[textState] in LETTER :
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        for i in range(len(MERGED02)):
            while textState < len(text1) and MERGED02[i].checkIng(text1[textState]) == 1:
                MERGED02[i].nextState(text1[textState])
                print("isIng :", MERGED02[i].isIng)
                if MERGED02[i].isIng == 1:
                    textState += 1
                else:
                    break
                # print("!!!!!!", textState)

            if MERGED02[i].isAccepted():
                subStr = ""
                for _ in range(textState):
                    subStr += text1.popleft()
                table.append([MERGED02[i].acceptedToken(), subStr])
                textState = 0
                MERGED02[i].clear()
            else:
                MERGED02[i].clear()
                i += 1
                textState = 0
