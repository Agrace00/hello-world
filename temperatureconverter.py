import tkinter as tk

class TemperatureConverter:
    def __init__(self, master):
        self.master = master
        master.title("Temperature Converter")

        self.f_label = tk.Label(master, text="Fahrenheit:")
        self.f_label.grid(row=0, column=0)
        self.f_entry = tk.Entry(master)
        self.f_entry.insert(0, "32.0")
        self.f_entry.grid(row=1, column=0)

        self.c_label = tk.Label(master, text="Celsius:")
        self.c_label.grid(row=0, column=1)
        self.c_entry = tk.Entry(master)
        self.c_entry.insert(0, "0.0")
        self.c_entry.grid(row=1, column=1)

        self.f_to_c_button = tk.Button(master, text=">>>>", command=self.f_to_c)
        self.f_to_c_button.grid(row=2, column=0)
        self.c_to_f_button = tk.Button(master, text="<<<<", command=self.c_to_f)
        self.c_to_f_button.grid(row=2, column=1)

    def f_to_c(self):
        f = float(self.f_entry.get())
        c = (f - 32) * 5/9
        self.c_entry.delete(0, tk.END)
        self.c_entry.insert(0, "{:.1f}".format(c))

    def c_to_f(self):
        c = float(self.c_entry.get())
        f = c * 9/5 + 32
        self.f_entry.delete(0, tk.END)
        self.f_entry.insert(0, "{:.1f}".format(f))


root = tk.Tk()
temp_conv = TemperatureConverter(root)
root.mainloop()
