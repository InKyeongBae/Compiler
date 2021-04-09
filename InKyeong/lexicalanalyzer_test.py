import sys

#file I/O
f = open(sys.argv[1],'r')
input = f.readlines()
filename = sys.argv[1]
# 일단 txt로 나오게 추후에 out으로 수정
file_out = open(f"{filename.replace('.java', '')}.txt",'w')

# 일단 input 내용 그대로 out으로 나오도록
for input in input :
    file_out.write(input + "\n")

def filewrite(file, string):
    print(string)
    file.write(string+"\n")


f.close()




####################################################################
def process(self, input):
    for input in input:

        # input 문자가 알파벳(시그마)이 아닐 때
        if input not in self.Sigma:
            print(f'{self.Q}|{input}: undefined alphabet')
            self.isIng = 1
            ## 끝남
            return self.isIng

        # automata가 이미 끝났을 때
        if self.isIng == 1:
            print(f'{self.Q}|{input}: automata dead')
            return self.isIng

        # find transition function with state and input character
        # for transition_function in self.transition_functions:
        #     if transition_function[0] == self.state and char in transition_function[1]:
        #         # do state transition
        #         self.state = transition_function[2]
        #         # print(f'{self.name}|{transition_function[0]} ---{char}---> {"("+str(self.state)+")" if self.isfinal() else self.state}')
        #         return self.life
        # # transition function not found: halt
        # else:
        #     # print(f'{self.name}|{char}: function undefined')
        #     self.life = Life.DEAD
        #     return self.life


# automata가 중단되지 않았는데 final state 일 때
def isFinal(self):
    is_final = self.state in self.F and self.isIng == 0
    print(is_final)
    return is_final


# state setter
# ex. stateSetter("T1")
def stateSetter(self, state):
    self.state = state
    self.isIng = 0


# 여러 개 중에 하나 고르는 형태
def choiceOne(lexemes):
    # lexemes == ['int', 'float', 'boolean', 'String'] 이런 꼴

    charlist = ""
    # 하나하나 뜯어놓기 -> alphabet == {'i', 'n', 't', 'f', 'l', 'o',,   ,, 'g'}
    for explist in lexemes:
        for char in explist:
            charlist += char
    alphabet = set(charlist)
    # initialize dfa
    # alphabet, transition_functions, initial_state, final_states
    # states, alphabet, finalState
    result = FiniteAutomata(alphabet, list(), list())

    state_index = 1
    for word in lexemes:
        # from starting state to first character state
        result.transition_functions.append((0, word[0], state_index))

        # from first character state to final character state
        for char in word[1:]:
            result.transition_functions.append((state_index, char, state_index + 1))
            state_index += 1
        # final character state would be the accepting state
        result.final_state.append(state_index)
        state_index += 1

    return result

    def matching_dfa(lexemes):
        # flatten list and generate alphabet
        alphabet = set(item for sublist in lexemes for item in sublist)
        # initialize dfa
        result = DFA(alphabet, list(), 0, list())

        state_index = 1
        for word in lexemes:
            # from starting state to first character state
            result.transition_functions.append((0, word[0], state_index))

            # from first character state to final character state
            for char in word[1:]:
                result.transition_functions.append((state_index, char, state_index + 1))
                state_index += 1
            # final character state would be the accepting state
            result.final_state.append(state_index)
            state_index += 1

        return result