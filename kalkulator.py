import tkinter as tk

def add_to_display(char):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + str(char))

def calculate():
    try:
        expression = display.get()
        result = eval(expression) # Hati-hati dengan eval() di aplikasi nyata, tapi cukup untuk latihan
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

root = tk.Tk()
root.title("Kalkulator Sederhana")

display = tk.Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Contoh tombol
button_1 = tk.Button(root, text="1", padx=20, pady=10, command=lambda: add_to_display(1))
button_1.grid(row=3, column=0)

button_plus = tk.Button(root, text="+", padx=20, pady=10, command=lambda: add_to_display('+'))
button_plus.grid(row=4, column=3)

button_equal = tk.Button(root, text="=", padx=20, pady=10, command=calculate)
button_equal.grid(row=5, column=2)

root.mainloop()