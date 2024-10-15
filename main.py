import json



# path = input('Por favor ingresar el camino del archivo.json (ej.  ./lenguaje.json )\n')

path = 'lenguaje.json'
with open(path, 'r') as file:
    data = json.load(file)

# Extract states and symbols
estados = data['ESTADOS']  # Treat states as literal strings
alf_entrada = data['ALF_ENTRADA']
alf_pila = data['ALF_PILA']  # Start state as a literal string
aceptacion = data['F']  # Acceptance states as literal strings
transiciones = data['TRANSICIONES']
state_inicial = data['ESTADO_INICIAL']  # Start state as a literal string
simb_inicial = data['SIMBOLO_INICIAL']  # Acceptance states as literal strings


cadena = input('Ingresa la cadena deseas probar\n')



stack = ['Z0']


no_function  = True

for i in cadena:
    done = True
    contadormain = 0
    while done or contadormain < (len(transiciones)-1):
        o = transiciones[contadormain]
        contadormain = contadormain + 1
        
        two_trans = o.split('=')
        first_trans = two_trans[0].split(',')
        if (state_inicial in first_trans[0]) and (first_trans[1] == i) and (stack[len(stack)-1] in first_trans[2] ):
            to_transition = two_trans[1].strip("()")
            to_transition = to_transition.split(',')
            stack.pop()
            
            if( 'Z0' in to_transition[1]):
                to_transition[1] = to_transition[1].replace( 'Z0', '$' )
            
            datos_ameter = (list(to_transition[1]))
            
            if datos_ameter[0] == 'e':
                datos_ameter = []
                
            
            stack = stack + datos_ameter[::-1]
            state_inicial = to_transition[0].strip(" (")
            
            contador = 0
            done = False
            contadormain = len(transiciones)+ 2
            
            while len(stack) > contador:
                if stack[contador] == '$':
                    stack[contador] = 'Z0'
                contador = contador + 1
                
        if contadormain == (len(transiciones)-1):
            contadormain = contadormain + 5
            done = False
            no_function = False
            print('Funcion de transición no encontrada')
            print( 'Valor actual', i )
            print( 'Estado', state_inicial )
            print( 'Stack', stack)
                       

           
aceptacion = False 
done = True
contadormain = 0
while done or contadormain < (len(transiciones)-1):
    o = transiciones[contadormain]
    contadormain = contadormain + 1
    two_trans = o.split('=')
    first_trans = two_trans[0].split(',')
    to_transition = two_trans[1].split(',')
    
    if (state_inicial in first_trans[0]) and (first_trans[1] == 'e') and (stack[len(stack)-1] in first_trans[2] ) and no_function == True:
        aceptacion = True
        contadormain = len(transiciones) + 2
        done = False
        
        state_inicial = to_transition[0].strip(" (")
    
    if contadormain == (len(transiciones)):
        done = False
        print(stack)
        print(state_inicial)
        

if no_function:
    if aceptacion:
        alf_dict = {key: 0 for key in alf_entrada}
        for i in cadena:
            alf_dict[i] = alf_dict[i] + 1
        
    
        
        print('cadena aceptada', cadena)
        print( 'Lenguaje aceptada por la cadena   '  + str('0^' + 'm') + ' ' +str('1^'+ '(m' )+ '+' +str( alf_dict['1'] - alf_dict['0'] ) + ')' + ' | ' + 'm ≥ 1'   )
        print( 'Estado actual',state_inicial)
        print( 'Stack', stack)
    else:
        print('Cadena no aceptada')
        
        print(state_inicial)
        print(stack)
else: 
    print('Cadena no aceptada')
    print(state_inicial)
    print(stack)
    