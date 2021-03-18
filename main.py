from tkinter import *
from tkinter import filedialog as fd

from help import help_text
import time


def open_file():
    file_name = fd.askopenfilename(filetypes=(("TXT files", "*.txt"),))
    if file_name != '':
        file = open(file_name, 'r')
        data = file.readlines()
        calculated_text.insert(1.0, data)


def show_information():
    children = Toplevel()
    children.title('Help')
    children.geometry("600x300+500+350")
    output_help_text = Text(children, height=20, width=80)
    scroll_b = Scrollbar(children, command=output_help_text.yview)
    scroll_b.grid(row=4, column=8, sticky='nsew')
    output_help_text.grid(row=4, column=0, sticky='nsew', columnspan=3)
    output_help_text.configure(yscrollcommand=scroll_b.set)
    output_help_text.insert('end', help_text)
    output_help_text.configure(state='disabled')


root = Tk()
root.title("Semantic text analysis")

root.resizable(width=False, height=False)
root.geometry("620x150+500+250")

label = Label(root, text='Input word:', font=("Comic Sans MS", 13, "bold"))
label.grid(row=0, column=0)

calculated_text = Text(root, height=5, width=50)
calculated_text.grid(row=1, column=1, sticky='nsew', columnspan=2)

help_button = Button(text="Help", width=10, command=show_information)
help_button.grid(row=0, column=3)

open_button = Button(text="Open file", width=10, command=open_file)
open_button.grid(row=1, column=3)

ok_button = Button(text="Semantic analysis", width=14)
ok_button.grid(row=2, column=3)
root.mainloop()
