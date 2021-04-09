# DFA (in the form of transition table)
class FiniteAutomata():  # Finite Automata for NFA, DFA
    F = {}
    Sigma = []
    # q0 = []
    state = 0
    Q = []
    Delta = {}
    isIng = 0

    def __init__(self, states, alphabet, finalState):  # startState
        self.Q = states  # list(map(str, Q))
        self.Sigma = alphabet  # list(map(str, alphabet))
        # self.q0 = startState #list(map(str, q0))
        self.state = "T0"
        self.F = finalState  # list(map(str, F))
        # self.Delta = transition #nfa2dfa


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

    def moveState(self, nextstate):  # state update하기
        return

    def acceptedToken(self):  # if accepted or not
        return self.F[self.state]

    def clear(self):  # 재사용하게 reset
        return


    def transitionTable(self, table):
        for T in self.Q:
            i = 0
            self.Delta.update({str(T): {}})
            for alphabet in self.Sigma:
                # print("**")
                # print(str(T), "/", alphabet, "/", table[str(T)][i])
                self.Delta[str(T)][str(alphabet)] = table[str(T)][i]
                i = i + 1







IntegerTable = {
    "T0": ["T1", "T2", "T3", ""],
    "T1": ["", "", "T3", ""],
    "T2": ["", "", "", ""],
    "T3": ["", "", "", "T4"],
    "T4": ["", "", "","T4"]
}

DIGIT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Reugular expressions 이부분은 구현하지 않는거고, DFA가 같은 효과인가?
#INT=((-|e)*Digit[1:]DIGIT*|0) #?->finite automata
Integer = FiniteAutomata(
    ["T0", "T1", "T2", "T3", "T4"], #이거 쓸라나?
    ["-", 0, DIGIT[1:], DIGIT], #얘도 쓸라나?
    {"T2":"INTEGER", "T3":"INTEGER", "T4":"INTEGER"} #accepetd token name

) #dfa transition table 정의



Integer.transitionTable(IntegerTable)

# Integer.nextState('-')
# F = {}
#     Sigma = []
#     # q0 = []
#     state = 0
#     Q = []
#     Delta = {}
#     isIng = 0
print("F(finalstate) :", Integer.F)
print("Sigma(alphabets) :",Integer.Sigma)
print("state(Initialstate) :",Integer.state)
print("Q(possible states) :",Integer.Q)
print("Delta(이동가능) :",Integer.Delta)
print("isIng :",Integer.isIng)

text1 = "-123"
text1[0]
text2 = "1a"





