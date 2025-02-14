while True:
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    if (a == b) and (b == c):
        print("The triangle is equilateral.")
    else:
        print("The triangle is not equilateral.")
