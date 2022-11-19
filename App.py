from tkinter import Tk, Label, Button, Entry

def fnSuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) + float(n2)
    txt3.insert(0,r)

ventana = Tk()
ventana.title("Suma")
ventana.geometry("450x260")

lbl1 = Label(ventana, text="1er numero", bg="red")
lbl1.place(relx=0.03, rely=0.04, relwidth=0.20, relheight=0.1)
txt1 = Entry(ventana, bg="red")
txt1.place(relx=0.25, rely=0.04, relwidth=0.20, relheight=0.1)

lbl2 = Label(ventana, text="2do numero", bg="red")
lbl2.place(relx=0.03, rely=0.17, relwidth=0.20, relheight=0.1)
txt2 = Entry(ventana, bg="red")
txt2.place(relx=0.25, rely=0.17, relwidth=0.20, relheight=0.1)

btn1 = Button(ventana, text="sumar", command=fnSuma)
btn1.place(relx=0.55, rely=0.17, relwidth=0.20, relheight=0.1)

lbl3 = Label(ventana, text="Resultado", bg="red")
lbl3.place(relx=0.03, rely=0.3, relwidth=0.20, relheight=0.1)
txt3 = Entry(ventana, text="Primer numero", bg="red")
txt3.place(relx=0.25, rely=0.3, relwidth=0.20, relheight=0.1)


ventana.mainloop()