"""
File: testinputfunctions.py

Defines a function for robust input of ints.
"""

def inputFloat(prompt="Please enter an integer or a float: "):
    while True:
        user_input = input(prompt)

        if user_input.count('.') > 1:
            print("Error: the input cannot have more than one '.'")
        elif not user_input.replace('.', '', 1).isdigit():
            print("Error: the input must consist only of digits.")
        else:
            return float(user_input)

if __name__ == "__main__":
    value = inputFloat()
    print(value)
