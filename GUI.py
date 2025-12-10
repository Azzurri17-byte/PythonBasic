# library
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
frm = ttk.Frame(window)
window.configure(bg="black")
window.geometry("200x300")
window.resizable(False, False)
window.title("hallo wir")
frm.pack(padx=10, pady=10,fill="x", expand=True)

# Variable dan function
NAMA = tk.StringVar()
UMUR = tk.StringVar()
def submit():
    info = f"hello, {NAMA.get()}, umur anda {UMUR.get()}, salam kenal"
    showinfo(title="hello wor", message=info)

# label nama dan input nama
namaLabel = ttk.Label(frm, text="nama ")
namaLabel.pack(padx=10,pady=10,fill="x",expand=True)

namaEntry = ttk.Entry(frm, textvariable=NAMA)
namaEntry.pack(padx=10,pady=10,fill="x",expand=True)

# label umur dan input umur
umurLabel = ttk.Label(frm, text="umur")
umurLabel.pack(padx=10,pady=10,fill="x",expand=True)

umurEntry = ttk.Entry(frm,textvariable=UMUR)
umurEntry.pack(padx=10,pady=10,fill="x",expand=True)

# button submit
submitButton = ttk.Button(frm, text="submit",command=submit)
submitButton.pack(padx=10,pady=10,fill="x",expand=True)


window.mainloop()