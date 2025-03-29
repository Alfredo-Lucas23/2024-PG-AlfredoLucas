# Crear un diccionario llamado informacion_personal con información ficticia sobre una persona
informacion_personal = {
    "nombre": "BENITO JUARES",
    "edad": 20,
    "ciudad": "Quito",
    "profesion": "Delivery"
}

# Acceder al valor asociado con la clave 'ciudad' y modificarlo con una ciudad diferente
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor al diccionario que represente la 'profesion' de la persona
informacion_personal["profesion"] = "Delivery"

# Verificar si la clave 'telefono' existe en el diccionario. Si no existe, agregarla con un número de teléfono ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar la clave 'edad' del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario resultante después de realizar todas las operaciones
print(informacion_personal)
