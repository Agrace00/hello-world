import tkinter as tk

class TaxFormWithGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tax Calculator")

        self.income_var = tk.DoubleVar()
        self.dependents_var = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):

        self.addLabel("Income:", 0, 0)
        self.addLabel("Number of Dependents:", 1, 0)

        self.addEntry(self.income_var, 0, 1)
        self.addEntry(self.dependents_var, 1, 1)

        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_tax)
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def addLabel(self, text, row, column):
        label = tk.Label(self.root, text=text)
        label.grid(row=row, column=column, padx=10, pady=5, sticky=tk.E)

    def addEntry(self, variable, row, column):
        entry = tk.Entry(self.root, textvariable=variable)
        entry.grid(row=row, column=column, padx=10, pady=5)

    def calculate_tax(self):
        income = self.income_var.get()
        dependents = self.dependents_var.get()

        tax_due = income * 0.15 - dependents * 1000

        print(f"The tax due is: ${tax_due:.2f}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TaxFormWithGUI()
    app.run()
