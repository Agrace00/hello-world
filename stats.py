def mean(numbers):
    """Compute the mean of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Compute the median of a list of numbers."""
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0: 
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:  
        return sorted_numbers[middle]

def mode(numbers):
    """Compute the mode of a list of numbers."""
    if not numbers:
        return 0
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]

    if len(modes) == 1:
        return modes[0]
    return min(modes)  

def main():
    """Test the statistical functions with a sample list."""
    sample_numbers = [5, 8, 9, 0, 7]
    print("Sample Numbers:", sample_numbers)
    print("Mean:", mean(sample_numbers))
    print("Median:", median(sample_numbers))
    print("Mode:", mode(sample_numbers))

if __name__ == "__main__":
    main()
