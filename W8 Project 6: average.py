def read_numbers(filename):
    """Reads numbers from a file and returns them as a list."""
    numbers = [] 
    try:
        infile = open(filename, 'r')
        for line in infile:
            nums = [float(num) for num in line.strip().split()]
            numbers.extend(nums)
        infile.close()
    except:
        print(f'Error: file: {filename} found.')
    return numbers

def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def main():
    filename = input("Enter the input file name: ")
    numbers = read_numbers(filename)

    if len(numbers) > 0:
        average = calculate_average(numbers)
        
        print(f"The average is {average}")

if __name__ == "__main__":
    main()
