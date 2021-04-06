# DFA (in the form of transition table)
class FiniteAutomata():  # Finite Automata for NFA, DFA
    F = {}
    Sigma = []
    # q0 = []
    state = 0
    Q = []
    Delta = {}

    def __init__(self, states, alphabet, finalState, transition):  # startState
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
        nextstate = self.Delta[self.state][input]

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
                print("**")
                print(str(T), "/", alphabet, "/", table[str(T)][i])
                self.Delta[str(T)][str(alphabet)] = table[str(T)][i]
                i = i + 1

IntegerTable = {
    "T0": ["T1", "T2", "T3", ""],
    "T1": ["", "", "T3", ""],
    "T2": ["", "", "", ""],
    "T3": ["", "", "", "T4"],
    "T4": ["", "", "","T4"]
}

#Reugular expressions 이부분은 구현하지 않는거고, DFA가 같은 효과인가?
#INT=((-|e)*Digit[1:]DIGIT*|0) #?->finite automata
Integer = FiniteAutomata(
    ["T0", "T1", "T2", "T3", "T4"], #이거 쓸라나?
    ["-", 0, DIGIT[1:], DIGIT], #얘도 쓸라나?
    {"T2":"INTEGER", "T3":"INTEGER", "T4":"INTEGER"} #accepetd token name

) #dfa transition table 정의

Integer.transitionTable(IntegerTable)


class FiniteAutomata2() :
    # Token Definition
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
    POSDIGIT = DIGIT[1:]

    ALPHABET = LETTER + DIGIT + WHITESPACE

    def __init__(self, input_string):
        self.input_string = input_string
        self.next_string = input_string


    def dfa_identifier(self, next_string):
        symbol = [self.LETTER, self.DIGIT, '_']

        final = [1, 2, 3, 4, 5]
        transition_table = [[1, -1, 2], [3, 4, 5], [3, 4, 5], [3, 4, 5], [3, 4, 5], [3, 4, 5]]

        #state
        i = 0

        id_string = ""
        #analyze
        for put in next_string:
            if put in symbol[0]:
                j = 0
            elif put in symbol[1]:
                j = 1
            elif put in symbol[2]:
                j = 2
            else:
                if len(id_string) > 0 :
                    print("Identifier", id_string)
                    self.next_string = next_string.replace(id_string, '')
                    return True
                else :
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

        if next_string[0] == symbol :
            self.next_string = next_string[1:]
            print("Blank ", " ")
            return True
        else :
            return False

    def dfa_comma(self, next_string):
        symbol = self.COMMA

        if next_string[0] == symbol :
            self.next_string = next_string[1:]
            print("Comma ", ",")
            return True
        else :
            return False

    def dfa_semicolon(self, next_string):
        symbol = self.SEMICOLON

        if next_string[0] == symbol :
            self.next_string = next_string[1:]
            print("Semicolon ", ";")
            return True
        else :
            return False


