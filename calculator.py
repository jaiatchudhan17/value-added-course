import tkinter as tk
from tkinter import font as tkfont

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x500")
        self.resizable(0, 0)
        
        self.current_input = ""
        self.total_expression = ""
        
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.total_label, self.label = self.create_display_labels()
        
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="lightgrey", fg="black", padx=24, font=tkfont.Font(size=16))
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_input, anchor=tk.E, bg="lightgrey", fg="black", padx=24, font=tkfont.Font(size=40, weight='bold'))
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self, height=221, bg="lightgrey")
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_input += str(value)
        self.update_current_label()

    def append_operator(self, operator):
        self.current_input += operator
        self.total_expression += self.current_input
        self.current_input = ""
        self.update_total_label()
        self.update_current_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="white", fg="black", font=tkfont.Font(size=24), borderwidth=5, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="white", fg="black", font=tkfont.Font(size=24), borderwidth=5, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_input = ""
        self.total_expression = ""
        self.update_current_label()
        self.update_total_label()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg="white", fg="black", font=tkfont.Font(size=24), borderwidth=5, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="lightblue", fg="black", font=tkfont.Font(size=24), borderwidth=5, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg="white", fg="black", font=tkfont.Font(size=24), borderwidth=5, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg="white", fg="black", font=tkfont.Font(size=24), borderwidth=5, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_input
        self.update_total_label()
        try:
            self.current_input = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_input = "Error"
        finally:
            self.update_current_label()

    def square(self):
        self.current_input = str(eval(f"{self.current_input}**2"))
        self.update_current_label()

    def sqrt(self):
        self.current_input = str(eval(f"{self.current_input}**0.5"))
        self.update_current_label()

    def update_current_label(self):
        self.label.config(text=self.current_input[:11])

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
