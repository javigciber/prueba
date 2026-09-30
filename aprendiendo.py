validoedad = False

while validoedad == False:
	try:
	    edad= int( input( "Cuantos años tienes?  "))
	    validoedad = True
	
	except: 
	       print("Eso no es un numero")
if edad >= 18:
	print(f"Tienes {edad} años")
	print(f"Acceso permitido")
else:
	print(f"Tienes {edad} años")
	print(f"Acceso denegado")
