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
    # lexical_analyzer.py의 결과값이 ERROR라서 syntax_analyzing을 할 수 없을 때
    if inputStr[0] == "E" :
        filewrite(file_out, "[REJECT] Error 0 : input file(Lexical Analysis Result) error")
        err = 1
        break

    # lexical_analyzer.py의 결과값을 syntax_analyzer.py에 쓰이는 TERMINAL 용어로 바꾸어 list에 추가
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
                
        # lexical_analyzer.py에서는 [ ]를 올바르 토큰으로 정의하였지만
        # syntax_analyzer.py에서는 [ ]를 TERMINAL로 선언하지 않았으므로
        # [ ]가 오면 syntax_analyzer.py의 결과가 ERROR가 된다.
        else :
            file_out.close()
            file_out = open(f"{filename.replace('.out', '')}_final.out", 'w')
            printStr = "[REJECT] Error 1 : not match type : " + list_str[1]
            filewrite(file_out, printStr)
            filewrite(file_out, '\n')
            break

terminal_list.append(END_MARK)
output = ""
for i in range(0, len(terminal_list)) :
    output = output + " " + terminal_list[i]

print(output)

now_stack = [0]
position = 0

k = 0
token_index = 0 # line for error

while (err == 0):
    k += 1

    # 현재 state
    current_state = now_stack[-1]
    # 다음 input symbol
    next_symbol = terminal_list[position]

    # 다음 symbol이 SLR_TABLE에 있는 지 체크
    if next_symbol not in SLR_TABLE[current_state].keys():
        file_out.close()
        file_out = open(f"{filename.replace('.out', '')}_final.out", 'w')
        print("REJECT")
        err = 1
        # ---Error message--- #
        printStr = "[REJECT] Error 2 : Token number ({}) ".format(token_index) + inputline[token_index-1]
        message = "SyntaxError: Missing a terminal corresponding to one of the following: (token line {})".format(token_index)
        # 올바른 syntax가 되기 위해 필요한 아이템
        missing_item = [item for item in list(SLR_TABLE[current_state].keys()) if item != END_MARK and item.islower()]
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


    # shift ( 값이 's+숫자'일 때 )
    if (SLR_TABLE[current_state][next_symbol][0] == 's'):
        position = position + 1
        now_stack.append(int(SLR_TABLE[current_state][next_symbol][1:]))
        token_index += 1 # count the token index

    # reduce ( 값이 'r+숫자'일 때 )
    elif (SLR_TABLE[current_state][next_symbol][0] == 'r'):

        string_check = SLR_TABLE[current_state][next_symbol][1:]
        rule_check = RULES[string_check].split()
        rule_check_len = len(rule_check) - 2

        # terminal list 확인
        for i in range(rule_check_len):
            # epsilon이 아닐 때
            if (rule_check[2] != 'epsilon'):
                # stack에서 pop
                now_stack.pop()
                terminal = terminal_list.pop(position - i - 1)

        # epsilon이 아닐 때
        if (rule_check[2] != 'epsilon'):
            position = position - rule_check_len + 1
        # epsilon일 때
        else:
            position = position + 1
        
        # terminal list 확인
        terminal_list.insert(position - 1, rule_check[0])
        current_state = now_stack[-1]

        now_stack.append(SLR_TABLE[current_state][rule_check[0]])

    # 결과가 ACCEPT일 때
    elif (SLR_TABLE[current_state][next_symbol] == 'acc'):
        file_out.close()
        file_out = open(f"{filename.replace('.out', '')}_final.out", 'w')
        printStr = "ACCEPT"
        print("ACCEPT")
        err = 1
        filewrite(file_out, printStr)
        filewrite(file_out, '\n')
        break
