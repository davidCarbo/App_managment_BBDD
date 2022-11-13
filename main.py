from tkinter import *
from tkinter import messagebox
import BBDD

#Todo, tiene estos colores porque está a medias de subir al guithub.
#TODO mencionar que la contraseña en la base de datos no se ve encriptada. Hay que aplicarlo.

root =Tk()
root.title('Gestion BBDD')

frame = Frame(root)
frame.pack()

#---------------------Declarando variables de control--------------------
valorEntryID = StringVar()
valorEntryNombre = StringVar()
valorEntryPassword = StringVar()
valorEntryApellido = StringVar()
valorEntryDireccion = StringVar()

#--------------------funciones GUI------------------------
def salirApp():
    valor = messagebox.askquestion('Salir', '¿Deseas salir de la app?')

    if valor == 'yes':
        root.destroy()

def borrarTextoInput():
    entry_id.delete(0, 'end')
    entry_nombre.delete(0, 'end')
    entry_password.delete(0, 'end')
    entry_apellido.delete(0, 'end')
    entry_direccion.delete(0, 'end')
    entry_comentario.delete('1.0', 'end')

def crearUsuario():
    nombre = valorEntryNombre.get()
    password = valorEntryPassword.get()
    apellido = valorEntryApellido.get()
    direccion = valorEntryDireccion.get()

    BBDD.agregarUsuarios(nombre, password, apellido, direccion)
    borrarTextoInput()

def leerInfoUsuario():
    id = valorEntryID.get()

    try:
        BBDD.infoUsuario(id)

    except:
        messagebox.showwarning("¡Atención!", "Este usuario no se encuentra en la base de datos")

    valorEntryNombre.set(BBDD.infoUsuario(id)[2])
    valorEntryPassword.set(BBDD.infoUsuario(id)[3])
    valorEntryApellido.set(BBDD.infoUsuario(id)[4])
    valorEntryDireccion.set(BBDD.infoUsuario(id)[5])

def actualizarInfoUsuario():
    id = valorEntryID.get()
    nombre = valorEntryNombre.get()
    password = valorEntryPassword.get()
    apellido = valorEntryApellido.get()
    direccion = valorEntryDireccion.get()

    BBDD.actualizarUsuario('NOMBRE_USUARIO', nombre, id)
    BBDD.actualizarUsuario('PASSWORD', password, id)
    BBDD.actualizarUsuario('APELLIDO', apellido, id)
    BBDD.actualizarUsuario('DIRECCION', direccion, id)

    messagebox.showinfo('BBDD', f'Registro actualizado con éxito')
    borrarTextoInput()

def borrarUsuario():
    id = valorEntryID.get()

    BBDD.borrarUsuarioBBDD(id)
    borrarTextoInput()

#-------------------------Campos--------------------------
label_id = Label(frame, text='ID:')
label_id.grid(column=0, row=0, sticky=E, padx=7, pady=10)
label_nombre = Label(frame, text='Nombre:')
label_nombre.grid(column=0, row=1, sticky=E, padx=7, pady=10)
label_password = Label(frame, text='Password:')
label_password.grid(column=0, row=2, sticky=E, padx=7, pady=10)
label_apellido = Label(frame, text='Apellido:')
label_apellido.grid(column=0, row=3, sticky=E, padx=7, pady=10)
label_direccion = Label(frame, text='Dirección:')
label_direccion.grid(column=0, row=4, sticky=E, padx=7, pady=10)
label_comentario = Label(frame, text='Comentarios:')
label_comentario.grid(column=0, row=5, sticky=E, padx=7, pady=10)

entry_id = Entry(frame, textvariable=valorEntryID)
entry_id.grid(column=1, row=0, sticky=E, padx=7, pady=10)
entry_nombre = Entry(frame, justify='right', fg='red', textvariable=valorEntryNombre)
entry_nombre.grid(column=1, row=1, sticky=E, padx=7, pady=10)
entry_password = Entry(frame, show='*', textvariable=valorEntryPassword)
entry_password.grid(column=1, row=2, sticky=E, padx=7, pady=10)
entry_apellido = Entry(frame, textvariable=valorEntryApellido)
entry_apellido.grid(column=1, row=3, sticky=E, padx=7, pady=10)
entry_direccion = Entry(frame, textvariable=valorEntryDireccion)
entry_direccion.grid(column=1, row=4, sticky=E, padx=7, pady=10)
entry_comentario = Text(frame, height=7, width=30)
entry_comentario.grid(column=1, row=5, sticky=E, pady=10)
scroll = Scrollbar(frame, command=entry_comentario.yview)
scroll.grid(column=2, row=5, sticky='nsew')
entry_comentario.config(yscrollcommand=scroll.set)

#---------------------------Botones CURD------------------------

frame2 = Frame(root)
frame2.pack()

btn_create = Button(frame2, text='Create', command=crearUsuario)
btn_create.grid(column=0, row=6, sticky=E, pady=5)
btn_read = Button(frame2, text='Read', command=leerInfoUsuario)
btn_read.grid(column=1, row=6, sticky=E, pady=5)
btn_update = Button(frame2, text='Update', command=actualizarInfoUsuario)
btn_update.grid(column=2, row=6, sticky=E, pady=5)
btn_delete = Button(frame2, text='Delete', command=borrarUsuario)
btn_delete.grid(column=3, row=6, sticky=E, pady=5)

#-------------------------Menu----------------------------

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoBBDD = Menu(barraMenu, tearoff=0)
archivoBBDD.add_command(label='Conectar', command=BBDD.crearTabla)
archivoBBDD.add_command(label='Salir', command=salirApp)
archivoBorrar = Menu(barraMenu, tearoff=0)
archivoBorrar.add_command(label='Borrar campos', command=borrarTextoInput)
archivoCRUD = Menu(barraMenu, tearoff=0)
archivoCRUD.add_command(label='Crear', command=crearUsuario)
archivoCRUD.add_command(label='Leer', command=leerInfoUsuario)
archivoCRUD.add_command(label='Actualizar', command=actualizarInfoUsuario)
archivoCRUD.add_command(label='Borrar', command=borrarUsuario)
archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label='Licencia')
archivoAyuda.add_command(label='Acerca de')

barraMenu.add_cascade(label='BBDD', menu=archivoBBDD)
barraMenu.add_cascade(label='Borrar', menu=archivoBorrar)
barraMenu.add_cascade(label='CRUD', menu=archivoCRUD)
barraMenu.add_cascade(label='Ayuda', menu=archivoAyuda)



root.mainloop()
