# Input Definition
TYPE = ['int', 'char', 'boolean', 'String']
BOOLEAN = ['true', 'false']
OPERATOR = ['-', '+', '*', '/']
WHITESPACE = ['\t', '\n', ' ']
COMMA = [',']
SEMICOLON = [';']
LBRACE = ['{']
RBRACE = ['}']
LPAREN = ['(']
RPAREN = [')']
LARRAY = ['[']
RARRAY = [']']

# Alphabet Definition
LETTER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
          'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']
DIGIT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
POS_DIGIT = DIGIT[1:]
BLANK = [' ']

class FiniteAutomata:  # Finite Automata for DFA
    tokenName = ""
    F = {}      # a set of final(or accepting) states
    Sigma = []  # a finite set of input symbols
    state = 0  # a start state q0
    Q = []  # a finite set of states
    Delta = {}  # a set of state transition functions
    isIng = 1  # a flag that saves FA is working

    def __init__(self, token, states, alphabet, final, table):
        self.tokenName = token
        self.Q = states
        self.Sigma = alphabet
        self.state = "T0"
        self.F = final
        self.Delta = self.transition(table)

    def isAccepted(self):  # return true when current lexeme is matched with this token
        if self.state in self.F:
            return True
        else:
            return False

    def checkIng(self, input):  # check the input is in the token's alphabet
        isAlpha = 0  # flag: is in alphabet
        for i in self.Sigma:
            if input not in i:  # not an element
                isAlpha = 0
            elif input == ' ':  # to distinguish input with WHITESPACE lexeme
                isAlpha = 0
            else:               # included in alphabet
                isAlpha = 1
                break

        if isAlpha == 0:
            # print(f'{input}: undefined alphabet')
            self.isIng = 0
        else:
            # print(f'{input}: defined alphabet')
            self.isIng = 1

        if self.isIng == 0:
            # print(f'{input}: automata dead')
            return self.isIng
        else:
            return self.isIng

    def wscheckIng(self, input):  # to check the blank is WHITESPACE lexemes
        isAlpha = 0
        for i in self.Sigma:
            if input not in i:
                isAlpha = 0
            else:
                isAlpha = 1  # if the token is WHITESPACE
                break
        if isAlpha == 0:
            # print(f'{input}: undefined alphabet')
            self.isIng = 0
        else:
            # print(f'{input}: defined alphabet')
            self.isIng = 1

        if self.isIng == 0:
            # print(f'{input}: automata dead')
            return self.isIng
        else:
            return self.isIng

    def nextState(self, input):  # look transition table and move to nest state
        items = self.Delta[self.state].items()
        posNext = dict()
        for key, value in items:
            if value != "":
                posNext[key] = value
        keys = posNext.keys()
        newKey = ""
        inputStr = ""

        for i in keys:
            if len(i) > 1:
                i = i.strip('][').replace("'", "").split(', ')
            if input in i:
                newKey = str(i)

        if newKey in posNext:
            nextState = posNext[newKey]
        else:
            self.isIng = 0
            return self.isIng
        self.state = nextState
        return self.isIng

    def moveState(self, next_state):  # update state
        self.state = next_state

    def currentState(self, next_state):  # get currentState
        return self.state

    def acceptedToken(self):  # get token name
        if self.state in self.F:
            return self.tokenName
        else:
            return "Not Accepted"

    def clear(self):  # clear to reuse the automata
        self.state = "T0"
        self.isIng = 1
        return

    def transition(self, table):  # transition table
        delta = {}
        for T in self.Q:
            delta[T] = {}
            i = 0
            self.Delta.update({str(T): {}})
            for alphabet in self.Sigma:
                delta[str(T)][str(alphabet)] = table[str(T)][i]
                i = i + 1
        return delta


# Finite Automata Definitions with transition table
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
    [str(COMMA)],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Semicolon = FiniteAutomata(
    "SEMICOLON",  # matched token name
    ["T0", "T1"],  # state
    [str(SEMICOLON)],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Lbrace = FiniteAutomata(
    "LBRACE",  # matched token name
    ["T0", "T1"],  # state
    [str(LBRACE)],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Rbrace = FiniteAutomata(
    "RBRACE",  # matched token name
    ["T0", "T1"],  # state
    [str(RBRACE)],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Lparen = FiniteAutomata(
    "LPAREN",  # matched token name
    ["T0", "T1"],  # state
    [str(LPAREN)],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Rparen = FiniteAutomata(
    "RPAREN",  # matched token name
    ["T0", "T1"],  # state
    [str(RPAREN)],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Larray = FiniteAutomata(
    "LARRAY",  # matched token name
    ["T0", "T1"],  # state
    [str(LARRAY)],  # input stream
    ["T1"],  # accepted state
    {  # nfa to dfa transition table
        "T0": ["T1"],
        "T1": [""]
    }
)

Rarray = FiniteAutomata(
    "RARRAY",  # matched token name
    ["T0", "T1"],  # state
    [str(RARRAY)],  # input stream
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