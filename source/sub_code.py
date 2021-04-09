TYPE = ['int', 'char', 'boolean', 'String']
BOOLEAN = ['true', 'false']
OPERATOR = ['-', '+', '*', '/']

WHITESPACE = ['\t', '\n', ' ']

SEMICOLON = ';'
COMMA = ','
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
            return True
        else:
            return False

    def nextState(self, input):  # transition table에서 입력하나 보고 간 state,
        items = self.Delta[self.state].items()
        posNext = dict()
        for key, value in items:
            if value != "" :
                posNext[key] = value

        keys = posNext.keys()
        print("keys",keys)
        for i in keys :
            if input in i :
                newKey = i

        if newKey in posNext :
            nextState = posNext[newKey]
        print(nextState)
        self.state = nextState
        return 0
        
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
        return

    def transition(self, table):
        delta = {}
        for T in self.Q:
            delta[T]={}
            i = 0
            self.Delta.update({str(T): {}})
            for alphabet in self.Sigma:
                #print("**")
                #print(str(T), "/", alphabet, "/", table[str(T)][i])
                delta[str(T)][str(alphabet)]=table[str(T)][i]
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
    ["r", "e", "t", "u", "r", "n"],  # input stream
    ["T6"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "", "", "", "", ""],
        "T1": ["", "T2", "", "", "", ""],
        "T2": ["", "", "T3", "", "", ""],
        "T3": ["", "", "", "T4", "", ""],
        "T4": ["", "", "", "", "T5", ""],
        "T5": ["", "", "", "", "", ""]
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
    ["\"", str(DIGIT), str(DIGIT), str(BLANK)],  # input stream
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
print("!!~!!",Integer.Sigma)

class Scanner:
    # Token Definition

    ALPHABET = LETTER + DIGIT + WHITESPACE

    def __init__(self, input_string):
        self.input_string = input_string
        self.next_string = input_string

    def dfa_identifier(self, next_string):
        symbol = [self.LETTER, self.DIGIT, '_']

        final = [1, 2, 3, 4, 5]
        transition_table = [[1, -1, 2], [3, 4, 5], [3, 4, 5], [3, 4, 5], [3, 4, 5], [3, 4, 5]]

        # state
        i = 0

        id_string = ""
        # analyze
        for put in next_string:
            if put in symbol[0]:
                j = 0
            elif put in symbol[1]:
                j = 1
            elif put in symbol[2]:
                j = 2
            else:
                if len(id_string) > 0:
                    print("Identifier", id_string)
                    self.next_string = next_string.replace(id_string, '')
                    return True
                else:
                    return False

            tmp_i = i
            i = transition_table[i][j]
            id_string += put

            if i == -1:
                return False

        if i in final:
            print("Identifier", id_string)
            return True
        else:
            return False

    def dfa_blank(self, next_string):
        symbol = self.BLANK

        if next_string[0] == symbol:
            self.next_string = next_string[1:]
            print("Blank ", " ")
            return True
        else:
            return False

    def dfa_comma(self, next_string):
        symbol = self.COMMA

        if next_string[0] == symbol:
            self.next_string = next_string[1:]
            print("Comma ", ",")
            return True
        else:
            return False

    def dfa_semicolon(self, next_string):
        symbol = self.SEMICOLON

        if next_string[0] == symbol:
            self.next_string = next_string[1:]
            print("Semicolon ", ";")
            return True
        else:
            return False

inputs = "1"

MERGED1 = [Integer]

#print(MERGED[0].Delta)
#print("----------------------------------")
#print(type(inputs[0]))
#print(type(inputs))
# print(MERGED[0])
# next = MERGED[0].nextState('1')
# MERGED[0].moveState(next)
# print(MERGED[0].isAccepted())
# print(MERGED[0].currentState(next))
# print(MERGED[0].acceptedToken())
# MERGED[0].clear()

table = {}
text1 = "-123"
textState = 1
mIdx=0
for textState in range(len(text1)): #try catch랑 겹치는?
    try:
        mIdx = textState
        if text1[mIdx] in OPERATOR or text1[0] in DIGIT : #text1[textState]
            for i in range(len(MERGED1)) :
                print("$$")
                while MERGED1[i].isIng == 1 :
                    MERGED1[i].nextState(text1[textState]) #text1[textState]
                    textState += 1
                    print("textState:", textState)
                    print("accept:",MERGED1[i].isAccepted())
                    #한 단어? 앞 뒤로 화이트 스페이스가 있는 건지
                    #글자.
                    #오토마타 -> 한 글자가 Sigma가 들었는지, 들어있으면
                    #isIng == 0, Sigma에 없으면 -> 현재 상태가 final이면 accepted
                    #Sigma에는 있는데 isIng == 1,
                        #nextState로 안 넘어갈 때 inIng == 0  
                    if textState >= len(text1):
                        MERGED1[i].isIng = 0

                    #Ing 바뀌는 부분
                if MERGED1[i].isAccepted():
                    print("@")
                    subStr = text1[mIdx:textState]
                    print()
                    table[subStr] = MERGED1[i].acceptedToken()
                    print(subStr)
                    break
                else:
                    textState = mIdx
    except IndexError:
        print("there is no more input");

print("table:",table)
    
    #mIdx = textState
    #textState = mIdx+1
    
    
text2 = "1a"
