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

terminal_list = []
err = 0
for inputStr in inputline:
    if inputStr[0] == "E" :
        filewrite(file_out, "ERROR : input file(Lexical Analysis Result) error")
        err = 1
        break
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
            elif list_str[3] == "*" or list_str == "/" :
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
            printStr = "ERROR : not match type : " + list_str[1]
            filewrite(file_out, printStr)
            filewrite(file_out, '\n')
            break

terminal_list.append(END_MARK)
print(terminal_list)

now_stack = [0]
spliter_pos = 0

k = 0
while (True and err == 0):
    k += 1
    print("!!!", k)
    # current state
    current_state = now_stack[-1]

    # next input symbol is deicded by position of spliter
    next_symbol = terminal_list[spliter_pos]
    # next input symbol shoud be in SLR_TABLE
    # if not, error
    if next_symbol not in SLR_TABLE[current_state].keys():
        file_out.close()
        file_out = open(f"{filename.replace('.out', '')}_final.out", 'w')
        print(next_symbol)
        print(spliter_pos)
        print(SLR_TABLE[current_state].keys())
        print("REJECT 1")
        printStr = "REJECT"
        filewrite(file_out, printStr)
        filewrite(file_out, '\n')
        break


    # shift
    if (SLR_TABLE[current_state][next_symbol][0] == 's'):
        # move position of spliter
        spliter_pos = spliter_pos + 1
        # push stack to next state
        now_stack.append(int(SLR_TABLE[current_state][next_symbol][1]))

    # reduce
    elif (SLR_TABLE[current_state][next_symbol][0] == 'r'):
        buf_string = SLR_TABLE[current_state][next_symbol][1]
        # get rule , type is list
        buf_rule = RULES[buf_string].split()
        buf_length = len(buf_rule) - 2  # ex) 'STMT → VDECL' , we only need VDECL
        # revise terminal list
        for i in range(buf_length):
            if (buf_rule[2] != 'epsilon'):  # if not epsilon
                # pop out from stack
                now_stack.pop()
                terminal_list.pop(spliter_pos - i - 1)
        if (buf_rule[2] != 'epsilon'):  # if not epsilon
            spliter_pos = spliter_pos - buf_length + 1
        else:  # if epsilon
            spliter_pos = spliter_pos + 1
        # revise terminal list
        terminal_list.insert(spliter_pos - 1, buf_rule[0])
        current_state = now_stack[-1]
        # Print for debugging
        # print(self.terminal_list)
        if ((buf_rule[0] == 's') and (len(terminal_list) == 2) and (spliter_pos == 1)):
            file_out.close()
            file_out = open(f"{filename.replace('.out', '')}_final.out", 'w')
            printStr = "ACCEPT"
            print("ACCEPT")
            filewrite(file_out, printStr)
            filewrite(file_out, '\n')
            break
        if buf_rule[0] not in SLR_TABLE[current_state].keys():
            file_out.close()
            file_out = open(f"{filename.replace('.out', '')}_final.out", 'w')
            print(buf_rule[0])
            print(SLR_TABLE[current_state].keys())
            print("REJECT 2")
            printStr = "REJECT"
            filewrite(file_out, printStr)
            filewrite(file_out, '\n')
            break
        now_stack.append(SLR_TABLE[current_state][buf_rule[0]])


