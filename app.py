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

platosESEN = []
platosUCA = []
platosKey = []
clientes = []
cafeterias = {'ESEN':'esen1234','UCA':'uca1234','Key Institute':'key1234'}
cafeTemporal = [] ## Variable que almacena temporalmente la cafeteria elegida por los estudiantes
temporal = "" ## Variable que almacena temporalmente cual cafetería está usando la plataforma
pedidos = []

## Pantalla de elección de usuario
class pantalla1: 

    def __init__(self, root):
        self.root = root
        self.root.title("ServeMe")
        self.root.geometry("450x600") ## Medidas de la pantalla
        self.root.config(bg = colores[1]) ## Color de fondo de la pantalla
        self.iniciar() ## Inicia la construccion de la pantalla 

    def iniciar(self):
        bienvenida = tkinter.Label(self.root, text= "Bienvenido a\nServeMe", font= "Garamond 35 bold",  bg= colores[1], fg= colores[0])
        bienvenida.place(x= 90, y= 50)

        seleccion = tkinter.Label(self.root, text= "Elige como ingresar", font= "Garamond 20 bold",  bg= colores[1], fg= colores[0])
        seleccion.place(x= 110, y= 190)      

        ## Opción para ingresar como alumno a reservar

        boton_cliente= tkinter.Button(self.root, text= "Cliente", font= "Poppins 20",command= self.ir_a_pantalla2, bg= colores[0], fg= colores[1], borderwidth= 0, relief= "solid",padx= 22, pady= 5)
        boton_cliente.place(x= 150, y=270)

        ## Opción para ingresar como cafetería

        boton_cafe = tkinter.Button(self.root, text= "Cafetería", font= "Poppins 20",command= self.ir_a_pantalla3, bg= colores[0], fg= colores[1], borderwidth= 0, relief= "solid", padx= 10, pady= 5)
        boton_cafe.place(x= 150, y= 370)

        ## Opción para salir de la aplicación

        boton_salir = tkinter.Button(self.root, text= "Salir", font= "Poppins 20",command=root.quit, bg= colores[1], fg= colores[0], borderwidth= 0, relief= "solid")
        boton_salir.place(x= 190, y= 500)

    ## Funcion para cambiar de pantalla 
    def ir_a_pantalla2(self):
        self.root.destroy() ##Cierra la pantalla actual
        nueva_ventana = tkinter.Tk()
        pantalla2(nueva_ventana) ##Abre la nueva pantalla
    
    def ir_a_pantalla3(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla3(nueva_ventana)

## Pantalla para que el cliente se registre
class pantalla2:
    def __init__(self, root):
        self.root = root
        self.root.title("ServeMe")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.registrarse()

    def registrarse(self):
        texto = tkinter.Label(self.root, text= "Regístrate en ServeMe", font= "Garamond 30 bold", bg= colores[1], fg= colores[0])
        texto.place(x= 30, y= 70)

        nombre_tex = tkinter.Label(self.root, text= "Escribe tu nombre", font= "Poppins 20", bg= colores[1], fg= colores[0])
        nombre_tex.place(x= 60, y= 150)

        ## Entradas de textos para ingresar datos del cliente
        nombre = tkinter.Entry(self.root,  font= "Poppins 18", bg= colores[5], fg= colores[4], width= 25, borderwidth= 0, relief= "solid")
        nombre.place(x= 60, y=200)
        
        ape_tex = tkinter.Label(self.root, text= "Escribe tu apellido", font= "Poppins 20", bg= colores[1], fg= colores[0])
        ape_tex.place(x= 60, y= 240)

        apellido = tkinter.Entry(self.root, font= "Poppins 18", bg= colores[5], fg= colores[4], width= 25, borderwidth= 0, relief= "solid")
        apellido.place(x= 60, y= 290)

        Reservas = tkinter.Label(self.root, text= "Selecciona tu cafe preferida", font= "Poppins 20", bg= colores[1], fg= colores[0])
        Reservas.place(x= 60, y= 330)

        ## Elección de cafeteria para el cliente
        cafeteria_menu = ttk.Combobox(self.root, font="Poppins 18", width=23)
        cafeteria_menu.config(state= 'readonly')
        cafeteria_menu['values'] = ("ESEN","UCA","Key Institute")
        cafeteria_menu.place(x=60, y=380) 

        ## Este boton captura los datos ingresados del cliente para ponerlos dentro de la lista clientes
        def boton_continuar():
            global cafeTemporal
            nom = nombre.get()
            ape = apellido.get() 
            cafeTemporal = cafeteria_menu.get()
            if nom and ape and cafeTemporal: ##Pendiente de decidir el tercer campo
                clientes.append({"cliente": nom, "apellido": ape, "cafe":cafeTemporal, "reservación":""})
                self.ir_a_pantalla4()
            else:
                messagebox.showwarning("","Completa todos los campos")
                    
        ## Al darle click a este botón se ejecuta la funcion anterior de boton_continuar
        boton_regi = tkinter.Button(self.root, text= "Ingresar", font= "Poppins 20", command= boton_continuar, bg= colores[0], fg= colores[1],borderwidth= 0, relief= "solid", padx = 10, pady= 5)
        boton_regi.place(x= 60, y= 450)   

        ## Este boton regresa a la pantalla de inicio que es para elegir usuario
        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Poppins 15", command= self.ir_a_pantalla1, bg= colores[1], fg= colores[0], borderwidth= 0, relief= "solid")
        boton_regresar.place(x= 10, y= 5)

    def ir_a_pantalla1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla1(nueva_ventana)

    def ir_a_pantalla4(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla4(nueva_ventana)
    
## Pantalla para que registren la cafeteria 
class pantalla3:
    
    def __init__(self, root):
        self.root = root
        self.root.title("ServeMe")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.ingresar()
    
    def ingresar(self):
            
        texto = tkinter.Label(self.root, text= "Regístrate en ServeMe", font= "Garamond 30 bold", bg= colores[1], fg= colores[0])
        texto.place(x= 30, y= 70)

        Reservas = tkinter.Label(self.root, text= "Seleccionar cafetería", font= "Poppins 20", bg= colores[1], fg= colores[0])
        Reservas.place(x= 60, y= 180)

        ## Este Combobox es para elegir cual es la cafeteria que se esta registrando 
        cafeteria_menu = ttk.Combobox(self.root, font="Poppins 18", width=23)
        cafeteria_menu.config(state= 'readonly')
        cafeteria_menu['values'] = ("ESEN","UCA","Key Institute")
        cafeteria_menu.place(x=60, y=230)  

        contra = tkinter.Label(self.root, text= "Contraseña", font= "Poppins 20", bg= colores[1], fg= colores[0])
        contra.place(x= 60, y= 270)

        ## Entrada de texto para ingresar la contraseña
        password_entry = tkinter.Entry(self.root, font="Poppins 18", width=25, show="*", borderwidth= 0, relief= "solid")
        password_entry.place(x=60, y=320)

        ## Este boton corrobora que los datos ingresados esten correctos
        def boton_regis():
            global temporal
            cafe = cafeteria_menu.get()
            temporal = cafe
            con = password_entry.get() 
            if cafe and con: 
                if con == cafeterias[cafe]:
                    self.ir_a_pantalla5()
                else:
                    messagebox.showerror("","La contraseña es incorrecta")
            else:
                messagebox.showwarning("","Complete ambos campos")
                    
        ## Al darle click a este botón se ejecuta la funcion de boton_regis
        boton_regi = tkinter.Button(self.root, text= "Ingresar", font= "Poppins 20", command= boton_regis, bg= colores[0], fg= colores[1],borderwidth= 0, relief= "solid", padx = 10, pady= 5)
        boton_regi.place(x= 60, y= 450)  

        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Poppins 15", command= self.ir_a_pantalla1, bg= colores[1], fg= colores[0], borderwidth= 0, relief= "solid")
        boton_regresar.place(x= 10, y= 5)

    def ir_a_pantalla5(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla5(nueva_ventana)

    def ir_a_pantalla1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla1(nueva_ventana)

## En esta pantalla la cafeteria agrega los platos que tendra disponible en el menú          
class pantalla5:
    def __init__(self, root):
        self.root = root
        self.root.title("ServeMe")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.gest_menu()


    def gest_menu(self):

        ServeMe = tkinter.Label(self.root, text= "ServeMe", font= "Garamond 40 bold",  bg= colores[1], fg= colores[0])
        ServeMe.place(x= 30, y= 70)

        nombre_texto = tkinter.Label(self.root, text= "Nombre del plato", font= "Poppins 20", bg= colores[1], fg= colores[0])
        nombre_texto.place(x= 60, y= 160)

        nombre = tkinter.Entry(self.root, font= "Poppins 18", bg= colores[5], fg= colores[4], width= 25, borderwidth= 0, relief= "solid")
        nombre.place(x= 60, y= 210)

        des_texto = tkinter.Label(self.root, text= "Descripción del plato", font= "Poppins 20", bg= colores[1], fg= colores[0])
        des_texto.place(x= 60, y= 260)

        descripcion = tkinter.Entry(self.root, font= "Poppins 18", bg= colores[5], fg= colores[4], width= 25, borderwidth= 0, relief= "solid")
        descripcion.place(x= 60, y= 310)

        ## Este boton captura los datos ingresados y los agrega a las listas de cada menu segun la cafeteria 
        def boton_agregar():
            nombre_plato = nombre.get()
            descripcion_plato = descripcion.get() 

            if nombre_plato and descripcion_plato: 
                if temporal == "ESEN":
                    platosESEN.append({"nombre":nombre_plato,"descripción":descripcion_plato})
                    messagebox.showinfo("","El plato fue agregado al menú")
                elif temporal == "UCA":
                    platosUCA.append({"nombre":nombre_plato,"descripción":descripcion_plato})
                    messagebox.showinfo("","El plato fue agregado al menú")
                elif temporal == "Key Institute":
                    platosKey.append({"nombre":nombre_plato,"descripción":descripcion_plato})
                    messagebox.showinfo("","El plato fue agregado al menú")
            else:
                messagebox.showwarning("Complete ambos campos")
                
        ## Al darle click a este boton se ejecuta la funcion de boton_agregar
        boton_agre = tkinter.Button(self.root, text= "Agregar al menú", font= "Poppins 20", command= boton_agregar, bg= colores[0], fg= colores[1], borderwidth= 0, relief= "solid")
        boton_agre.place(x= 60, y= 380)

        ## Este boton dirije a la pantalla de reservaciones 
        boton_ver = tkinter.Button(self.root, text= "Ver pedidos", font= "Poppins 15",command= self.ir_a_reservacion, bg= colores[0], fg= colores[1], borderwidth= 0, relief= "solid")
        boton_ver.place(x= 240, y= 490)

        ## Este boton dirije a la pantalla del menu
        boton_ver_menu = tkinter.Button(self.root, text= "Ver menú actual", font= "Poppins 15",command= self.ir_a_menuactual, bg= colores[0], fg= colores[1], borderwidth= 0, relief= "solid")
        boton_ver_menu.place(x= 60, y= 490)

        ## Este boton regresa a la pantalla anterior que es la de registrarse 
        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Poppins 15", command= self.ir_a_pantalla3, bg= colores[1], fg= colores[0], borderwidth= 0, relief= "solid")
        boton_regresar.place(x= 10, y= 5)

        boton_inicio = tkinter.Button(self.root, text= "Inicio", font= "Poppins 15", command= self.ir_a_pantalla1, bg= colores[1], fg= colores[0], borderwidth= 0, relief= "solid")
        boton_inicio.place(x= 380, y= 5)

    def ir_a_pantalla1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla1(nueva_ventana)   
    
    def ir_a_pantalla3(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla3(nueva_ventana)

    def ir_a_reservacion(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        reservacion(nueva_ventana)

    def ir_a_menuactual(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        MenuActual(nueva_ventana)

## En esta pantalla el cliente elige el plato que desea reservar
class pantalla4:
    def __init__(self, root):
        self.root = root
        self.root.title("ServeMe")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.reservar_plato()

    def reservar_plato(self):

        titulo = tkinter.Label(self.root, text= "ServeMe", font= "Garamond 40 bold", bg= colores[1], fg= colores[0])
        titulo.place(x= 30, y= 70)

        plato = tkinter.Label(self.root, text= "Seleccionar plato", font= "Poppins 20", bg= colores[1], fg= colores[0])

        NoHay = tkinter.Label(self.root, text= "Aún no se ha\nagregado el menú\n:(", font= "Poppins 20", bg= colores[1], fg= colores[0])

        ## Este boton captura los datos que eligio el cliente
        def boton_reservar():
            reservacion = menu.get()
            clientes[-1]['reservación'] = reservacion
            messagebox.showinfo("","¡Plato reservado exitosamente!. Puede pasar a recogerlo a las 12:00pm. Gracias por usar esta app <3")
            self.ir_a_pantalla1()
 
        ## Al darle click a este boton se ejecuta la funcion de boton_reservar
        boton_reser = tkinter.Button(self.root, text= "Reservar", font= "Poppins 20", command= boton_reservar, bg= colores[0], fg= colores[1], borderwidth= 0, relief= "solid")
        
        ## Este condicional muestra el menu dependiendo de la universidad seleccionada
        if cafeTemporal == "ESEN":
            if len(platosESEN) == 0:
                NoHay.place(x= 120, y=170)
            else:
                plato.place(x= 60, y= 230)
                for p in platosESEN:
                    menu = ttk.Combobox(self.root, font="Poppins 18", width=25)
                    menu.config(state= 'readonly')
                    menu['values'] = [f"{p['nombre']} - {p['descripción']}" for p in platosESEN]
                    menu.place(x=60, y=300)
                boton_reser.place(x= 60, y= 350)
        elif cafeTemporal == "UCA":
            if len(platosUCA) == 0:
                NoHay.place(x= 120, y=300)
            else:
                plato.place(x= 60, y= 230)
                for p in platosUCA:
                    menu = ttk.Combobox(self.root, font="Poppins 18", width=25)
                    menu.config(state= 'readonly')
                    menu['values'] = [f"{p['nombre']} - {p['descripción']}" for p in platosUCA]
                    menu.place(x=60, y=300)
                boton_reser.place(x= 60, y= 350)
        elif cafeTemporal == "Key Institute":
            if len(platosKey) == 0:
                NoHay.place(x= 120, y=300)
            else:
                plato.place(x= 60, y= 230)
                for p in platosKey:
                    menu = ttk.Combobox(self.root, font="Poppins 18", width=25)
                    menu.config(state= 'readonly')
                    menu['values'] = [f"{p['nombre']} - {p['descripción']}" for p in platosKey]
                    menu.place(x=60, y=300)
                boton_reser.place(x= 60, y= 350)
            
        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Poppins 15", command= self.ir_a_pantalla2, bg= colores[1], fg= colores[0], borderwidth= 0, relief= "solid")
        boton_regresar.place(x= 10, y= 5)

        boton_inicio = tkinter.Button(self.root, text= "Inicio", font= "Poppins 15", command= self.ir_a_pantalla1, bg= colores[1], fg= colores[0], borderwidth= 0, relief= "solid")
        boton_inicio.place(x= 380, y= 5)

    def ir_a_pantalla2(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla2(nueva_ventana)

    def ir_a_pantalla1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla1(nueva_ventana) 

## Pantalla donde se muestran los platos reservados
class reservacion:
    def __init__(self, root):
        self.root = root
        self.root.title("ServeMe")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.reservacion()

    def reservacion(self):
        PReservados = tkinter.Label(self.root, text= "Platos reservados", font= "Garamond 30 bold", bg= colores[1], fg= colores[0])    
        PReservados.place(x = 30, y= 70)

        listbox = tkinter.Listbox(self.root, height= 25, width= 50, borderwidth= 0, relief= "solid", font= "Poppins 9")
        listbox.place(x= 50, y= 150)
        
        ## Condicional que enlista los platos reservados según la universidad
        if temporal == "ESEN":
            for q in clientes:
                if q['cafe'] == "ESEN":
                    listbox.insert(tkinter.END, f"{q['cliente']} {q['apellido']}: {q['reservación']}")
        elif temporal == "UCA":
            for q in clientes:
                if q['cafe'] == "UCA":
                    listbox.insert(tkinter.END, f"{q['cliente']} {q['apellido']}: {q['reservación']}")
        elif temporal == "Key Institute":
            for q in clientes:
                if q['cafe'] == "Key Institute":
                    listbox.insert(tkinter.END, f"{q['cliente']} {q['apellido']}: {q['reservación']}")
    
        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Poppins 15", command= self.ir_a_pantalla5, bg= colores[1], fg= colores[0], borderwidth= 0, relief= "solid")
        boton_regresar.place(x= 10, y= 5)

        boton_inicio = tkinter.Button(self.root, text= "Inicio", font= "Poppins 15", command= self.ir_a_pantalla1, bg= colores[1], fg= colores[0], borderwidth= 0, relief= "solid")
        boton_inicio.place(x= 380, y= 5)

    def ir_a_pantalla1(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla1(nueva_ventana) 

    def ir_a_pantalla5(self):
        self.root.destroy()
        nueva_ventana = tkinter.Tk()
        pantalla5(nueva_ventana)

## Pantalla que muestra el menú que ha ingresado la cafetería
class MenuActual:
    def __init__(self,root):
        self.root = root
        self.root.title("ServeMe")
        self.root.geometry("450x600")
        self.root.config(bg = colores[1])
        self.menu()
        
    def menu(self):

        MenuDelDia = tkinter.Label(self.root, text= "Menú", font= "Garamond 30 bold", bg= colores[1], fg= colores[0])    
        MenuDelDia.place(x = 30, y= 70)

        listbox = tkinter.Listbox(self.root, height= 25, width= 50, borderwidth= 0, relief= "solid", font= "Poppins 9")
        listbox.place(x= 50, y= 150)

        ## Condicional que enlista los platos según la universidad
        if temporal == "ESEN":
            for q in platosESEN:
                listbox.insert(tkinter.END, f"{q['nombre']} - {q['descripción']}")
        elif temporal == "UCA":
            for q in platosUCA:
                listbox.insert(tkinter.END, f"{q['nombre']} - {q['descripción']}")
        elif temporal == "Key Institute":
            for q in platosKey:
                listbox.insert(tkinter.END, f"{q['nombre']} - {q['descripción']}")

        boton_regresar = tkinter.Button(self.root, text= "Regresar", font= "Poppins 15", command= self.ir_a_pantalla5, bg= colores[1], fg= colores[0], borderwidth= 0, relief= "solid")
        boton_regresar.place(x= 10, y= 5)

        boton_inicio = tkinter.Button(self.root, text= "Inicio", font= "Poppins 15", command= self.ir_a_pantalla1, bg= colores[1], fg= colores[0], borderwidth= 0, relief= "solid")
        boton_inicio.place(x= 380, y= 5)

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