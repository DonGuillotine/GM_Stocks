from tkinter import *

def convert_number_to_words(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return ' '.join(words[int(i)] for i in str(n))

def cheque_generator():
    name = name_entry.get()
    date = date_entry.get()
    amount = int(amount_entry.get())
    amount_in_words = convert_number_to_words(amount)
    result.set(f"Pay: {name}\nDate: {date}\nAmount: {amount_in_words}")

root = Tk()

Label(root, text="Name").grid(row=0)
Label(root, text="Date").grid(row=1)
Label(root, text="Amount").grid(row=2)

name_entry = Entry(root)
date_entry = Entry(root)
amount_entry = Entry(root)

name_entry.grid(row=0, column=1)
date_entry.grid(row=1, column=1)
amount_entry.grid(row=2, column=1)

Button(root, text='Generate', command=cheque_generator).grid(row=3, column=1, sticky=W, pady=4)

result = StringVar()
Label(root, text="", textvariable=result).grid(row=4)

mainloop()
