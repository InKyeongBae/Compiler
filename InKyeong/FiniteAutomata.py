
class FiniteAutomata() :
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

    ALPHABET = LETTER + DIGIT  + WHITESPACE

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


