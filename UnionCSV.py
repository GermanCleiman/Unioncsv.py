''' Visor de bases de datos '''
import pandas as pd
from tkinter import *
from tkinter import messagebox 


raiz=Tk()                
raiz.title("Concatenacion de archivos .csv")
raiz.geometry("440x240") 

archivo1=StringVar()
archivo2=StringVar()
nuevoArchivo=StringVar()

# ------ Funciones --------------------------------------------------------------
def crea_CSV():
        a=True
        while a :

                if archivo1.get()== "" or archivo2.get== "" or nuevoArchivo.get== "" :
                        messagebox.showwarning(" Error ", " Falta llenar campos")
                        break

                else:
                        try:
                                ar1= pd.read_csv(archivo1.get())
                                ar2= pd.read_csv(archivo2.get())

                                clients= pd.concat([ar1, ar2])

                                clients.to_csv(nuevoArchivo.get())

                                messagebox.showinfo( "Listo", "Archivo Creado con Exito")
                                break
                        except   FileNotFoundError :
                                messagebox.showwarning(" Error", """No se encuentra uno de los Archivos
    Verifica que esten bien escritos""")
                                break

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿ Deseas salir de la aplicacion ?")
    if valor=="yes":   
        raiz.destroy()  

def borrar():
    archivo1.set("")
    archivo2.set("")
    nuevoArchivo.set("")

# ----- Menu --------------------------------------------------------------------
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu)  #

archivoMenu=Menu(barraMenu,tearoff=0)   # tearoff saca la raya cortada que se forma arriva del cuadro
archivoMenu.add_command(label="Crear ", command=crea_CSV)
archivoMenu.add_command(label="Salir", command=salirAplicacion)


barraMenu.add_cascade(label="Archivos", menu=archivoMenu)
barraMenu.add_cascade(label="Borrar", command=borrar)

# --------Etiquetas ----------------------------------------------
nombreLabel=Label(raiz, text="1º Archivo")
nombreLabel.place(x=32, y=10)

passLabel=Label(raiz, text="2º Archivo")
passLabel.place(x=32, y=50)

apellidoLabel=Label(raiz, text="Nuevo Archivo")
apellidoLabel.place(x=30, y=90)

ayudalabel= Label(raiz, text= """Los archivos .csv tienen que tener igual numero de columnas y tipo de datos.
Tienen que estar guardados en la misma carpeta que este programa.
Controlar bien los nombres de los archivos antes de crear el nuevo """)
ayudalabel.place(x=10, y= 135)

# ----------- Entrys ---------------------------------------------

cuadroNombre =Entry(raiz, width=45 , textvariable=archivo1)
cuadroNombre.place(x=120, y=10)
cuadroNombre.config(fg="blue", justify="center") 
        #cambia el color y justificacion del texto a ingresar
cuadroPass =Entry(raiz, width=45 , textvariable=archivo2)
cuadroPass.place(x=120, y=50)
cuadroPass.config( fg="blue", justify="center") # en vez del texto ingresa por pantalla******

cuadroApellido=Entry(raiz, width=45 , textvariable=nuevoArchivo)
cuadroApellido.place(x=120, y=90)
cuadroApellido.config(fg="blue", justify="center")

raiz.mainloop()    