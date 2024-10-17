class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'

    def process_input(self, input_string):
        self.stack = ['Z0']
        self.state = 'q0'
        index = 0

        while index < len(input_string):
            symbol = input_string[index]

            if self.state == 'q0':
                if symbol == 'a':
                    self.stack.append('X')
                    index += 1
                elif symbol == 'b':
                    if self.stack and self.stack[-1] == 'X':
                        self.stack.pop()
                        index += 1
                    else:
                        return False  # Error: más b's que a's
                elif symbol == 'c':
                    if self.stack == ['Z0']:
                        self.state = 'q1'
                        # No incrementamos index aquí
                    else:
                        return False  # Error: a's y b's no balanceados
                else:
                    return False  # Símbolo inválido en q0

            elif self.state == 'q1':
                if symbol == 'c':
                    self.stack.append('X')
                    index += 1
                elif symbol == 'd':
                    if self.stack and self.stack[-1] == 'X':
                        self.stack.pop()
                        index += 1
                    else:
                        return False  # Error: más d's que c's
                else:
                    return False  # Símbolo inválido en q1

            else:
                return False  # Estado inválido

        # Verificar aceptación
        if self.state == 'q1' and self.stack == ['Z0']:
            return True
        else:
            return False


# Ejemplos de uso:
pda = PDA()

# Cadenas aceptadas:
print(pda.process_input('aaabbbccddd'))  
print(pda.process_input('abcd'))         
print(pda.process_input('aabbccdd'))     

# Cadenas no aceptadas:
print(pda.process_input('aabbbccdd'))   
print(pda.process_input('aabbccddd'))   
print(pda.process_input('abccdd'))       
