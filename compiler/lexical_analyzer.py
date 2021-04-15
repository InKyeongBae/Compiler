import sys
from DFA import *
from collections import deque

MERGED1 = [Literal, Character, Comma, Lbrace, Rbrace, Lparen, Rparen, Relop, Assign, Semicolon, Larray, Rarray]
MERGED2 = [TTrue, TFalse, Class, If, Else, While, Return, TInt, TChar, TBoolean, TString, Identifier]
MERGED3 = [Integer, Operator]
MERGED4 = [Relop, Assign]
MERGED5 = [Whitespace]

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
    # error report
    error_line = 0
    is_error = 0
    table = []
    inputline =
    text1 = deque(inputline)
    textState = 0
    table = []
    inputline =
    text1 = deque(inputline)
    textState = 0

    # error report
    error_line = error_line + 1inputStr
    #print(inputline)
    error_num = 0

    symbols = ["'", '"', ',', '{', '}', '(', ')', '!', ">", "<", '=', ';', '[', ']']
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
                else:
                    while textState < len(text1) and MERGED1[i].checkIng(text1[textState]) == 1:
                        MERGED1[i].nextState(text1[textState])
                        if MERGED1[i].isIng == 1:
                            textState += 1
                            if MERGED1[i].tokenName == "CHARACTER" and textState < len(text1) and text1[textState] == BLANK[0]:
                                MERGED1[i].nextState(text1[textState])
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
                else:
                    # if text1:
                    #     if MERGED1[i].tokenName == "CHARACTER" and text1[0] == "'":
                    #         text1.popleft()
                    #         error_num = error_num + 1
                    #         table.append(["Not Matched", "'"])
                    #         # 만약 허용되는 글자인데 없으면, 혹은 ", ' 따옴표들이면 짝 쓰시오 오류 메시
                    #         file_out.close()
                    #         file_out = open(f"{filename.replace('.java', '')}.out", 'w')
                    #         printStr = "ERROR: is not CHRACTER type, line:" + str(error_line)
                    #
                    #         filewrite(file_out, printStr)
                    #         filewrite(file_out, '\n')
                    #         is_error = 1
                    #
                    #
                    #         for index in range(error_num):
                    #             error.append(" ")
                    #         error[error_num - 1] = "^"
                    #         filewrite(file_out, inputline.rstrip('\n') + '\n')
                    #         filewrite(file_out, ''.join(error) + '\n')
                    #
                    #         i = 0
                    #         textState = 0
                    #         break
                    #     elif MERGED1[i].tokenName == "LITERAL" and text1[0] == '"':
                    #         text1.popleft()
                    #         error_num = error_num + 1
                    #         table.append(["Not Matched", '"'])
                    #         # 만약 허용되는 글자인데 없으면, 혹은 ", ' 따옴표들이면 짝 쓰시오 오류 메시
                    #         file_out.close()
                    #         file_out = open(f"{filename.replace('.java', '')}.out", 'w')
                    #         printStr = "ERROR: is not LITERAL type line:" + str(error_line)
                    #
                    #         filewrite(file_out, printStr)
                    #         filewrite(file_out, '\n')
                    #         is_error = 1
                    #
                    #         for index in range(error_num):
                    #             error.append(" ")
                    #         error[error_num - 1] = "^"
                    #         filewrite(file_out, inputline.rstrip('\n') + '\n')
                    #         filewrite(file_out, ''.join(error) + '\n')
                    #         i = 0
                    #         textState = 0
                    #         break
                    subStr = ""
                    subStr += text1.popleft()
                    error_num = error_num + 1
                    table.append(["Not Match", subStr])  # 없는 글자 처리해줌.

                    file_out.close()
                    file_out = open(f"{filename.replace('.java', '')}.out", 'w')
                    printStr = "ERROR: There is a letter " + '"' + subStr + '"' + " is not acceptable. line:" + str(
                        error_line)

                    filewrite(file_out, printStr)
                    filewrite(file_out, '\n')
                    is_error = 1

                    for index in range(error_num):
                        error.append(" ")
                    error[error_num - 1] = "^"
                    filewrite(file_out, inputline.rstrip('\n') + '\n')
                    filewrite(file_out, ''.join(error) + '\n')

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
            for i in range(len(MERGED5)):
                while textState < len(text1) and MERGED5[i].wscheckIng(text1[textState]) == 1:
                    MERGED5[i].nextState(text1[textState])
                    if MERGED5[i].isIng == 1:
                        textState += 1
                    else:
                        break

                if MERGED5[i].isAccepted():
                    subStr = ""
                    text1copy = text1
                    for _ in range(textState):
                        subStr += text1.popleft()
                        error_num = error_num + 1
                    # table.append([MERGED5[i].acceptedToken(), subStr])
                    textState = 0
                    MERGED5[i].clear()
                else:
                    MERGED5[i].clear()
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



class error_report:


    def __init__(self, filename):  # startState
        self.subStr = ""
        self.error_num = 0
        self.error_line = 0
        self.is_error = 0
        self.f = open(filename, 'r') #filename = sys.argv[1]
        self.file_out

    def fileopen(self, file, string):
        self.file_out = open(f"{filename.replace('.java', '')}.out", 'w')


    def filewrite(self, file, string):
        file.write(string)

    def fileclose(self, file):
        f.close()

    def count_line(self):
        self.error_line = self.error_line + 1

    def count_error(self):
        self.error_num = self.error_num + 1

    def write_file(self):
        file_out.close()
        file_out = open(f"{filename.replace('.java', '')}.out", 'w')
        printStr = "ERROR: There is a letter " + '"' + subStr + '"' + " is not acceptable. line:" + str(error_line)

        filewrite(file_out, printStr)
        filewrite(file_out, '\n')

        self.is_error = 1

        for index in range(error_num):
            error.append(" ")

        error[error_num - 1] = "^"
        filewrite(file_out, inputline.rstrip('\n') + '\n')
        filewrite(file_out, ''.join(error) + '\n')

        for index in range(error_num):
            error.append(" ")

    def check_error(self):
        return self.is_error




    if is_error == 0 :
        for i in range(len(table)):
            #print("table:", table[i])
            filewrite(file_out, str(table[i]))
            filewrite(file_out, "\n")

