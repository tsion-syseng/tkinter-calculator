import tkinter as tk

def handle_button_click(clicked_button_text):
    current_text = result_var.get()

    if clicked_button_text == "=":
        if not current_text:
            return
        try:
            expression = current_text.replace("÷", "/").replace("×", "*")
            result = eval(expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            result_var.set(result)
        except Exception:
            result_var.set("Error")
    elif clicked_button_text == "C":
        result_var.set("")
    elif clicked_button_text == "±":
        try:
            current_number = float(current_text)
            result_var.set(-current_number)
        except ValueError:
            result_var.set("Error")
    elif clicked_button_text == "%":
        try:
            current_number = float(current_text)
            result_var.set(current_number / 100)
        except ValueError:
            result_var.set("Error")
    elif clicked_button_text == ".":
        if not current_text or "." not in current_text.split()[-1]:
            result_var.set(current_text + ".")
    else:
        result_var.set(current_text + clicked_button_text)

# Main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#2e2e2e")  # Dark background
root.geometry("400x550")
root.resizable(False, False)

# Entry
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Helvetica", 28), justify="right", bd=0, bg="#1e1e1e", fg="white", insertbackground="white")
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)

# Button layout
buttons = [
    ("C", 1, 0, "#ff6666"), ("±", 1, 1, "#ffcc66"), ("%", 1, 2, "#ffcc66"), ("÷", 1, 3, "#66b3ff"),
    ("7", 2, 0, "#333333"), ("8", 2, 1, "#333333"), ("9", 2, 2, "#333333"), ("×", 2, 3, "#66b3ff"),
    ("4", 3, 0, "#333333"), ("5", 3, 1, "#333333"), ("6", 3, 2, "#333333"), ("-", 3, 3, "#66b3ff"),
    ("1", 4, 0, "#333333"), ("2", 4, 1, "#333333"), ("3", 4, 2, "#333333"), ("+", 4, 3, "#66b3ff"),
    ("0", 5, 0, "#333333", 2), (".", 5, 2, "#333333"), ("=", 5, 3, "#66b3ff")
]

# Create buttons
for info in buttons:
    text, row, col = info[:3]
    color = info[3]
    colspan = info[4] if len(info) > 4 else 1

    btn = tk.Button(root, text=text, font=("Helvetica", 22), fg="white", bg=color, bd=0, activebackground="#888888",
                    command=lambda t=text: handle_button_click(t))
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Configure grid
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Keyboard controls
root.bind("<Return>", lambda event: handle_button_click("="))
root.bind("<BackSpace>", lambda event: result_var.set(result_var.get()[:-1]))

root.mainloop()
