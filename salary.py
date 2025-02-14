startSal = float(input("Enter the starting salary: $"))

increase = int(input("Enter the annual increase: "))

years = int(input("Enter the number of years: "))

print("Year   Salary   Stipend\n------------------------")

multiplier = 1 + increase / 100

nextSal = startSal

for year in range(1, years + 1):
  
    stipend = 1000

    totalSalary = nextSal + stipend

    print("%2d%10.2f%10.2f" % (year, nextSal, totalSalary))

    nextSal *= multiplier
