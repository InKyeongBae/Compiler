#lexical specificatons
#Token
from enum import EnumMeta
#class digit(Enum):
DIGIT=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

#변수명 구림 주의※
# #input stream -대소문자 처리 어떻게 할지
input = ['123', '234'] #queue로 appned, pop -> pop 마지막이 입력 끝

def readProgram(input): # 파일 입출력
    while lexeme in input: #파일 전체
        subString = list(lexeme) #파일  한출
        for i in subString: # [1, 2, 3]
            if input in Merged: #ERORR HANDLING-> FINITE AUTOMATA -> Accept or NOT
                temp = mIndex
                mIndex = i
            #transition table에 넣기 
        #partition and classify substring

#lexeme

#NFA-thompson construction -> transition table

#DFA (in the form of transition table)
class FiniteAutomata(): #Finite Automata for NFA, DFA    
    F = {}
    Sigma = []
    #q0 = []
    state = 0
    Q = []
    Delta = {}
    def __init__(self, states, alphabet, finalState, transition): #startState
        self.Q = states #list(map(str, Q)) 
        self.Sigma = alphabet#list(map(str, alphabet))
        #self.q0 = startState #list(map(str, q0))
        self.state = "T0"
        self.F = finalState #list(map(str, F))
        #self.Delta = transition #nfa2dfa

    def isAccepted(self):
        if self.state in self.F:
            return True
        else:
            return False
    
    def nextState(self, input): #transition table에서 입력하나 보고 간 state,
        nextstate = self.Delta[self.state][input]

    def moveState(self, nextstate): # state update하기
        return 

    def acceptedToken(self): #if accepted or not
        return self.F[self.state]
    
    def clear(self): #재사용하게 reset
        return
    
    def transitionTable(self, table):
        for T in self.Q:
            i = 0
            self.Delta.update({str(T):{}})
            for alphabet in self.Sigma:
                print("**")
                print(str(T),"/", alphabet, "/",table[str(T)][i])
                self.Delta[str(T)][str(alphabet)] = table[str(T)][i]
                i = i + 1

Integer = {
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



# if input in DIGIT:
#     state: T3

#accepted?
#state에 따른 token 종류

#ERROR REPORT

#Merge ? 어케하지 
Merged = [Integer] #, Literal, Relop, ... #class로 ?

#반복 -.> accepted? -token 우선순위 만들기 
def travle(input, Merged):
    for token in Merged:
        token.nextState(input)
    #moveState
    
#Draw Token table
class SymbolTable:
    
    table = []#"token name": , "token value": 
    def putLexemes(self, name, lexme): #token name, value 넣기 
        self.table.append({"name": name,"value": lexme})
    def write2file(self): #파일에 그리기
        return

symbolTable = SymbolTable()

if __name__ == "__main__":
    #state = Integer.nextState('1')
    #print(Integer.acceptedToken(state))
    # mIndex = 0;
    Integer.transitionTable(table) #
    print(Integer.Delta)

    #test()
    #rep 
