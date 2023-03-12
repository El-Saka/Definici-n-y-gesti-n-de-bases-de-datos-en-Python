import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('alumnos.db')

# Crear la tabla Alumnos
conn.execute('''CREATE TABLE Alumnos
             (id INTEGER PRIMARY KEY,
             nombre TEXT,
             apellido TEXT);''')

# Insertar datos en la tabla
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (1, 'Juan', 'Pérez')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (2, 'María', 'García')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (3, 'Pedro', 'López')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (4, 'Ana', 'Martínez')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (5, 'Carlos', 'González')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (6, 'Sara', 'Sánchez')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (7, 'Diego', 'Fernández')")
conn.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (8, 'Laura', 'Ruiz')")

# Guardar los cambios en la base de datos
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()

import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('alumnos.db')

# Buscar un alumno por nombre
nombre_buscar = 'Juan'
cursor = conn.execute("SELECT * FROM Alumnos WHERE nombre=?", (nombre_buscar,))
alumno = cursor.fetchone()

# Mostrar los datos del alumno por consola
print("Id:", alumno[0])
print("Nombre:", alumno[1])
print("Apellido:", alumno[2])

# Cerrar la conexión a la base de datos
conn.close()

