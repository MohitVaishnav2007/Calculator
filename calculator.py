import tkinter as tk
from tkinter import messagebox
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#202124")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, bg="#202124")
        input_frame.pack(pady=10)

        input_field = tk.Entry(input_frame, font=('Arial', 24), textvariable=self.input_text, width=22, bd=5, bg="#303134", fg="white", justify='right')
        input_field.grid(row=0, column=0)
        input_field.bind("<Key>", lambda e: "break")  # Disable typing

        buttons_frame = tk.Frame(self.root, bg="#202124")
        buttons_frame.pack()

        buttons = [
            ["C", "DEL", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "^", "="],
            ["sqrt", "log", "sin", "cos"],
            ["tan"]
        ]

        for r, row in enumerate(buttons):
            for c, btn in enumerate(row):
                tk.Button(buttons_frame, text=btn, width=8, height=2, font=('Arial', 14), bg="#3c4043", fg="white",
                          command=lambda b=btn: self.on_button_click(b)).grid(row=r, column=c, padx=5, pady=5)

    def on_button_click(self, char):
        try:
            if char == "C":
                self.expression = ""
            elif char == "DEL":
                self.expression = self.expression[:-1]
            elif char == "=":
                result = str(eval(self.parse_expression(self.expression)))
                self.expression = result
            elif char in ["sqrt", "log", "sin", "cos", "tan"]:
                self.expression += f"math.{char}("
            elif char == "^":
                self.expression += "**"
            else:
                self.expression += str(char)

            self.input_text.set(self.expression)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression: {e}")
            self.expression = ""
            self.input_text.set("")

    def parse_expression(self, expr):
        return expr.replace('math.', 'math.')


if __name__ == '__main__':
    root = tk.Tk()
    calc = AdvancedCalculator(root)
    root.mainloop()
