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
                print("**")
                print(str(T), "/", alphabet, "/", table[str(T)][i])
                delta[str(T)][str(alphabet)]=table[str(T)][i]
                i = i + 1
        return delta


# Regular expressions 이부분은 구현하지 않는거고, DFA가 같은 효과인가?
# INT=((-|e)*Digit[1:]DIGIT*|0) #?->finite automata

Integer = FiniteAutomata(
    "INTEGER",  # matched token name
    ["T0", "T1", "T2", "T3", "T4"],  # state
    ["-", 0, POS_DIGIT, DIGIT],  # input stream
    ["T2", "T3", "T4"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1", "T2", "T3", ""],
        "T1": ["", "", "T3", ""],
        "T2": ["", "", "", ""],
        "T3": ["", "", "", "T4"],
        "T4": ["", "", "", "T4"]
    }
)



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


text1 = "-123"
textState = 0
if text1[textState] in OPERATOR or text1[0] in DIGIT :
    for i in range(len(MERGED1)) :
        while MERGED1[i].isIng == 1 :
            MERGED1[i].nextState(text1[textState])
            textState += 1


text2 = "1a"
