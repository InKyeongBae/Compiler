from collections import deque

TYPE = ['int', 'char', 'boolean', 'String']
BOOLEAN = ['true', 'false']
OPERATOR = ['-', '+', '*', '/']

WHITESPACE = ['\t', '\n', ' ']

BLANK = ' '

# Alphabet Definition
LETTER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
          'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']
DIGIT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

POS_DIGIT = DIGIT[1:]


# DFA (in the form of transition table)
class FiniteAutomata:  # Finite Automata for NFA, DFA
    tokenName = ""
    F = {}
    Sigma = []
    # q0 = []
    state = 0
    Q = []
    Delta = {}
    isIng = 1

    def __init__(self, token, states, alphabet, final, table):  # startState
        self.tokenName = token
        self.Q = states
        self.Sigma = alphabet
        self.state = "T0"
        self.F = final
        self.Delta = self.transition(table)

    def isAccepted(self):
        if self.state in self.F:
            print("Accepted")
            return True
        else:
            print("Rejected")
            return False

    def checkIng(self, input):
        isAlpha = 0
        for i in self.Sigma:
            #print("-------------------------------------/////", input, i)
            if input not in i:
                print("not in")
                isAlpha = 0
            elif input == ' ':
                print("blank")
                isAlpha = 0
            else:
                print("in")
                isAlpha = 1
                break
        print("checkIng input:", input)
        if isAlpha == 0:
            print(f'{input}: undefined alphabet')
            self.isIng = 0
        else:
            print(f'{input}: defined alphabet')
            self.isIng = 1

        if self.isIng == 0:
            # print(f'{input}: automata dead')
            return self.isIng
        else:
            return self.isIng

    def wscheckIng(self, input):
        isAlpha = 0
        print("wschecking")
        for i in self.Sigma:
            #print(self.Sigma, self.tokenName)
            #print("---------------------------------------////////", i)
            
            if input not in i:
                print("no")
                #print("input:* ",input)
                isAlpha = 0
            else:
                #print("input:* ",input)
                print("yes!")
                isAlpha = 1
                break
        if isAlpha == 0:
            print(f'{input}: undefined alphabet')
            self.isIng = 0
        else:
            print(f'{input}: defined alphabet')
            self.isIng = 1

        if self.isIng == 0:
            # print(f'{input}: automata dead')
            return self.isIng
        else:
            return self.isIng

    def nextState(self, input):  # transition table에서 입력하나 보고 간 state,
        items = self.Delta[self.state].items()
        posNext = dict()
        for key, value in items:
            if value != "":
                posNext[key] = value
        keys = posNext.keys()
        newKey = ""
        inputStr = ""
        print("--------------------->", input)
        #print(keys)
        for i in keys:
            if len(i) > 1: #  ast.literal_eval(x), json
                print("뀨뀨뀨뀨뀨")
                i = i.strip('][').replace("'", "").split(', ')
                #print("string to list ",i)
            if input in i:
                #print("없지?", input)
                #print("hey", i, type(i))
                newKey = str(i)
                
        
        #print("nextState", posNext)
        if newKey in posNext:
            print("wowowowo")
            print(newKey, type(newKey), type(posNext))
            nextState = posNext[newKey]
        else:
            self.isIng = 0
            return self.isIng
        self.state = nextState
        return self.isIng

    def moveState(self, next_state):  # state update하기
        self.state = next_state

    def currentState(self, next_state):  # state update하기
        return self.state

    def acceptedToken(self):  # if accepted or not
        if self.state in self.F:
            return self.tokenName
        else:
            return "Not Accepted"

    def clear(self):  # 재사용하게 reset
        self.state = "T0"
        self.isIng = 1
        return

    def transition(self, table):
        delta = {}
        for T in self.Q:
            delta[T] = {}
            i = 0
            self.Delta.update({str(T): {}})
            for alphabet in self.Sigma:
                # print("**")
                # print(str(T), "/", alphabet, "/", table[str(T)][i])
                delta[str(T)][str(alphabet)] = table[str(T)][i]
                i = i + 1
        return delta


