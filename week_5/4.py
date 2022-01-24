import tkinter as tk
from tkinter import messagebox


def send_name():
    if first_name.get() == 'Piotr':
        messagebox.showinfo(title="OK", message='Witam Pana!')
    else:
        messagebox.showerror(title='Kurza twarz', message='Nie znam Pana!')


window = tk.Tk()
window.title('Pystart')

label = tk.Label(window, text="Jak masz na imię?")
label.pack()

first_name = tk.Entry()
first_name.pack()

button = tk.Button(text="OK", command=send_name)
button.pack()

window.mainloop()
