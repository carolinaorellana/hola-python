# 1. TAREA: imprime "Hola, mundo"
print("Hola Mundo")
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Carolina"
print("Hola",name)	# con una coma
print("hola "+ name)	# con un +
# 3. imprimir "Hola 42!" con el número en una variable
num1 = 27
print("Hola", num1,"!" )	# con una coma
print("Hola " + str(num1)+"!")	# con una +	-- este debería arrojar un error!


# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "Amo comer {} y {}".format(fave_food1,fave_food2)) # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}") # con una cadena f

# Experimentar
print (fave_food2.upper()) #uppercase
print(fave_food2.isalnum()) #alfanumerico true, si tiene espacio o punto false.

variableChar = "Hola me llamo Carolina"
print(variableChar.split()) #por defecto es el espacio
print(variableChar.split("o")) # que la divida cuando sale la o, este caracter lo elimina
print(variableChar.split("a"))