# Regular expressions 이부분은 구현하지 않는거고, DFA가 같은 효과인가?
# INT=((-|e)*Digit[1:]DIGIT*|0) #?->finite automata

Integer = FiniteAutomata(
    "INTEGER",  # matched token name
    ["T0", "T1", "T2", "T3", "T4"],  # state
    ["-", "0", str(POS_DIGIT), str(DIGIT)],  # input stream
    ["T2", "T3", "T4"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "T2", "T3", ""],
        "T1": ["", "", "T3", ""],
        "T2": ["", "", "", ""],
        "T3": ["", "", "", "T4"],
        "T4": ["", "", "", "T4"]
    }
)


Whitespace = FiniteAutomata(
    "WHITESPACE",  # matched token name
    ["T0", "T1", "T2", "T3"],  # state
    ["\t", "\n", " "],  # input stream
    ["T1", "T2", "T3"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "T2", "T3"],
        "T1": ["", "", ""],
        "T2": ["", "", ""],
        "T3": ["", "", ""],
        "T4": ["", "", ""]
    }
)

Boolean = FiniteAutomata(
    "BOOLEAN",  # matched token name
    ["T0", "T1", "T2"],  # state
    ["true", "false"],  # input stream
    ["T1", "T2"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "T2"],
        "T1": ["", ""],
        "T2": ["", ""]
    }
)

#"'"
Character = FiniteAutomata(
    "CHARACTER",  # matched token name
    ["T0", "T1", "T2", "T3", "T4", "T5"],  # state
    ["'", str(LETTER), str(DIGIT), str(BLANK)],  # input stream
    ["T5"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "", ""],
        "T1": ["T5", "T2", "T3", "T4"],
        "T2": ["T5", "", "", ""],
        "T3": ["T5", "", "", ""],
        "T4": ["T5", "", "", ""],
        "T5": ["", "", "", ""]
    }
)

Operator = FiniteAutomata(
    "OPERATOR",  # matched token name
    ["T0", "T1", "T2", "T3", "T4"],  # state
    ["+", "-", "*", "/"],  # input stream
    ["T1", "T2", "T3", "T4"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "T2", "T3", "T4"],
        "T1": ["", "", "", ""],
        "T2": ["", "", "", ""],
        "T3": ["", "", "", ""],
        "T4": ["", "", "", ""]
    }
)

##########finite안에 finite
Type = FiniteAutomata(
    "TYPE",  # matched token name
    ["T0", "T1", "T2", "T3", "T4"],  # state
    ["int", "char", "boolean", "String"],  # input stream
    ["T1", "T2", "T3", "T4"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "T2", "T3", "T4"],
        "T1": ["", "", "", ""],
        "T2": ["", "", "", ""],
        "T3": ["", "", "", ""],
        "T4": ["", "", "", ""]
    }
)

Identifier = FiniteAutomata(
    "IDENTIFIER",  # matched token name
    ["T0", "T1", "T2", "T3", "T4", "T5"],  # state
    [str(LETTER), str(DIGIT), "_"],  # input stream
    ["T1", "T2", "T3", "T4", "T5"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "T2"],
        "T1": ["T3", "T4", "T5"],
        "T2": ["T3", "T4", "T5"],
        "T3": ["T3", "T4", "T5"],
        "T4": ["T3", "T4", "T5"],
        "T5": ["T3", "T4", "T5"]
    }
)

Relop = FiniteAutomata(
    "RELOP",  # matched token name
    ["T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"],  # state
    ["<", "=", "!", ">"],  # input stream
    ["T1", "T4", "T5", "T6", "T7", "T8"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "T2", "T3", "T4"],
        "T1": ["", "T5", "", ""],
        "T2": ["", "T6", "", ""],
        "T3": ["", "T7", "", ""],
        "T4": ["", "T8", "", ""],
        "T5": ["", "", "", ""],
        "T6": ["", "", "", ""],
        "T7": ["", "", "", ""],
        "T8": ["", "", "", ""]
    }
)

