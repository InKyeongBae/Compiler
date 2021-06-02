import sys
from SLR import *
from rules import *


# file I/O
f = open(sys.argv[1], 'r')
inputline = f.readlines()
filename = sys.argv[1]

file_out = open(f"{filename.replace('.out', '')}_final.out", 'w')

def filewrite(file, string):
    file.write(string)


terminal_list = []
err = 0
for inputStr in inputline:
    if inputStr[0] == "E" :
        filewrite(file_out, "ERROR 0: input file(Lexical Analysis Result) error")
        err = 1
        break
    # print("inputStr", inputStr, end='')
    # print("terminal_list", terminal_list)
    # print("")
    if inputStr[0] == "[" :
        list_str = inputStr.split("'")
        if list_str[1] == "IDENTIFIER" :
            terminal_list.append("id")
        elif list_str[1] == "INTEGER" :
            terminal_list.append("num")
        elif list_str[1] == "CHARACTER" :
            terminal_list.append("character")
        elif list_str[1] == "BOOLEAN" :
            terminal_list.append("boolstr")
        elif list_str[1] == "LITERAL" :
            terminal_list.append("literal")
        elif list_str[1] == "COMMA" :
            terminal_list.append("comma")
        elif list_str[1] == "LBRACE" :
            terminal_list.append("lbrace")
        elif list_str[1] == "RBRACE" :
            terminal_list.append("rbrace")
        elif list_str[1] == "LPAREN" :
            terminal_list.append("lparen")
        elif list_str[1] == "RPAREN" :
            terminal_list.append("rparen")
        elif list_str[1] == "ASSIGN" :
            terminal_list.append("assign")
        elif list_str[1] == "RELOP" :
            terminal_list.append("comp")
        elif list_str[1] == "OPERATOR" :
            if list_str[3] == "+" or list_str[3] == "-" :
                terminal_list.append("addsub")
            elif list_str[3] == "*" or list_str[3] == "/" :
                terminal_list.append("multdiv")
        elif list_str[1] == "TYPE" :
            terminal_list.append("vtype")
        elif list_str[1] == "SEMICOLON" :
            terminal_list.append("semi")
        elif list_str[1] == "KEYWORD" :
            if list_str[3] == "if":
                terminal_list.append("if")
            elif list_str[3] == "else":
                terminal_list.append("else")
            if list_str[3] == "while" :
                terminal_list.append("while")
            elif list_str[3] == "class" :
                terminal_list.append("class")
            elif list_str[3] == "return":
                terminal_list.append("return")
        else :
            file_out.close()
            file_out = open(f"{filename.replace('.out', '')}_final.out", 'w')
            printStr = "ERROR 1: not match type : " + list_str[1]
            filewrite(file_out, printStr)
            filewrite(file_out, '\n')
            break

terminal_list.append(END_MARK)
#print(terminal_list)
output = ""
for i in range(0, len(terminal_list)) :
    output = output + " " + terminal_list[i]

print(output)

now_stack = [0]
position = 0

k = 0
token_index = 1 # line for error

while (err == 0):
    k += 1
<<<<<<< HEAD
=======
    # print("!!!", k)
>>>>>>> 9f0d857da65f1906fab3224a1ee4316a65464260

    # current state
    current_state = now_stack[-1]
    # next input symbol
    next_symbol = terminal_list[position]

    # next symbol이 SLR_TABLE에 있는 지 체크
    if next_symbol not in SLR_TABLE[current_state].keys():
        file_out.close()
        file_out = open(f"{filename.replace('.out', '')}_final.out", 'w')
        print("REJECT")
        err = 1
        # ---Error message--- #
        printStr = "ERROR 2: Token number ({}) ".format(token_index) + inputline[token_index-1]
        message = "SyntaxError: Lexeme " + inputline[position-1].split("'")[3] + \
                  " must be a terminal corresponding to one of the following:"
        # 올바른 syntax가 되기 위해 필요한 아이템
        missing_item = [item for item in list(SLR_TABLE[current_state].keys()) if item != END_MARK]
        missing = "             {}".format(missing_item)

        print(printStr, end='')  # 터미널 창에 출력
        print(message)
        print(missing)

        filewrite(file_out, printStr) # file out
        filewrite(file_out, message)
        filewrite(file_out, '\n')
        filewrite(file_out, missing)
        filewrite(file_out, '\n')
        # ---End of the Error message--- #
        break
<<<<<<< HEAD

=======
    # print(next_symbol, "|", current_state)
    # print(terminal_list)
    # print(position)
>>>>>>> 9f0d857da65f1906fab3224a1ee4316a65464260

    # shift
    if (SLR_TABLE[current_state][next_symbol][0] == 's'):
        position = position + 1
        now_stack.append(int(SLR_TABLE[current_state][next_symbol][1:]))
<<<<<<< HEAD
        token_index += 1 # count the token index

    # reduce
    elif (SLR_TABLE[current_state][next_symbol][0] == 'r'):
=======

    # reduce
    elif (SLR_TABLE[current_state][next_symbol][0] == 'r'):

>>>>>>> 9f0d857da65f1906fab3224a1ee4316a65464260
        string_check = SLR_TABLE[current_state][next_symbol][1:]

        rule_check = RULES[string_check].split()
        rule_check_len = len(rule_check) - 2

        # terminal list 확인
        for i in range(rule_check_len):
            if (rule_check[2] != 'epsilon'):  # if not epsilon
                # pop out from stack
                now_stack.pop()
                terminal = terminal_list.pop(position - i - 1)

        if (rule_check[2] != 'epsilon'):  # if not epsilon
            position = position - rule_check_len + 1
        else:
            # epsilon일 때
            position = position + 1
        # terminal list 확인

        terminal_list.insert(position - 1, rule_check[0])
        current_state = now_stack[-1]

        now_stack.append(SLR_TABLE[current_state][rule_check[0]])

    elif (SLR_TABLE[current_state][next_symbol] == 'acc'):
        file_out.close()
        file_out = open(f"{filename.replace('.out', '')}_final.out", 'w')
        printStr = "ACCEPT"
        print("ACCEPT")
        err = 1
        filewrite(file_out, printStr)
        filewrite(file_out, '\n')
        break
