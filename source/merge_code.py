from collections import deque

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

inputs = "1"

MERGED1 = [Integer]

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
text1 = deque("123!1")

textState = 0
while len(text1) > 0:
    if text1[textState] in OPERATOR or text1[0] in DIGIT:
        for i in range(len(MERGED1)):
            # print("Initial state :", MERGED1[i].state)
            # print("isIng :", MERGED1[i].isIng)
            while textState < len(text1) and MERGED1[i].checkIng(text1[textState]) == 1:
                # print(text1[textState])
                MERGED1[i].nextState(text1[textState])
                # print("state :", MERGED1[i].state)
                # print("isIng :", MERGED1[i].isIng)
                if MERGED1[i].isIng == 1:
                    textState += 1
                else:
                    break
                # print("!!!!!!", textState)

            if MERGED1[i].isAccepted():
                subStr = ""
                for _ in range(textState):
                    subStr += text1.popleft()
                table.append([MERGED1[i].acceptedToken(), subStr])
                textState = 0
            else:
                i += 1
                textState = 0

    elif text1[textState] == '!':
        subStr = ""
        subStr += text1.popleft()
        table.append(["TYPE", subStr])
        textState = 0

print("table:", table)






