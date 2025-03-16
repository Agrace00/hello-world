filename = input('Enter the filename: ')
with open(filename, 'r') as file:
    lines = file.readlines()
while True:
    print('Number of lines:', len(lines))
    line_number = int(input('Enter a line number (0 to quit): '))
    if line_number == 0:
        break
    print(lines[line_number - 1])
