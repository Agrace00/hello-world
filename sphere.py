import math

radius = float(input("Enter the radius of the sphere: "))

diameter = radius * 2.0
circumference = 2.0 * math.pi * radius
surfaceArea = 4.0 * math.pi * (radius ** 2.0)
volume = (4.0/3.0) * math.pi * (radius ** 3.0)

print("Diameter: ", diameter)
print("Circumference: ", circumference)
print("Surface Area: ", surfaceArea)
print("Volume: ", volume)
