import tkinter
finestra = tkinter.Tk()
finestra.geometry("800x800")
finestra.resizable(True, True)
finestra.title("finestrina python")
finestra.configure(background="black")
def first_print():
    text = "Hello World!"
    text_output = tk.Label(window, text=text, fg="red", font=("Helvetica", 16))
    text_output.grid(row=0, column=1)
bottone = tkinter.Button(text="premi!", command=first_print)
bottone.grid(column = "0", row = "0")
if __name__ == '__main__':
    finestra.mainloop()