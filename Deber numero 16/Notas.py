# Escritura de Archivo de Texto

# Crear un nuevo archivo llamado my_notes.txt y escribir al menos tres líneas de notas personales en él.
with open('my_notes.txt', 'w') as file:
    file.write("Hoy aprendí algo nuevo sobre la programación en Python. Me siento más seguro con el manejo de archivos de texto. Estoy emocionado por seguir mejorando mis habilidades y aplicarlas en proyectos futuros.\n")
    file.write("He decidido empezar a leer un libro nuevo cada mes. Este mes comenzaré con 'Cien años de soledad' de Gabriel García Márquez. Espero disfrutar de esta obra maestra de la literatura y aprender más sobre la cultura latinoamericana.\n")
    file.write("Mi objetivo para esta semana es hacer ejercicio al menos tres veces. Voy a mantenerme activo y saludable. Además, planeo probar una nueva rutina para mejorar  y reducir el estrés\n")

# Lectura de Archivo de Texto

# Abrir el archivo my_notes.txt y leer su contenido línea por línea.
with open('my_notes.txt', 'r') as file:
    for line in file:
        # Mostrar en la consola cada línea leída.
        print(line.strip())

# El archivo se cierra automáticamente al salir del bloque with.
