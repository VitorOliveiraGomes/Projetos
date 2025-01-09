import tkinter as tk

def click_button(item):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(item))

def clear_display():
    display.delete(0, tk.END)

def calculo():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "ERRO")


app = tk.Tk()
app.title("Calculadora")

display = tk.Entry(app, font=("Arial", 20), bd=10, insertwidth=2, width=14, border=4)
display.grid(row=0, column= 0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    tk.Button(app, text=text, padx=20, pady=20, bd=8, font=("Arial", 18),
              command=lambda item=text: click_button(item) if item != '='
              else calculo()).grid(row=row, column=col, sticky="nsew")
    tk.Button(app, text="C", padx=20, pady=20, bd=8, font=("Arial", 18), command=clear_display).grid(row=5, column=0, columnspan=4, sticky="nsew")

for i in range(4):
    app.grid_columnconfigure(i, weight=1)
for i in range(6):
    app.grid_rowconfigure(i, weight=1)

app.mainloop()