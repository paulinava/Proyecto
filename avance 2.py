#personas que tienen acesso a las instalaciones
print ("Personas con acesso a las instalaciones")
print ("Directivos")
print ("Trabajadores turno matutino")
print ("Trabajadores turno vespertino")
print ("Socios")
print ("Seguridad")

Pase_libre = True
Directivos = True
Traba_TM = True
Traba_TV = True
Socios = True
Seguridad = True
Entradas = 0

if Directivos:
    Entradas = Entradas + 1
elif Pase_libre:
    Entradas = Entradas + 1
    print("Puede pasar")
if Traba_TM:
    Entradas = Entradas + 1
elif Pase_libre:
    Entradas = Entradas + 1
    print ("Puede pasar")
if Traba_TV:
    Entradas = Entradas + 1
elif Pase_libre:
    Entradas = Entradas + 1
    print("Puede pasar")



    




