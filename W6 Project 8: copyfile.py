def copyfile():
    
    sourceFileName = input("Enter the first filename: ")
    destinationFileName = input("Enter the second filename: ")
    
    try:
        
        with open(sourceFileName, 'r') as inputFile:
            
            content = inputFile.read()
        
      
        with open(destinationFileName, 'w') as outputFile:
            
            outputFile.write(content)
        
        print(f"Contents of '{sourceFileName}' have been successfully copied to '{destinationFileName}'.")

    except FileNotFoundError:
        print(f"Error: The file '{sourceFileName}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 
if __name__ == "__main__":
    copyfile()
