import tkinter as tk

Au = tk.Tk()
Au.title("Automatic Username")
Au.minsize(width= 450, height= 320)

frm=tk.LabelFrame(Au, text="Username Suggestion", width= 400, height= 300)
lblFN=tk.Label(Au, text="First Name : ")
lblFN.grid(column=2, row=3)

ent1=tk.Entry(Au, width= 30)
ent1.grid(column=3, row=3)

lblSN=tk.Label(Au, text="Second Name : ")
lblSN.grid(column=2, row=4)

ent2=tk.Entry(Au, width= 30)
ent2.grid(column=3, row=4)

lblSG=tk.Label(Au, text="Suggested : ")
lblSG.grid(column=2, row=5)

ent3=tk.Entry(Au, width= 30)
ent3.grid(column=3, row=5)

btnCB=tk.Button(Au, text="Combine", width=10)
btnCB.place(x=88, y=70)

btnCR=tk.Button(Au, text="Clear", width=10)
btnCR.place(x=192, y=70)

btnEX=tk.Button(Au, text="Exit", width=10)
btnEX.place(x=192, y=100)

Au.mainloop()