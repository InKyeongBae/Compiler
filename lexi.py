import Queue 
#lexical specificatons
#Token
DIGIT=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 


#input stream -대소문자 처리 어떻게 할지. 파일 입출력
input = Queue.Queue()

#lexeme

# mIndex = 0;
# for 1<= i <= n:
#     if input is in L(Merged): #ERORR HANDLING-> FINITE AUTOMATA -> Accept or NOT
#       mIndex = i 
# partition and classify substring


#NFA-thompson construction

#DFA (in the form of transition table)
class FiniteAutomata(): #Finite Automata for NFA, DFA    
    F = []
    Sigma = []
    #q0 = []
    state = 0
    Q = []
    Delta = []
    def __init__(self, states, alphabet, finalState, transition): #startState
        self.Q = states #list(map(str, Q))
        self.Sigma = list(map(str, alphabet))
        #self.q0 = startState #list(map(str, q0))
        self.state = "T0"
        self.F = finalState #list(map(str, F))
        self.Delta = transition #nfa2dfa
       
        # def transitionTable(self, nfa2dfa):
        #     self.Delta = nfa2dfa

    def isAccepted(self):
        if self.state in self.F:
            return True
        else:
            return False

#Reugular expressions 이부분은 구현하지 않는거고, DFA가 같은 효과인가?
#INT=((-|e)*Digit[1:]DIGIT*|0) #?->finite automata
Integer = FiniteAutomata(
    ["T0", "T1", "T2", "T3", "T4"],
    ["-", 0, DIGIT[1:], DIGIT],
    ["T2", "T3", "T4"]
    {
        "T0": {"-":"T1", 0:"T2", DIGIT[1:]:"T3", DIGIT:""},
        "T1": {"-":"", 0:"", DIGIT[1:]:"T3", DIGIT:""},
        "T2": {"-":"", 0:"", DIGIT[1:]:"", DIGIT:""},
        "T3": {"-":"", 0:"", DIGIT[1:]:"", DIGIT:"T4"},
        "T4": {"-":"", 0:"", DIGIT[1:]:"", DIGIT:"T4"},
    }
)

#Merge ? 어케하지 -token 우선순위 만들기 

#dfa transition table 정의 
dfa = FiniteAutomata()
#accepted?
#state에 따른 token 종류

#Draw Token table
map<name, value>