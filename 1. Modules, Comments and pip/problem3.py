# print contents of a directory using OS module
import os

def print_directory_contents(directory):
    try:
        # Get the list of all files and directories
        contents = os.listdir(directory)
        
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"The directory '{directory}' was not found.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = "."  # Current directory
print_directory_contents(directory_path)
