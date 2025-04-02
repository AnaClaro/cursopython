import tkinter

root = tkinter.Tk()
root.title("Hello World Gráfico")
root.geometry("1024x768")

labelFrase = tkinter.Label(root,text='Olá Developer',font=('Ink Free',72),fg='Purple',bg='lightblue')
labelFrase.pack(padx=5,pady=5)

labelNome = tkinter.Label(root,text='Digite seu nome',font=('Comic Sans MS',30),fg='Green')
labelNome.pack(padx=5,pady=5)

entryNome = tkinter.Entry(root,width=25,font=('Verdana',32))
entryNome.pack(padx=5,pady=5)

buttonGravar = tkinter.Button(root,text="Gravar",command=None)
buttonGravar.pack(padx=5,pady=5)

root.mainloop()