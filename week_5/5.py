import tkinter as tk
from random import randint


def guess_number():
    diff = abs(target - int(guess.get()))
    if diff == 0:
        tip.configure(text=f'Koniec! Wygrałeś. Twój wynik to {len(guesses)}')
        return

    guesses.append(diff)
    if len(guesses) == 1:
        return

    if guesses[-1] > guesses[-2]:
        tip.configure(text='Zimno...')

    if guesses[-1] < guesses[-2]:
        tip.configure(text='Cieplej...')

    if guesses[-1] == guesses[-2]:
        tip.configure('Niezły ambaras...')


target = randint(1, 50)
print(target)
guesses = []

window = tk.Tk()
window.geometry('500x500')
window.title('Zgadnij liczbę')

label = tk.Label(window, text="Jaką liczbę wylosował komputer?")
label.pack()

guess = tk.Entry(window)
guess.pack()

button = tk.Button(window, text='Zgaduję', command=guess_number)
button.pack()

tip = tk.Label(window, text='')
tip.pack()

window.mainloop()
