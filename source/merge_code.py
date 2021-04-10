from collections import deque

TYPE = ['int', 'char', 'boolean', 'String']
BOOLEAN = ['true', 'false']
OPERATOR = ['-', '+', '*', '/']

WHITESPACE = ['\t', '\n', ' ']

BLANK = ' '

# Alphabet Definition
LETTER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q,' 'R', 'S', 'T', 'U',
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
            if input not in i:
                isAlpha = 0
            # 이렇게 하면 나중에 whitespace 어떡하지...ㅠㅠ
            elif input == ' ':
                isAlpha = 0
            else:
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

    def wscheckIng(self, input):
        isAlpha = 0
        for i in self.Sigma:
            if input not in i:
                isAlpha = 0
            else:
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
        for i in keys:
            if input in i:
                newKey = i

        if newKey in posNext:
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
        "T1": ["", "T2", "T3", "T4"],
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
    ["T0", "T1", "T2", "T3", "T4", "T5", "T6"],  # state
    ["<", "=", "!", ">"],  # input stream
    ["T1", "T2", "T3", "T5", "T6"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "T2", "T3", "T4"],
        "T1": ["", "T5", "", ""],
        "T2": ["", "", "", ""],
        "T3": ["", "", "", ""],
        "T4": ["", "T6", "", ""],
        "T5": ["", "", "", ""],
        "T6": ["", "", "", ""]
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
        "T1": ["", "T2", "T3", "T4"],
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
MERGED02 = [TTrue, TFalse, Class, If, Else, While, Return, TInt, TChar, TBoolean, TString, Identifier]
MERGED1 = [Literal, Character, Comma, Lbrace, Rbrace, Lparen, Rparen, Assign, Semicolon, Larray, Rarray]
MERGED2 = [Keyword, Boolean, Type, Identifier]
MERGED3 = [Integer, Operator]
MERGED4 = [Relop, Assign]
MERGED5 = [Whitespace]


# print(MERGED[0].Delta)
# print("----------------------------------")
# print(type(inputs[0]))
# print(type(inputs))
# print(MERGED[0])
# next = MERGED[0].nextState('1')
# MERGED[0].moveState(next)
# print(MERGED[0].isAccepted())
# print(MERGED[0].currentState(next))
# print(MERGED[0].acceptedToken())
# MERGED[0].clear()

table = []
# text1 = deque("int while if return true false char boolean String")
text1 = deque("-(-123)")
textState = 0

while len(text1) > 0:
    symbols = ["'", '"', ',', '{', '}', '(', ')', '=', ';', '[', ']']
    symbols = symbols

    if text1[textState] in symbols :
        for i in range(len(MERGED1)):
            if i == 0 :
                while textState < len(text1) and MERGED1[i].wscheckIng(text1[textState]) == 1:
                    MERGED1[i].nextState(text1[textState])
                    if MERGED1[i].isIng == 1:
                        textState += 1
                    else:
                        break
            else :
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
                print(">>>",subStr)
                table.append([MERGED1[i].acceptedToken(), subStr])
                textState = 0
                MERGED1[i].clear()
            else:
                MERGED1[i].clear()
                i += 1
                textState = 0

    elif text1[textState] in LETTER:
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
            #
            else :
                if MERGED02[i].isAccepted() and text1[textState] == ' ' and i != len(MERGED02) - 1:
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

    #3) 숫자가 들어올 때
    elif text1[textState] in OPERATOR or text1[0] in DIGIT:
        for i in range(len(MERGED3)):
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
                    subStr += text1.popleft()
                print(">>>",subStr)
                table.append([MERGED3[i].acceptedToken(), subStr])
                textState = 0
                MERGED3[i].clear()
            else:
                MERGED3[i].clear()
                i += 1
                textState = 0

    #4) 연산자 들어올 때
    elif text1[textState] in ["<", "=", "!", ">"] :
        for i in range(len(MERGED4)):
            while textState < len(text1) and MERGED4[i].checkIng(text1[textState]) == 1:
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
                print(">>>",subStr)
                table.append([MERGED4[i].acceptedToken(), subStr])
                textState = 0
                MERGED4[i].clear()
            else:
                MERGED4[i].clear()
                i += 1
                textState = 0

    elif text1[textState] in WHITESPACE :
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
                # table.append([MERGED5[i].acceptedToken(), subStr])
                textState = 0
                MERGED5[i].clear()
            else:
                MERGED5[i].clear()
                i += 1
                textState = 0


    else :
        subStr = ""
        subStr += text1.popleft()
        table.append(["Not Match", subStr])
        textState = 0

print("#############")
for i in range(len(table)) :
    print("table:", table[i])






