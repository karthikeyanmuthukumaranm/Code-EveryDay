import tkinter as tk
from tkinter import messagebox

def calci():
    
    try:
        exp=entry.get()
        result=eval(exp)
        entry.insert(tk.END,result)
        entry.delete(0,tk.END)

    expect Exception:
        messagebox.showerror("invalid")
def 