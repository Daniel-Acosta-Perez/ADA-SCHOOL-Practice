"""Daniel Acosta Perez"""
#? 1. 
# Define variables de cada tipo primitivo

integer = 10
float = 10.5  
bool = True
string = "Ada_School"

# El límite de los enteros en Python es sys.maxsize, que es 2^63 - 1 en una máquina de 64 bits
# El límite de los floats es aproximadamente 1.8e308
""" Bibliografia: 
    https://realpython.com/python-data-types/
    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
    """

#? 2. 
# Concatena las variables a la cadena

resultado = string + str(integer) + str(float) + str(bool) 


#? 3. 
# Fórmula suma de los primeros n números pares
# La fórmula es n*(n+1)

n = integer 
sumatoria = n*(n+1)


#? 4. 
# Imprime los resultados
print(resultado)
print(suma)