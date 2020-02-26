import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox


def funcion_click():
    
    if(respuesta1.get() == '' or respuesta2.get() == ''): 
        accion.configure(text="Faltan Campos")
    else:
        accion.configure(text="LISTO")
        mBox.showinfo('Respuestas: ', respuesta1.get()+'\n'+respuesta2.get())    
        Calificacion()

def Calificacion():
    if(respuesta1.get() == "50m"):
        aux = 1
    else:
        aux = 0
    if(respuesta2.get() == "5 bultos"):
        aux = aux + 1
    else:
        aux = aux

    if(aux == 1):
        cal = 20
    if(aux == 2):
        cal = 40
    if(aux == 3):
        cal = 60
    if(aux == 4):
        cal = 80
    if(aux == 5):
        cal = 100

    mBox.showinfo('Tu calificacion es de: ' + cal)
            
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#------ Ventana FORMULARIO
ventana = tk.Tk()
ventana.title("Examen-Arquitectura")
ventana.geometry("500x450")
ventana.resizable(0,0)

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#------- TextBox Pregunta1
ttk.Label(ventana, text="¿Cuanto mide el edificio A?").place(x=10,y=20)
pregunta1 = tk.StringVar()
respuesta1 = ttk.Entry(ventana, width = 12, textvariable=pregunta1)
respuesta1.place(x=10,y=40)

#------- TextBox Pregunta2
ttk.Label(ventana, text="¿Cuanto cemento se ocupara para construir el edificio A?").place(x=10,y=60)
pregunta2 = tk.StringVar()
respuesta2 = ttk.Entry(ventana, width = 12, textvariable=pregunta2)
respuesta2.place(x=10,y=80)

#------- RadioButton Pregunta 3
ttk.Label(ventana, text= "¿Cual es el material principal que se usa para hacer la mezcla?").place(x = 10, y = 100)
opcion = tk.IntVar()
aux2 = opcion.get()  
radio1 = tk.Radiobutton(ventana, text= "Cemento", variable= opcion, value=1)
radio1.place(x=10,y=120)
radio2 = tk.Radiobutton(ventana, text= "Graba", variable= opcion, value=2)
radio2.place(x=120,y=120)
radio3 = tk.Radiobutton(ventana, text= "Cal", variable= opcion, value=3)
radio3.place(x=225,y=120)


#------- RadioButton Pregunta 4
ttk.Label(ventana, text= "¿Cúantos bultos de cemento se necesitan para hacer una pared de 5x5?").place(x = 10, y = 140)
respuesta4 = tk.IntVar()
aux2 = respuesta4.get()  
radio1 = tk.Radiobutton(ventana, text= "10", variable= respuesta4, value=1)
radio1.place(x=10,y=160)
radio2 = tk.Radiobutton(ventana, text= "15", variable= respuesta4, value=2)
radio2.place(x=120,y=160)
radio3 = tk.Radiobutton(ventana, text= "8", variable= respuesta4, value=3)
radio3.place(x=225,y=160)

#------ CheckBox Pregunt 5
ttk.Label(ventana, text= "Selecciona 2 marcas conocidas de cemento").place(x = 10, y = 180)
respuesta5 = tk.IntVar()
aux = respuesta5.get()
check = tk.Checkbutton(ventana, text = "Cemex", variable = respuesta5, onvalue = 1, offvalue = 0)
check.deselect()
check.place(x=10,y=200)

respuesta5 = tk.IntVar()
check = tk.Checkbutton(ventana, text = "Nahuatl", variable = respuesta5, onvalue = 0, offvalue = 0)
check.deselect()
check.place(x=120,y=200)

respuesta5 = tk.IntVar()
check = tk.Checkbutton(ventana, text = "Moctezuma", variable = respuesta5, onvalue = 1, offvalue = 0)
check.deselect()
check.place(x=225,y=200)

respuesta5 = tk.IntVar()
check = tk.Checkbutton(ventana, text = "Cemento Chuchita", variable = respuesta5, onvalue = 0, offvalue = 0)
check.deselect()
check.place(x=330,y=200)

respuesta5 = tk.IntVar()
check = tk.Checkbutton(ventana, text = "EduCemex", variable = respuesta5, onvalue = 0, offvalue = 0)
check.deselect()
check.place(x=150,y=220)



#------- Boton REGISTRAR
accion = ttk.Button(ventana, text="Calificar", command = funcion_click)
accion.place(x=200,y=350)


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------


ventana.mainloop()