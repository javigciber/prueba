validoedad = False

while validoedad == False:
	try:
	    edad= int( input( "Cuantos años tienes?  "))
	    validoedad = True
	    print(f" Tienes {edad} años")
	
	except: 
	       print("Eso no es un numero")
