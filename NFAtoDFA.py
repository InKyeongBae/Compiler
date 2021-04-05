#오토마타와 형식언어 03분반 20190192 좌민주
eps = '#'

def Delta (state1, num, state2): #delta 생성
    delta = {'curr_state': state1, 'input': str(num), 'next_state': state2}
    return delta

class FA(): #Finite Automata for NFA, DFA, eNFA    
    Q = []
    Sigma = []
    q0 = []
    F = []
    Delta = []
    def __init__(self, Q, Sigma, q0, F, Delta):
        self.Q = Q #list(map(str, Q))
        self.Sigma = list(map(str, Sigma))
        self.q0 = q0 #list(map(str, q0))
        self.F = F #list(map(str, F))
        self.Delta = Delta
    
    def State_2Q(self, states): #DFA를 위한 함수 -> 나중에 파이썬 상속을 배우면 DFA 클래스에만 넣어서 코드를 정리하고 싶습니다
        #모든 상태 2^Q를 구함
        if(isinstance(states, list)):
            for s in states :
                self.Q.append(s)
        else :
            self.Q.append(states)
        
        #모든 상태로부터 final state를 구함
        final = self.F.pop()
        for f in self.Q:
            if final in f :
                self.F.append(f)
                    
    def Closure(self, state, input):
        
        stack = []
        closure = []
        State = []

        #list에 있는 입력이 list인지, 문자인지 판별하며 state를 모두 문자로 재구성함
        if(isinstance(state, list)):
            for s in state :
                if(isinstance(s, list)):
                    for _s in s :
                        State.append(_s)
                else : 
                    State.append(s) 
        else :
            State.append(state)

        #입력을 보고 갈 수 있는 상태 -closure의 부분집합      
        while State :
            S = State.pop()
            for d in self.Delta :
                if S == d['curr_state'] and d['input']  == input:
                    #list인지 판별
                    if(isinstance(d['next_state'], list)):
                        for s in d['next_state']:
                            closure.append(s)
                            stack.append(s)
                    else :
                        closure.append(d['next_state'])
                        stack.append(d['next_state'])
        #epsilon을 보고 갈 수 있는 상태 포함-closure가 완성됨
        while stack:
            S = stack.pop()
            for s in S:
                for d in self.Delta :
                    if s == d['curr_state'] and d['input']  == eps:
                        #list인지 판별
                        if(isinstance(d['next_state'], list)):
                            for s in d['next_state']:
                                closure.append(s)
                                stack.append(s)
                        else :
                            closure.append(d['next_state'])
                            stack.append(d['next_state'])
        return closure

    #dfa를 위한 드라이버
    def Driver(self, language):
        language = list(language)
        s = self.q0
        for i in language :
            for d in self.Delta :
                if s == d['curr_state'] and d['input']  == i:
                    s = d['next_state']
                    break
        if s in self.F :
            print("Accept")
        else :
            print("Reject")

    #nfa를 위한 드라이버
    #nfa를 위한 드라이버를 만들면서 nfa를 dfa로 변환시켜서 accept인지 reject인지 판별하는 것과 유사하다 느꼈다.
    #여기서 while s 부분이 subset construction을 구하는 과정과 유사했기 때문이다.
    def Driver_nfa(self, language):
        language = list(language)
        state = self.q0    
        for i in language :
            s = list(state)
            state.clear()
            while s :
                S = s.pop()
                for d in self.Delta :
                    if S == d['curr_state'] and d['input']  == i:
                        if(isinstance(d['next_state'], list)):
                            for _S in d['next_state']:
                                state.append(_S)
                        else :
                            state.append(d['next_state'])
        for s in state :
            if s in self.F :
                print("Accept")
                return

        print("Reject")

    #FA를 출력
    def print_FA(self):
        print("Here, closure{} is represented as [] ")
        print("Q:", self.Q)
        print("Sigma:", self.Sigma)
        print("q0:", self.q0)
        print("F:", self.F)
        print("Delta")
        for d in self.Delta :
            print("Delta", "(", d['curr_state'], ",", d['input'], ") = ", d['next_state'])


#eNFA in Slide 23 (ch.3)
eNFA = FA(['A', 'B', 'C', 'D', 'E', 'F'],
    [0, 1], ['A'], ['D'], [
    Delta('A', 0, 'E'),
    Delta('A', 1,'B'), 
    Delta('B', 1, 'C'), 
    Delta('B', eps, 'D'),
    Delta('C', 1, 'D'),
    Delta('E', 0, 'F'),
    Delta('E', eps, ['B', 'C']),
    Delta('F', 0, 'D'),
])
print("\n***epsilon-NFA***")
eNFA.print_FA()

#DFA for eNFA
DFA_for_eNFA = FA([], eNFA.Sigma, eNFA.q0, eNFA.F, [])

marked = []
unmarked = []
CL_q0 = eNFA.Closure(eNFA.q0, eps)
#시작 상태의 closure을 구함
if not CL_q0 : 
    unmarked.append(eNFA.q0)
else :
    unmarked.append(CL_q0)

#subset construction (closure 알고리즘 포함)
while unmarked:
    state = unmarked.pop()
    if state in marked:
        continue
    else :
        marked.append(state)
    for i in eNFA.Sigma :
        closure = eNFA.Closure(state, i) #closure 알고리즘
        if not closure : 
            continue
        if not closure in marked :
            unmarked.append(closure) 
        DFA_for_eNFA.Delta.append(Delta(state, i, closure))

DFA_for_eNFA.State_2Q(marked)
print("\n***DFA for e-NFA***")
DFA_for_eNFA.print_FA()
#입력 문자열을 받아 accept/reject 여부 검증
#입력을 보고 갈 수 있는 상태가 없다면 (델타에 없는 규칙의 입력이라면) 현재 삳태에 머무른다.
#예를 들어, 현재 상태가 A이고 2를 받는다면 현재 상태는 2이다. 111이 accept한 언어라면 2111도 accept하게 처리하였다.
user1 = input("\n>>>input your language ")
print(user1)
DFA_for_eNFA.Driver(user1)
#DFA_for_eNFA.Driver("111")

#주어진 NFA에 입력 문자열을 받아 판별해보기
#nfa in slide 18 (ch.3)
NFA = FA([0, 1, 2, 3], ['a', 'b'], [0], [3], [
    Delta(0, 'a', [0, 1]),
    Delta(0, 'b', 0),
    Delta(1, 'b', 2),
    Delta(2, 'b', 3)
])
print("\n***NFA***")
NFA.print_FA()
user2 = input("\n>>>input your language ")
print(user2)
NFA.Driver_nfa(user2)

