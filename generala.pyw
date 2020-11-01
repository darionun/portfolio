# llamada para el metodo grafico
from tkinter import *
import random

# Ventana raiz
raiz = Tk()
raiz.title("LA GENERALA")
raiz.iconbitmap(r"C:\datos\Cursos\Curso-Python\interfaces_graficas\biohazard.ico")
raiz.resizable(1, 1)
# raiz.geometry("650x350")

# establece un frame
miFrame = Frame()
miFrame.pack(side="left", anchor="s")
miFrame.config(bg="white")
miFrame.config(width="850", height="700")
# miFrame.config(relief="groove")
miFrame.config(bd=35)
# miFrame.config(cursor="pirate")

# Como agregar una Label de texto
Label(miFrame, text="Tirá los dados...",
      fg="black", bg="white", font=("Comic Sans MS", 18)).grid(row=0, column=0, sticky="e")


# Con el metodo Label tambien se puede agregar una imagen
miImage = PhotoImage(
    file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara1.png")
Label(miFrame, image=miImage).grid(row=1, column=0)
miFrame.update()

miImage2 = PhotoImage(
    file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara1.png")
Label(miFrame, image=miImage).grid(row=1, column=1)
miFrame.update()


def tirar_dados():

        global miImage, miImage2
        
        num = random.randint(1, 6)
        num2 = random.randint(1, 6)

        if num == 1:
            miImage = PhotoImage(
            file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara1.png")
        
                        
        elif num == 2:
            miImage = PhotoImage(
                file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara2.png")
                
        elif num == 3:
            miImage = PhotoImage(
                file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara3.png")
                        
        elif num == 4:
            miImage = PhotoImage(
                file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara4.png")
                    
        elif num == 5:
            miImage = PhotoImage(
                file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara5.png")
                    
        elif num == 6:
            miImage = PhotoImage(
                file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara6.png")
            
        miImage.config(width="225", height="225")
        Label(miFrame, image=miImage).grid(row=1, column=0)
        miFrame.update()

        if num2 == 1:
            miImage2 = PhotoImage(
                file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara1.png")

        elif num2 == 2:
            miImage2 = PhotoImage(
                file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara2.png")

        elif num2 == 3:
            miImage2 = PhotoImage(
                file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara3.png")

        elif num2 == 4:
            miImage2 = PhotoImage(
                file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara4.png")

        elif num2 == 5:
            miImage2 = PhotoImage(
                file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara5.png")

        elif num2 == 6:
            miImage2 = PhotoImage(
                file=r"C:\datos\Cursos\Curso-Python\interfaces_graficas\dado_cara6.png")

        miImage2.config(width="225", height="225")
        Label(miFrame, image=miImage2).grid(row=1, column=1)
        miFrame.update()
        


# Agregar un cuadro de Texto
button = Button(miFrame, text="TIRAR", cursor="hand2", command=tirar_dados)
button.grid(row=0, column=1)    




# loop principal, simpre debe estar al final para mantener activa la ventana

raiz.mainloop()
