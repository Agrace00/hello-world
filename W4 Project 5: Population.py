initial_population = int(input("Enter the initial number of organisms: "))
growth_rate = float(input("Enter the rate of growth [a real number > 0]: "))
time_to_achieve_rate = int(input("Enter the number of hours to achieve the rate of growth: "))
total_hours = int(input("Enter the total hours of growth: "))

time_periods = total_hours // time_to_achieve_rate
total_population = initial_population * (growth_rate ** time_periods)

print(f"The total population is {total_population}")
