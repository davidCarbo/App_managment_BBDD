import sqlite3
from tkinter import messagebox

def crearTabla():
    try:
        conn = sqlite3.connect('usuarios.db')
        c = conn.cursor()

        c.execute("""CREATE TABLE usuarios (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        PASSWORD VARCHAR(50),
        APELLIDO VARCHAR(50),
        DIRECCION VARCHAR(70)
        )""")

        c.close()
        conn.close()
        messagebox.showinfo('BBDD', 'Base de datos conectada. Tabla usuarios creada.')

    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "La base de datos ya está creada")

def agregarUsuarios(nombre, password, apellido, direccion):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    c.execute("INSERT INTO usuarios VALUES (NULL,?,?,?,?)", (nombre, password, apellido, direccion))
    conn.commit()
    messagebox.showinfo('BBDD', f'Registro de nombre "{nombre}" insertado con éxito')

    c.close()
    conn.close()

def borrarUsuarioBBDD(id):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    c.execute(f"DELETE FROM usuarios WHERE ID = {id}")
    conn.commit()
    messagebox.showinfo('BBDD', f'El usuario ha sido borrado con éxito')

    c.close()
    conn.close()

def infoUsuario(id):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    c.execute(f"SELECT ID, * FROM usuarios WHERE ID = {id}")

    lista = []
    for i in c.fetchone():
        print(i)
        lista.append(i)

    c.close()
    conn.close()

    return lista


def actualizarUsuario(campo, nuevoDato, id):

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    c.execute(f'UPDATE usuarios SET {campo} = "{nuevoDato}" WHERE ID = {id}')
    conn.commit()

    c.close()
    conn.close()