If = FiniteAutomata(
    "IF",  # matched token name
    ["T0", "T1", "T2"],  # state
    ["i", "f"],  # input stream
    ["T2"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", ""],
        "T1": ["", "T2"],
        "T2": ["", ""]
    }
)

Else = FiniteAutomata(
    "ELSE",  # matched token name
    ["T0", "T1", "T2", "T3", "T4"],  # state
    ["e", "l", "s"],  # input stream
    ["T4"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", ""],
        "T1": ["", "T2", ""],
        "T2": ["", "", "T3"],
        "T3": ["T4", "", ""],
        "T4": ["", "", ""]
    }
)

While = FiniteAutomata(
    "WHILE",  # matched token name
    ["T0", "T1", "T2", "T3", "T4", "T5"],  # state
    ["w", "h", "i", "l", "e"],  # input stream
    ["T5"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "", "", ""],
        "T1": ["", "T2", "", "", ""],
        "T2": ["", "", "T3", "", ""],
        "T3": ["", "", "", "T4", ""],
        "T4": ["", "", "", "", "T5"],
        "T5": ["", "", "", "", ""]
    }
)

Class = FiniteAutomata(
    "CLASS",  # matched token name
    ["T0", "T1", "T2", "T3", "T4", "T5"],  # state
    ["c", "l", "a", "s"],  # input stream
    ["T5"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "", ""],
        "T1": ["", "T2", "", ""],
        "T2": ["", "", "T3", ""],
        "T3": ["", "", "", "T4"],
        "T4": ["", "", "", "T5"],
        "T5": ["", "", "", ""]
    }
)

Return = FiniteAutomata(
    "RETURN",  # matched token name
    ["T0", "T1", "T2", "T3", "T4", "T5", "T6"],  # state
    ["r", "e", "t", "u", "n"],  # input stream
    ["T6"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "", "", ""],
        "T1": ["", "T2", "", "", ""],
        "T2": ["", "", "T3", "", ""],
        "T3": ["", "", "", "T4", ""],
        "T4": ["T5", "", "", "", ""],
        "T5": ["", "", "", "", "T6"],
        "T6": ["", "", "", "", ""]
    }
)

Keyword = FiniteAutomata(
    "KEYWORD",  # matched token name
    ["T0", "T1", "T2", "T3", "T4", "T5"],  # state
    ["if", "else", "while", "class", "return"],  # input stream
    ["T1", "T2", "T3", "T4", "T5"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "T2", "T3", "T4", "T5"],
        "T1": ["", "", "", "", "", ""],
        "T2": ["", "", "", "", "", ""],
        "T3": ["", "", "", "", "", ""],
        "T4": ["", "", "", "", "", ""],
        "T5": ["", "", "", "", "", ""]
    }
)

#"\""가 맞나?
Literal = FiniteAutomata(
    "LITERAL",  # matched token name
    ["T0", "T1", "T2", "T3", "T4", "T5"],  # state
    ['"', str(DIGIT), str(LETTER), str(BLANK)],  # input stream
    ["T5"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "", ""],
        "T1": ["T5", "T2", "T3", "T4"],
        "T2": ["T5", "T2", "T3", "T4"],
        "T3": ["T5", "T2", "T3", "T4"],
        "T4": ["T5", "T2", "T3", "T4"],
        "T5": ["", "", "", "", "", ""]
    }
)

