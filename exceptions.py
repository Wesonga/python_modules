try:
    # Attempting to open a file that might not exist
    with open("missing_file.txt", "r") as file:
        print(file.read())
        
except FileNotFoundError:
    print("Oops! That file could not be found. Please check the filename.")
    
else:
    print("File read successfully!")
    
finally:
    print("Execution complete. Cleaning up resources.")