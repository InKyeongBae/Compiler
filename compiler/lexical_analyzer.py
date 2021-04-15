import sys
from DFA import *
from collections import deque

MERGED1 = [Literal, Character, Comma, Lbrace, Rbrace, Lparen, Rparen, Relop, Assign, Semicolon, Larray, Rarray]
MERGED2 = [TTrue, TFalse, Class, If, Else, While, Return, TInt, TChar, TBoolean, TString, Identifier]
MERGED3 = [Integer, Operator]
MERGED4 = [Whitespace]

# file I/O
f = open(sys.argv[1], 'r')
inputline = f.readlines()
filename = sys.argv[1]

file_out = open(f"{filename.replace('.java', '')}.out", 'w')



def filewrite(file, string):
    file.write(string)

# error report
error_line = 0
is_error = 0

# 일단 input 내용 그대로 out으로 나오도록
for inputStr in inputline:  ##아래 있는 inputline이랑 왜 다르지?
    #print("###############"
     #     "########################")
    table = []

    inputline = inputStr
    #print(inputline)
    text1 = deque(inputline)
    textState = 0

    # error report
    error_line = error_line + 1
    error_num = 0

    symbols = ["'", '"', ',', '{', '}', '(', ')', '!', ">", "<", '=', ';', '[', ']']
    if is_error == 1 :
        break
    else :
        while len(text1) > 0:
            error = []
            if text1[textState] in symbols:
                for i in range(len(MERGED1)):
                    if i == 0:
                        while textState < len(text1) and MERGED1[i].wscheckIng(text1[textState]) == 1:
                            MERGED1[i].nextState(text1[textState])
                            if MERGED1[i].isIng == 1:
                                textState += 1
                            else:
                                break
                            ##

                    else:
                        while textState < len(text1) and MERGED1[i].checkIng(text1[textState]) == 1:
                            MERGED1[i].nextState(text1[textState])
                            if MERGED1[i].isIng == 1:
                                textState += 1
                            else:
                                break

                    if MERGED1[i].isAccepted():
                        subStr = ""
                        text1copy = text1
                        for _ in range(textState):
                            # print(text1[_])
                            subStr += text1.popleft()
                            error_num = error_num + 1

                        table.append([MERGED1[i].acceptedToken(), subStr])
                        textState = 0
                        MERGED1[i].clear()

                    elif MERGED1[i].isAccepted() == False and i == (len(MERGED1) - 1) :
                        MERGED1[i].clear()
                        while(len(text1) > 0) :
                            text1.pop()
                        print("EMPTY", text1)
                        error_num = error_num + 1
                        file_out.close()
                        file_out = open(f"{filename.replace('.java', '')}.out", 'w')
                        printStr = "ERROR: is not match type, line:" + str(error_line)

                        filewrite(file_out, printStr)
                        filewrite(file_out, '\n')
                        is_error = 1
                        for index in range(error_num):
                            error.append(" ")
                        error[error_num - 1] = "^"
                        filewrite(file_out, inputline.rstrip('\n') + '\n')
                        filewrite(file_out, ''.join(error) + '\n')

                        i += 1
                        textState = 0

                    else:
                        MERGED1[i].clear()

                        i += 1
                        textState = 0


            elif text1[textState] in LETTER or text1[textState] == "_":
                for i in range(len(MERGED2)):
                    while textState < len(text1) and MERGED2[i].checkIng(text1[textState]) == 1:
                        MERGED2[i].nextState(text1[textState])
                        if MERGED2[i].isIng == 1:
                            textState += 1
                        else:
                            break

                    # 마지막 글자면
                    if textState >= len(text1):
                        if MERGED2[i].isAccepted():
                            subStr = ""
                            for _ in range(textState):
                                subStr += text1.popleft()
                                error_num = error_num + 1
                            if i == len(MERGED2) - 1:
                                table.append([MERGED2[i].acceptedToken(), subStr])
                            elif i >= 0 and i < 2:
                                table.append(['BOOLEAN', subStr])
                            elif i >= 2 and i < 7:
                                table.append(['KEYWORD', subStr])
                            else:
                                table.append(['TYPE', subStr])
                            textState = 0
                            MERGED2[i].clear()
                        else:
                            MERGED2[i].clear()
                            i += 1
                            textState = 0
                    else:
                        if MERGED2[i].isAccepted() and (
                                text1[textState] == ' ' or text1[textState] != '_' or text1[textState] not in LETTER or
                                text1[textState] not in DIGIT) and i != len(MERGED2) - 1:
                            subStr = ""
                            for _ in range(textState):
                                subStr += text1.popleft()
                                error_num = error_num + 1
                            if i >= 0 and i < 2:
                                table.append(['BOOLEAN', subStr])
                            elif i >= 2 and i < 7:
                                table.append(['KEYWORD', subStr])
                            else:
                                table.append(['TYPE', subStr])
                            textState = 0
                            MERGED2[i].clear()

                        elif MERGED2[i].isAccepted() and i == len(MERGED2) - 1:
                            subStr = ""
                            for _ in range(textState):
                                subStr += text1.popleft()
                                error_num = error_num + 1
                            table.append([MERGED2[i].acceptedToken(), subStr])
                            textState = 0
                            MERGED2[i].clear()
                        else:
                            MERGED2[i].clear()
                            i += 1
                            textState = 0


            # 3) 숫자가 들어올 때
            elif text1[textState] in OPERATOR or text1[0] in DIGIT:
                idx = 0
                if table and table[-1][0] == "IDENTIFIER" and text1[textState] == "-":  # MINUS PROBLEM
                    idx = 1
                if table and table[-1][0] == "OPERATOR" and text1[textState] == "-":  # MINUS PROBLEM
                    idx = 0
                for i in range(idx, len(MERGED3)):
                    while textState < len(text1) and MERGED3[i].checkIng(text1[textState]) == 1:
                        MERGED3[i].nextState(text1[textState])
                        if MERGED3[i].isIng == 1:
                            textState += 1
                        else:  # accaept이 안됨
                            break

                    # MERGED를 다 돈게 아닌 상태에서 넘어감.
                    if MERGED3[i].isAccepted():

                        subStr = ""
                        text1copy = text1
                        # if textState == 0: #MINUS PROBLEM -1 #for operator "-" ex) 1-1
                        #    subStr += text1.popleft()

                        for _ in range(textState):
                            subStr += text1.popleft()  # 1
                            error_num = error_num + 1

                        # print(text1)
                        # if text1[0] == "-": #MINUS PROBLEM -2 #
                        #    if table[-1][0] == "IDENTIFIER":
                        #        table.append(["OPERATOR", subStr[0]])
                        #        table.append([MERGED3[i].acceptedToken(), subStr[1:]])
                        # else:

                        table.append([MERGED3[i].acceptedToken(), subStr])
                        textState = 0
                        MERGED3[i].clear()

                        if MERGED3[i].tokenName == "INTEGER":
                            i = 1
                        else:
                            i = 0

                    else:
                        MERGED3[i].clear()
                        i += 1
                        textState = 0


            elif text1[textState] in WHITESPACE:
                for i in range(len(MERGED4)):
                    while textState < len(text1) and MERGED4[i].wscheckIng(text1[textState]) == 1:
                        MERGED4[i].nextState(text1[textState])
                        if MERGED4[i].isIng == 1:
                            textState += 1
                        else:
                            break

                    if MERGED4[i].isAccepted():
                        subStr = ""
                        text1copy = text1
                        for _ in range(textState):
                            subStr += text1.popleft()
                            error_num = error_num + 1
                        # table.append([MERGED4[i].acceptedToken(), subStr])
                        textState = 0
                        MERGED4[i].clear()
                    else:
                        MERGED4[i].clear()
                        i += 1
                        textState = 0

            else:
                subStr = ""
                subStr += text1.popleft()
                error_num = error_num + 1
                table.append(["Not Match", subStr])  # 없는 글자 처리해줌.

                file_out.close()
                file_out = open(f"{filename.replace('.java', '')}.out", 'w')
                printStr = "ERROR: There is a letter " + '"' + subStr + '"' + " is not acceptable. line:" + str(error_line)

                filewrite(file_out, printStr)
                filewrite(file_out, '\n')
                is_error = 1

                for index in range(error_num):
                    error.append(" ")
                error[error_num - 1] = "^"
                filewrite(file_out, inputline.rstrip('\n')+'\n')
                filewrite(file_out,  ''.join(error) + '\n')
                textState = 0


        if is_error == 0 :
            for i in range(len(table)):
                #print("table:", table[i])
                filewrite(file_out, str(table[i]))
                filewrite(file_out, "\n")

f.close()



