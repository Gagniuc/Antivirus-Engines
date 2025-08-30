import tkinter as t
from tkinter import filedialog as f
import os as o

def s():
    r = t.Tk()
    r.withdraw()
    p = f.askdirectory()
    if p:
        a(p)

def a(p, n=50):
    for r, d, fs in o.walk(p):
        for x in fs:
            q = o.path.join(r, x)
            with open(q, 'rb') as g:
                h = g.read(n)
                z = h.hex().upper()
                y = ' '.join([z[i:i+2] for i in range(0, len(z), 2)])
                print(f"Aligned Hex: {y}")

def g():
    r = t.Tk()
    r.title("Folder Selection")
    
    def b():
        p = f.askdirectory()
        if p:
            a(p)
    
    k = t.Button(r, text="Browse", command=b)
    k.pack(pady=10)
    r.mainloop()

g()

