#pedir dos expresiones y que al insertar si o no nos devuelva si o no debe de debolber true o false
variable_logico=input("ingresa si o no: ")
variable_logico=variable_logico.lower()=="si"
print(variable_logico)

variable_logico2=input("ingresa si o no: ")
variable_logico2=variable_logico2.lower()=="si"
print("La segunda respuesta es: ", variable_logico2)

print(f"¿Ambas resupuestas fueron si? {variable_logico and variable_logico2}")
print(f"¿una respuesta fue si? {variable_logico or variable_logico2}")
print(f"La negacion de la primera respuesta es:  { not variable_logico}")
print(f"La negacion de la segunda respuesta es:  { not variable_logico2}")