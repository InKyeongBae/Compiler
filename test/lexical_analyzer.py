import sys
from DFA import *
from collections import deque

# The elements in each array are ordered according to priority
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

for inputStr in inputline:
    table = []
    inputline = inputStr

    # Use deque to check and popleft() the first letter
    text1 = deque(inputline)
    textState = 0

    # error report
    error_line = error_line + 1
    error_num = 0

    symbols = ["'", '"', ',', '{', '}', '(', ')', '!', ">", "<", '=', ';', '[', ']']

    # If an error occurs, not to be checked from the next input(java file) line.
    if is_error == 1 :
        break
    else :
        # 1) Depending on what alphabet text1[0] is now,
        #   perform lexical_analyzing to classify tokens and popleft() when classified as specific tokens
        # 2) Repeat until all are pop and there are no more letters left in text1.
        while len(text1) > 0:
            error = []
            # 1) When the alphabet you examine is an alphabet in the symbols array defined in line 38
            ## Checking about MERGED1
            if text1[textState] in symbols :
                for i in range(len(MERGED1)):

                    # case : LITERAL & CHARACTER
                    ## to check the blank is WHITESPACE lexemes
                    if i == 0 or i == 1:
                        while textState < len(text1) and MERGED1[i].wscheckIng(text1[textState]) == 1:
                            MERGED1[i].nextState(text1[textState])
                            if MERGED1[i].isIng == 1:
                                textState += 1
                            else:
                                break

                    ## to check the input is in the token's alphabet
                    else:
                        while textState < len(text1) and MERGED1[i].checkIng(text1[textState]) == 1:
                            MERGED1[i].nextState(text1[textState])
                            if MERGED1[i].isIng == 1:
                                textState += 1
                            else:
                                break

                    ## case : Accept
                    if MERGED1[i].isAccepted():
                        subStr = ""
                        text1copy = text1

                        for _ in range(textState):
                            subStr += text1.popleft()
                            error_num = error_num + 1

                        table.append([MERGED1[i].acceptedToken(), subStr])
                        textState = 0

                        # for reuse MERGED1[i]
                        MERGED1[i].clear()
                        break
                    ## case : Reject
                    ### When all the tokens of the MERGED2 array have been examined,
                    ### to send out errors without looping infinity
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
                    ## case : Reject
                    ### Check next token in MERGED2
                    else:
                        MERGED1[i].clear()
                        i += 1
                        textState = 0

            # 2) When the alphabet you examine is LETTER or '_'
            ## Checking about MERGED2
            elif text1[textState] in LETTER or text1[textState] == "_":
                for i in range(len(MERGED2)):
                    ## to check the input is in the token's alphabet
                    while textState < len(text1) and MERGED2[i].checkIng(text1[textState]) == 1:
                        MERGED2[i].nextState(text1[textState])
                        if MERGED2[i].isIng == 1:
                            textState += 1
                        else:
                            break

                    # If it's the last word in a sentence
                    if textState >= len(text1):
                        ## case : Accept
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
                        ## case : Reject
                        ### When all the tokens of the MERGED1 array have been examined,
                        ### to send out errors without looping infinity
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
                        ## case : Reject
                        ### Check next token in MERGED1
                        else:
                            MERGED2[i].clear()
                            i += 1
                            textState = 0

                    # If it's not the last word in a sentence
                    else:
                        ## case : Accept
                        ### case : BOOLEAN, KEYWORD, TYPE
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
                        ## case : Accept
                        ### case : IDENTIFIER
                        elif MERGED2[i].isAccepted() and i == len(MERGED2) - 1:
                            subStr = ""
                            for _ in range(textState):
                                subStr += text1.popleft()
                                error_num = error_num + 1

                            table.append([MERGED2[i].acceptedToken(), subStr])
                            textState = 0
                            MERGED2[i].clear()
                            break
                        ## case : Reject
                        ### When all the tokens of the MERGED1 array have been examined,
                        ### to send out errors without looping infinity
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
                        ## case : Reject
                        ### Check next token in MERGED1
                        else:
                            MERGED2[i].clear()
                            i += 1
                            textState = 0

            # 3) When the alphabet you examine is OPERATOR or DIGIT
            ## Checking about MERGED3
            elif text1[textState] in OPERATOR or text1[0] in DIGIT:
                idx = 0
                # Solve MINUS PROBLEM
                if table and (table[-1][0] == "IDENTIFIER" or table[-1][0] == "INTEGER" or table[-1][0] == "CHARACTER" ) and text1[textState] == "-":  # MINUS PROBLEM
                    idx = 1

                for i in range(idx, len(MERGED3)):
                    ## to check the input is in the token's alphabet
                    while textState < len(text1) and MERGED3[i].checkIng(text1[textState]) == 1:
                        MERGED3[i].nextState(text1[textState])
                        if MERGED3[i].isIng == 1:
                            textState += 1
                        else:
                            break
                    ## case : Accept
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
                    ## case : Reject
                    ### When all the tokens of the MERGED3 array have been examined,
                    ### to send out errors without looping infinity
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
                    ## case : Reject
                    ### Check next token in MERGED3
                    else:
                        MERGED3[i].clear()
                        i += 1
                        textState = 0

            # 4) When the alphabet you examine is WHITESPACE
            ## Checking about MERGED4
            elif text1[textState] in WHITESPACE:

                for i in range(len(MERGED4)):
                    ## to check the input is in the token's alphabet
                    while textState < len(text1) and MERGED4[i].wscheckIng(text1[textState]) == 1:
                        MERGED4[i].nextState(text1[textState])
                        if MERGED4[i].isIng == 1:
                            textState += 1
                        else:
                            break
                    ## case : Accept
                    if MERGED4[i].isAccepted():
                        subStr = ""
                        text1copy = text1
                        for _ in range(textState):
                            subStr += text1.popleft()
                            error_num = error_num + 1
                        textState = 0
                        MERGED4[i].clear()
                        break
                    ## case : Reject
                    ### Check next token in MERGED4
                    else:
                        MERGED4[i].clear()
                        i += 1
                        textState = 0

            # 5) When the alphabet you examine is not defined alphabet
            ## ex) &, $, \
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

        # Create token table in out file only if token is well classified without error
        if is_error == 0 :
            for i in range(len(table)):
                filewrite(file_out, str(table[i]))
                filewrite(file_out, "\n")

f.close()



