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
for inputStr in inputline:
    table = []
    inputline = inputStr
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
            if text1[textState] in symbols :
                for i in range(len(MERGED1)):
                    if i == 0 or i == 1:
                        while textState < len(text1) and MERGED1[i].wscheckIng(text1[textState]) == 1:
                            MERGED1[i].nextState(text1[textState])
                            if MERGED1[i].isIng == 1:
                                textState += 1
                            else:
                                break

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
                            subStr += text1.popleft()
                            error_num = error_num + 1

                        table.append([MERGED1[i].acceptedToken(), subStr])
                        textState = 0
                        MERGED1[i].clear()
                        break

                    elif MERGED1[i].isAccepted() == False and i == (len(MERGED1) - 1):
                        MERGED1[i].clear()
                        while(len(text1) > 0) :
                            text1.pop()
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
                            break

                        elif MERGED2[i].isAccepted() == False and i == (len(MERGED2) - 1):
                            MERGED2[i].clear()
                            while (len(text1) > 0):
                                text1.pop()
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
                            MERGED2[i].clear()
                            i += 1
                            textState = 0

                    # 마지막 글자가 아니면
                    else:
                        if MERGED2[i].isAccepted() and (text1[textState] != '_' and text1[textState] not in LETTER and text1[textState] not in DIGIT) and i != len(MERGED2) - 1:
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
                            break

                        elif MERGED2[i].isAccepted() and i == len(MERGED2) - 1:
                            subStr = ""
                            for _ in range(textState):
                                subStr += text1.popleft()
                                error_num = error_num + 1

                            table.append([MERGED2[i].acceptedToken(), subStr])
                            textState = 0
                            MERGED2[i].clear()
                            break

                        elif MERGED2[i].isAccepted() == False and i == (len(MERGED2) - 1):
                            MERGED2[i].clear()
                            while (len(text1) > 0):
                                text1.pop()
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
                            MERGED2[i].clear()
                            i += 1
                            textState = 0


            elif text1[textState] in OPERATOR or text1[0] in DIGIT:
                idx = 0
                if table and (table[-1][0] == "IDENTIFIER" or table[-1][0] == "INTEGER" ) and text1[textState] == "-":  # MINUS PROBLEM
                    idx = 1

                for i in range(idx, len(MERGED3)):
                    while textState < len(text1) and MERGED3[i].checkIng(text1[textState]) == 1:
                        MERGED3[i].nextState(text1[textState])
                        if MERGED3[i].isIng == 1:
                            textState += 1
                        else:
                            break

                    if MERGED3[i].isAccepted():
                        subStr = ""
                        text1copy = text1

                        for _ in range(textState):
                            subStr += text1.popleft()  # 1
                            error_num = error_num + 1

                        table.append([MERGED3[i].acceptedToken(), subStr])
                        textState = 0
                        MERGED3[i].clear()

                        if MERGED3[i].tokenName == "INTEGER":
                            i = 1
                        else:
                            i = 0
                        break

                    elif MERGED3[i].isAccepted() == False and i == (len(MERGED3) - 1):
                        MERGED3[i].clear()
                        while (len(text1) > 0):
                            text1.pop()
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
                        textState = 0
                        MERGED4[i].clear()
                        break

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
                filewrite(file_out, str(table[i]))
                filewrite(file_out, "\n")

f.close()



