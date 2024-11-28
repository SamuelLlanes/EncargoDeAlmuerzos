
import tkinter
from tkinter import ttk 
from tkinter import messagebox



colores = [
        [ '#014d29' ],
        [ '#e4e2dd' ],
        [ '#f4f3f3' ],
        [ '#606060' ],
        [ '#000000' ],
        [ '#feffff' ]
        ]

pedido = []
clientes = []
cafeterias = []
pedidos = []

class pantalla1: 

    def __init__(self, root):
        self.root = root
        self.root.title("Pantalla de inicio")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.iniciar()

    def iniciar(self):
        bienvenida = tkinter.Label(self.root, text= "Bienvenido a ServeMe", font= "Garamond 20 bold",  bg= colores[1], fg= colores[0])
        bienvenida.place(x= 80, y= 50)

        seleccion = tkinter.Label(self.root, text= "Elige como ingresar", font= "Garamond 20 bold",  bg= colores[1], fg= colores[0])
        seleccion.place(x= 80, y= 150)      

        # opcion para ingresar como alumno a reservar

        boton_cliente= tkinter.Button(self.root, text= "Cliente", font= "Calibri 20",command= self.ir_a_pantalla2, bg= colores[0], fg= colores[1])
        boton_cliente.place(x= 150, y=250)

        # opcion para ingresar al apartado de cafeteria

        boton_cafe = tkinter.Button(self.root, text= "Cafeteria", font= "Calibri 20",command= self.ir_a_pantalla3, bg= colores[0], fg= colores[1])
        boton_cafe.place(x= 150, y= 350)

        # opcion para salir de la aplicacion

        boton_salir = tkinter.Button(self.root, text= "Salir", font= "Calibri 20",command=root.quit, bg= colores[1], fg= colores[0])
        boton_salir.place(x= 170, y= 500)

    def ir_a_pantalla2(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla2(nueva_ventana)
    
    def ir_a_pantalla3(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla3(nueva_ventana)

class pantalla2:
    def __init__(self, root):
        self.root = root
        self.root.title("Platos")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.registrarse()

    def registrarse(self):
        texto = tkinter.Label(self.root, text= "Registrate en ServeMe", font= "Calibri 20", bg= colores[1], fg= colores[0])
        texto.place(x= 60, y= 100)

        nombre_tex = tkinter.Label(self.root, text= "Escriba su nombre", font= "Calibri 20", bg= colores[1], fg= colores[0])
        nombre_tex.place(x= 60, y= 200)

        nombre = tkinter.Entry(self.root,  font= "Calibri 20", bg= colores[5], fg= colores[4])
        nombre.place(x= 60, y=250)
        
        ape_tex = tkinter.Label(self.root, text= "Escriba su apellido", font= "Calibri 20", bg= colores[1], fg= colores[0])
        ape_tex.place(x= 60, y= 300)

        apellido = tkinter.Entry(self.root, font= "Calibri 20", bg= colores[5], fg= colores[4])
        apellido.place(x= 60, y= 350)

        def boton_continuar():
            nom = nombre.get()
            ape = apellido.get() 
            if nom and ape: 
                
                clientes.append({"cliente": nom, "apellido": ape})
                messagebox.showinfo(" Ha ingresado exitosamente")
                boton_con = tkinter.Button(self.root, text= "Continuar", font= "Calibri 20", command= self.ir_a_pantalla4, bg= colores[0], fg= colores[1])
                boton_con.place(x= 150, y= 500)
            else:
                messagebox.showwarning("Complete ambos campos")
                    

        boton_regi = tkinter.Button(self.root, text= "Registrarse", font= "Calibri 20", command= boton_continuar, bg= colores[0], fg= colores[1])
        boton_regi.place(x= 150, y= 400)   

        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Calibri 20", command= self.ir_a_pantalla1, bg= colores[0], fg= colores[1])
        boton_regresar.place(x= 10, y= 5)

    def ir_a_pantalla1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla1(nueva_ventana)

    def ir_a_pantalla4(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla4(nueva_ventana)
    

class pantalla3:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Platos")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.ingresar()
    
    def ingresar(self):
            
        ServeMe = tkinter.Label(self.root, text= "ServeMe", font= "Garamond 30 bold", bg= colores[1], fg= colores[0])
        ServeMe.place(x= 150, y= 100)

        Reservas = tkinter.Label(self.root, text= "Seleccionar cafetería", font= "Poppins 20", bg= colores[1], fg= colores[0])
        Reservas.place(x= 100, y= 200)

        cafeteria_menu = ttk.Combobox(self.root, font="Poppins 12", width=25)
        cafeteria_menu['values'] = ["ESEN", "UCA", "UDB", "UFG", "Monica Herrera", "UJMD"]
        cafeteria_menu.place(x=100, y=250)  

        contra = tkinter.Label(self.root, text= "Contraseña", font= "Poppins 20", bg= colores[1], fg= colores[0])
        contra.place(x= 100, y= 300)

        password_entry = tkinter.Entry(self.root, font="Poppins 12", width=30, show="*")
        password_entry.place(x=100, y=350)

        def boton_continuar():
            cafe = cafeteria_menu.get()
            con = password_entry.get() 
            if cafe and con: 

                cafeterias.append({"cafe": cafe, "contra": con})
                messagebox.showinfo(" Ha ingresado exitosamente")
                boton_con = tkinter.Button(self.root, text= "Continuar", font= "Calibri 20", command= self.ir_a_pantalla5, bg= colores[0], fg= colores[1])
                boton_con.place(x= 150, y= 500)
            else:
                messagebox.showwarning("Complete ambos campos")
                    

        boton_regi = tkinter.Button(self.root, text= "Registrarse", font= "Calibri 20", command= boton_continuar, bg= colores[0], fg= colores[1])
        boton_regi.place(x= 150, y= 400)

        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Calibri 20", command= self.ir_a_pantalla1, bg= colores[0], fg= colores[1])
        boton_regresar.place(x= 10, y= 5)

    def ir_a_pantalla5(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla5(nueva_ventana)

    def ir_a_pantalla1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla1(nueva_ventana)

            
class pantalla5:
    def __init__(self, root):
        self.root = root
        self.root.title("Platos")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.gest_menu()


    def gest_menu(self):

        ServeMe = tkinter.Label(self.root, text= "ServeMe", font= "Garamond 30 bold",  bg= colores[1], fg= colores[0])
        ServeMe.place(x= 60, y= 70)

        boton_agregar = tkinter.Button(self.root, text= "Agregar pedidos", font= "Calibri 20",command= self.ir_a_pantalla6, bg= colores[0], fg= colores[1])
        boton_agregar.place(x= 60, y= 200)

        boton_ver = tkinter.Button(self.root, text= "Ver pedidos", font= "Calibri 20",command= self.ir_a_reservacion, bg= colores[0], fg= colores[1])
        boton_ver.place(x= 60, y= 300)

        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Calibri 20", command= self.ir_a_pantalla3, bg= colores[0], fg= colores[1])
        boton_regresar.place(x= 10, y= 5)

        boton_inicio = tkinter.Button(self.root, text= "Inicio", font= "Calibri 20", command= self.ir_a_pantalla1, bg= colores[0], fg= colores[1])
        boton_inicio.place(x= 300, y= 5)

    def ir_a_pantalla1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla1(nueva_ventana)   
    
    def ir_a_pantalla6(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla6(nueva_ventana)

    def ir_a_pantalla3(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla3(nueva_ventana)

    def ir_a_reservacion(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        reservacion(nueva_ventana)



class pantalla6:
    def __init__(self, root):
        self.root = root
        self.root.title("Agregar platos")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.agregar_plato()


    def agregar_plato(self):

        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Calibri 20", command= self.ir_a_pantalla5, bg= colores[0], fg= colores[1])
        boton_regresar.place(x= 10, y= 5)

        ServeMe = tkinter.Label(self.root, text= "ServeMe", font= "Garamond 30 bold",  bg= colores[1], fg= colores[0])
        ServeMe.place(x= 100, y= 80)
        nombre_texto = tkinter.Label(self.root, text= "Agregar plato", font= "Calibri 20", bg= colores[1], fg= colores[0])
        nombre_texto.place(x= 60, y= 200)

        nombre = tkinter.Entry(self.root, text= "Agregar plato", font= "Calibri 20", bg= colores[5], fg= colores[4])
        nombre.place(x= 60, y= 250)

        des_texto = tkinter.Label(self.root, text= "Agregar descripcion", font= "Calibri 20", bg= colores[1], fg= colores[0])
        des_texto.place(x= 60, y= 300)

        descripcion = tkinter.Entry(self.root, text= "Agregar descripcion", font= "Calibri 20", bg= colores[5], fg= colores[4])
        descripcion.place(x= 60, y= 350)
        
        def boton_agregar():
            nombre_plato = nombre.get()
            descripcion_plato = descripcion.get() 

            if nombre_plato and descripcion_plato: 
            
                pedido.append({"nombre": nombre_plato, "descripcion": descripcion_plato})
                messagebox.showinfo(" El plato fue agregado con éxito")
            else:
                messagebox.showwarning("Complete ambos campos")
                

        boton_agre = tkinter.Button(self.root, text= "Agregar", font= "Calibri 20", command= boton_agregar, bg= colores[0], fg= colores[1])
        boton_agre.place(x= 60, y= 500)

        boton_inicio = tkinter.Button(self.root, text= "inicio", font= "Calibri 20", command= self.ir_a_pantalla1, bg= colores[0], fg= colores[1])
        boton_inicio.place(x= 1000, y= 5)

    def ir_a_pantalla1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla1(nueva_ventana) 

    def ir_a_pantalla5(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla5(nueva_ventana)

class pantalla4:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservar plato")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.reservar_plato()

    def reservar_plato(self ):

        titulo = tkinter.Label(self.root, text= "ServeMe", font= "Garamond 30 bold", bg= colores[1], fg= colores[0])
        titulo.place(x= 100, y= 100)

        Menu = tkinter.Label(self.root, text= "Menú", font= "Calibri 20", bg= colores[1], fg= colores[0])
        Menu.place(x= 100, y= 200)

        plato = tkinter.Label(self.root, text= "Seleccionar plato", font= "Poppins 20", bg= colores[1], fg= colores[0])
        plato.place(x= 100, y= 200)

        for plato in pedido:
            menu = ttk.Combobox(self.root, font="Poppins 12", width=25)
            menu['values'] = [f"{plato['nombre']} - {plato['descripcion']}" for plato in pedido]
            menu.place(x=100, y=250)
        
        def boton_continuar():
            reservacion = menu.get()

            if reservacion:
                pedidos.append({"plato": reservacion})
                messagebox.showinfo(" Ha ingresado exitosamente")
                boton_re = tkinter.Button(self.root, text= "Continuar", font= "Calibri 20", command= self.ir_a_reserva1, bg= colores[0], fg= colores[1])
                boton_re.place(x= 150, y= 400)
            else:
                messagebox.showwarning("Complete ambos campos")
                    

        boton_reser = tkinter.Button(self.root, text= "Reservar", font= "Calibri 20", command= boton_continuar, bg= colores[0], fg= colores[1])
        boton_reser.place(x= 150, y= 350)

        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Calibri 20", command= self.ir_a_pantalla2, bg= colores[0], fg= colores[1])
        boton_regresar.place(x= 10, y= 5)

    def ir_a_pantalla2(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla2(nueva_ventana)

    def ir_a_reserva1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        reserva1(nueva_ventana)

class reserva1:
    def __init__(self, root):
        self.root = root
        self.root.title("Reserva exitosa")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.reserva1()

    def reserva1(self):
        ReservaExitosa = tkinter.Label(self.root, text= "¡Reserva\nexitosa!", font= "Garamond 30 bold", bg= colores[1], fg= colores[0])
        ReservaExitosa.place(x= 150, y= 50)

        Menu = tkinter.Label(self.root, text= "¿Pedir algo \n más?", font= "Poppins 20", bg= colores[1], fg= colores[0])
        Menu.place(x= 150, y= 180)

        BotonSi = tkinter.Button(self.root, text= "Sí", font= "Poppins 20", bg= colores[0], fg= colores[1], width= 6, command= self.ir_a_pantalla4)
        BotonSi.place(x= 110, y= 280)

        BotonNo = tkinter.Button(self.root, text= "No", font= "Poppins 20", bg= colores[0], fg= colores[1], width= 6, command= self.ir_a_reserva)
        BotonNo.place(x= 240, y= 280)

        boton_inicio = tkinter.Button(self.root, text= "Inicio", font= "Calibri 20", command= self.ir_a_pantalla1, bg= colores[0], fg= colores[1])
        boton_inicio.place(x= 300, y= 5)

    def ir_a_pantalla1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla1(nueva_ventana) 

    def ir_a_reserva(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        reserva(nueva_ventana)

    def ir_a_pantalla4(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla4(nueva_ventana)

class reserva:
    def __init__(self, root):
        self.root = root
        self.root.title("Regresar")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.reserva()

    def reserva(self):

            gracias = tkinter.Label(self.root, text= "Gracias por utilizar ServeMe\nPuede recoger su almuerzo\na partir de las 12:00pm", font= "Calibri 15", bg= colores[1], fg= colores[0])
            gracias.place(x=130, y=180)
            boton_gracias =tkinter.Button(self.root, text= "Cerrar", font= "Poppins 20", bg= colores[0], fg= colores[1], width= 6, command= self.ir_a_pantalla2)
            boton_gracias.place(x= 150, y= 280)

    def ir_a_pantalla2(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla2(nueva_ventana)

class reservacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Regresar")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.reservacion()

    def reservacion(self):
        ServeMe = tkinter.Label(self.root, text= "RESERVAS", font= "Garamond 30 bold", bg= colores[1], fg= colores[0])    
        ServeMe.place(x = 100, y= 150)

        listbox = tkinter.Listbox(self.root)
        listbox.pack(padx=200, pady=300)
            
        for plato in pedidos :
                listbox.insert(tkinter.END, f"{plato['plato']} ")
        for cliente in clientes:
                listbox.insert(tkinter.END, f"{cliente['cliente']}{cliente['apellido']} ")


        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Calibri 20", command= self.ir_a_pantalla5, bg= colores[0], fg= colores[1])
        boton_regresar.place(x= 10, y= 5)

        boton_inicio = tkinter.Button(self.root, text= "Inicio", font= "Calibri 20", command= self.ir_a_pantalla1, bg= colores[0], fg= colores[1])
        boton_inicio.place(x= 300, y= 5)

    def ir_a_pantalla1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla1(nueva_ventana) 

    def ir_a_pantalla5(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla5(nueva_ventana)

root = tkinter.Tk()
app = pantalla1(root)
root.mainloop()