Comma = FiniteAutomata(
    "COMMA",  # matched token name
    ["T0", "T1"],  # state
    [","],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

# Minus = FiniteAutomata(
#     "MINUS",  # matched token name
#     ["T0", "T1"],  # state
#     ["-"],  # input stream
#     ["T1"],  # accepted state
#     {  # nfa to dfa transition table
#         "T0": ["T1"],
#         "T1": [""]
#     }
# )

Semicolon = FiniteAutomata(
    "SEMICOLON",  # matched token name
    ["T0", "T1"],  # state
    [";"],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Lbrace = FiniteAutomata(
    "LBRACE",  # matched token name
    ["T0", "T1"],  # state
    ["{"],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Rbrace = FiniteAutomata(
    "RBRACE",  # matched token name
    ["T0", "T1"],  # state
    ["}"],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Lparen = FiniteAutomata(
    "LPAREN",  # matched token name
    ["T0", "T1"],  # state
    ["("],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Rparen = FiniteAutomata(
    "RPAREN",  # matched token name
    ["T0", "T1"],  # state
    [")"],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Larray = FiniteAutomata(
    "LARRAY",  # matched token name
    ["T0", "T1"],  # state
    ["["],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Rarray = FiniteAutomata(
    "RARRAY",  # matched token name
    ["T0", "T1"],  # state
    ["]"],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Assign = FiniteAutomata(
    "ASSIGN",  # matched token name
    ["T0", "T1"],  # state
    ["="],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

TTrue = FiniteAutomata(
    "TRUE",  # matched token name
    ["T0", "T1", "T2", "T3", "T4"],  # state
    ["t", "r", "u", "e"],  # input stream
    ["T4"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "", ""],
        "T1": ["", "T2", "", ""],
        "T2": ["", "", "T3", ""],
        "T3": ["", "", "", "T4"],
        "T4": ["", "", "", ""],
    }
)

TFalse = FiniteAutomata(
    "FALSE",  # matched token name
    ["T0", "T1", "T2", "T3", "T4", "T5"],  # state
    ["f", "a", "l", "s", "e"],  # input stream
    ["T5"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "", "", ""],
        "T1": ["", "T2", "", "", ""],
        "T2": ["", "", "T3", "", ""],
        "T3": ["", "", "", "T4", ""],
        "T4": ["", "", "", "", "T5"],
        "T5": ["", "", "", "", ""]
    }
)

TInt = FiniteAutomata(
    "INT",  # matched token name
    ["T0", "T1", "T2", "T3"],  # state
    ["i", "n", "t"],  # input stream
    ["T3"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", ""],
        "T1": ["", "T2", ""],
        "T2": ["", "", "T3"],
        "T3": ["", "", ""],
    }
)

TChar = FiniteAutomata(
    "CHAR",  # matched token name
    ["T0", "T1", "T2", "T3", "T4"],  # state
    ["c", "h", "a", "r"],  # input stream
    ["T4"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "", ""],
        "T1": ["", "T2", "", ""],
        "T2": ["", "", "T3", ""],
        "T3": ["", "", "", "T4"],
        "T4": ["", "", "", ""],
    }
)

TBoolean = FiniteAutomata(
    "BOOLEAN",  # matched token name
    ["T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7"],  # state
    ["b", "o", "l", "e", "a", "n"],  # input stream
    ["T7"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "", "", "", ""],
        "T1": ["", "T2", "", "", "", ""],
        "T2": ["", "T3", "", "", "", ""],
        "T3": ["", "", "T4", "", "", ""],
        "T4": ["", "", "", "T5", "", ""],
        "T5": ["", "", "", "", "T6", ""],
        "T6": ["", "", "", "", "", "T7"],
        "T7": ["", "", "", "", "", ""],
    }
)

TString = FiniteAutomata(
    "STRING",  # matched token name
    ["T0", "T1", "T2", "T3", "T4", "T5", "T6"],  # state
    ["S", "t", "r", "i", "n", "g"],  # input stream
    ["T6"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "", "", "", ""],
        "T1": ["", "T2", "", "", "", ""],
        "T2": ["", "", "T3", "", "", ""],
        "T3": ["", "", "", "T4", "", ""],
        "T4": ["", "", "", "", "T5", ""],
        "T5": ["", "", "", "", "", "T6"],
        "T6": ["", "", "", "", "", ""]
    }
)

#If, Else, While, Class, Return, Minus
#boolean keyword type

MERGED1 = [Literal, Character, Comma, Lbrace, Rbrace, Lparen, Rparen, Relop, Assign, Semicolon, Larray, Rarray]
MERGED02 = [TTrue, TFalse, Class, If, Else, While, Return, TInt, TChar, TBoolean, TString, Identifier]
MERGED3 = [Integer, Operator]
MERGED4 = [Relop, Assign]
MERGED5 = [Whitespace]

table = []
file = "a---1" #a-1 a+-1 #1-1, 1+1, -1-123 \"%\"
# text1 = deque("int while if return true false char boolean String")
text1 = deque(file)
#int main(){char if123='1';int 0a=a+-1;return -0;}

textState = 0
print("처음")
symbols = ["'", '"', ',', '{', '}', '(', ')', '!', ">", "<", '=', ';', '[', ']']
while len(text1) > 0:
    print("length: ",)
    print("input",text1)
    if text1[textState] in symbols :
        print("1")
        print("@@@@@@@@@")
        for i in range(len(MERGED1)):
            print("wwwwwwwwwww", MERGED1[i].tokenName)
            if i == 0 :
                print("1-1")
                while textState < len(text1) and MERGED1[i].wscheckIng(text1[textState]) == 1:
                    MERGED1[i].nextState(text1[textState])
                    if MERGED1[i].isIng == 1:
                        print("ifififif")
                        textState += 1
                    else:
                        print("elseelseelseelseelseelseelseelseelseelseelse")
                        #if text1[1]=="'":   
                        break
                    ##
                    
            else :
                print("1-2")
                while textState < len(text1) and MERGED1[i].checkIng(text1[textState]) == 1:
                    MERGED1[i].nextState(text1[textState])
                    if MERGED1[i].isIng == 1:
                        textState += 1
                    else:
                        print("breakbreak")
                        break

            if MERGED1[i].isAccepted():
                print("1-1-1")
                subStr = ""
                text1copy = text1
                for _ in range(textState):
                    #print(text1[_])
                    subStr += text1.popleft()
                    
                print(">>>", subStr, textState)
                table.append([MERGED1[i].acceptedToken(), subStr])
                textState = 0
                MERGED1[i].clear()          
            else:
                print("1-1-2")
                print("####3333###", textState)
                MERGED1[i].clear()
                print("흠", textState, text1, i)
                if text1:
                    if MERGED1[i].tokenName == "CHARACTER" and text1[0] == "'":
                        text1.popleft() 
                        table.append(["Not Matched", "'"])
                        # 만약 허용되는 글자인데 없으면, 혹은 ", ' 따옴표들이면 짝 쓰시오 오류 메시
                        print("'짝이 안 맞는 에러")
                        i = 0
                        break
                    elif MERGED1[i].tokenName == "LITERAL" and text1[0] == '"':
                        text1.popleft() 
                        table.append(["Not Matched", '"'])
                        # 만약 허용되는 글자인데 없으면, 혹은 ", ' 따옴표들이면 짝 쓰시오 오류 메시
                        print("'짝이 안 맞는 에러")
                        i = 0
                        break
                    
                i += 1
                textState = 0

            
    elif text1[textState] in LETTER or text1[textState] == "_":
        print("2")
        for i in range(len(MERGED02)):
            while textState < len(text1) and MERGED02[i].checkIng(text1[textState]) == 1:
                MERGED02[i].nextState(text1[textState])
                if MERGED02[i].isIng == 1:
                    textState += 1
                else:
                    break

            #마지막 글자면
            if textState >= len(text1) :
                if MERGED02[i].isAccepted():
                    subStr = ""
                    for _ in range(textState):
                        subStr += text1.popleft()
                    if i == len(MERGED02) - 1 :
                        table.append([MERGED02[i].acceptedToken(), subStr])
                    elif i >= 0 and i < 2 :
                        table.append(['BOOLEAN', subStr])
                    elif i >= 2 and i < 7 :
                        table.append(['KEYWORD', subStr])
                    else :
                        table.append(['TYPE', subStr])
                    textState = 0
                    MERGED02[i].clear()
                else:
                    MERGED02[i].clear()
                    i += 1
                    textState = 0
            # - 는 앞 뒤 내용에 따라 달라짐. (연산자 일 때)
            else :
                if MERGED02[i].isAccepted() and text1[textState] == ' ' and i != len(MERGED02) - 1:
                    print("2-0")
                    subStr = ""
                    for _ in range(textState):
                        subStr += text1.popleft()
                    if i >= 0 and i < 2:
                        table.append(['BOOLEAN', subStr])
                    elif i >= 2 and i < 7:
                        table.append(['KEYWORD', subStr])
                    else:
                        table.append(['TYPE', subStr])
                    textState = 0
                    MERGED02[i].clear()

                elif MERGED02[i].isAccepted() and i == len(MERGED02) - 1:
                    print("2-1")
                    subStr = ""
                    for _ in range(textState):
                        subStr += text1.popleft()
                    table.append([MERGED02[i].acceptedToken(), subStr])
                    textState = 0
                    MERGED02[i].clear()
                else:
                    print("2-2")
                    MERGED02[i].clear()
                    print()
                    i += 1
                    textState = 0
                    if text1[0] == "'":
                        
                        print(table)
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(MERGED02[i].tokenName)
                        print(MERGED02[i].Sigma)
                        
    
    #3) 숫자가 들어올 때
    elif text1[textState] in OPERATOR or text1[0] in DIGIT:
        print("3")
        print("%%%")
        if table and table[-1][0] == "IDENTIFIER": # MINUS PROBLEM
            idx = 1
        if table and table[-1][0] == "OPERATOR" and text1[textState]== "-": # MINUS PROBLEM
            idx = 0
        for i in range(idx,len(MERGED3)):
            
            print("-----------------------------------------------------------", i)
            while textState < len(text1) and MERGED3[i].checkIng(text1[textState]) == 1:
                print("~~~~~~~~~~~~~~~~~")
                MERGED3[i].nextState(text1[textState])
                if MERGED3[i].isIng == 1:
                    print("if")
                    textState += 1
                    #if 
                    #i = 0 # ?
                else: #accaept이 안됨. 
                    print("else")
                    break

            #MERGED를 다 돈게 아닌 상태에서 넘어감. 
            if MERGED3[i].isAccepted():
                print("&&**&&: ")#, text1[textState-1])
                subStr = ""
                text1copy = text1
                print("엥구")
                #if textState == 0: #MINUS PROBLEM -1 #for operator "-" ex) 1-1
                #    subStr += text1.popleft()

                for _ in range(textState):
                    print("엥구")
                    subStr += text1.popleft()  #1
                    
                print(">>>",subStr)
                #print(text1)
                #if text1[0] == "-": #MINUS PROBLEM -2 #
                #    if table[-1][0] == "IDENTIFIER":
                #        table.append(["OPERATOR", subStr[0]])
                #        table.append([MERGED3[i].acceptedToken(), subStr[1:]])
                #else:
                
                table.append([MERGED3[i].acceptedToken(), subStr])
                textState = 0
                MERGED3[i].clear()

                if MERGED3[i].tokenName == "INTEGER":
                    i = 1
                    print("제발제발제발제발요")
                else:
                    i = 0

                print(i, MERGED3[i].tokenName)
            else:
                MERGED3[i].clear()
                i += 1
                textState = 0
                

    elif text1[textState] in WHITESPACE :
        print("4")
        for i in range(len(MERGED5)):
            while textState < len(text1) and MERGED5[i].wscheckIng(text1[textState]) == 1:
                MERGED5[i].nextState(text1[textState])
                if MERGED5[i].isIng == 1:
                    textState += 1
                    print("$$")
                else:
                    break

            if MERGED5[i].isAccepted():
                print("#2")
                subStr = ""
                text1copy = text1
                for _ in range(textState):
                    subStr += text1.popleft()
                # table.append([MERGED5[i].acceptedToken(), subStr])
                textState = 0
                MERGED5[i].clear()
            else:
                MERGED5[i].clear()
                i += 1
                textState = 0

    else :
        print("5")
        print("text:",text1[textState])
        subStr = ""
        subStr += text1.popleft()
        table.append(["Not Match", subStr]) #없는 글자 처리해줌. 
        textState = 0

print("#############")
for i in range(len(table)) :
    print("table:", table[i])






