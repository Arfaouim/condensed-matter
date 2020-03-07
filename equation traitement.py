from sympy import*
from tkinter import*
from tkinter.ttk import*

def sol():
    print(roots(e.get()))
def lim():
    print(limit(e1.get(),e2.get(),e3.get()))
    resultLabel.config(text=limit(e1.get(),e2.get(),e3.get()))


r=Tk()

root=Labelframe(r, text='Label')
e=Entry(root)
e.pack()
b=Button(root,text="racine d\'une fonction",command=sol)
b.pack()

l=Label(root,text="entrer fonction")
l.pack()
e1=Entry(root)
e1.pack()

l2=Label(root,text="variable")
l2.pack()
e2=Entry(root)
e2.pack()

l3=Label(root,text="tend vers")
l3.pack()
e3=Entry(root)
e3.pack()

b=Button(root,text="limit",command=lim)
b.pack()
resultLabel = Label(root, text = "limite est ")
resultLabel.pack(fill=X)

root.pack()

r.mainloop()
