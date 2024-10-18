import os

def list_files_in_folder(folder_path):
    try:
        # Get the list of all files in the specified folder
        files = os.listdir(folder_path)
        
        # Count the number of files
        file_count = len(files)
        
        # Return the list of files and the count
        return files, file_count
    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' does not exist.")
        return [], 0
    except PermissionError:
        print(f"Error: Permission denied to access the folder '{folder_path}'.")
        return [], 0
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return [], 0

# Example usage
folder_path = "./asserts/Pre_Wedding_Shoot"  # Replace this with the actual path to your folder
file_list, file_count = list_files_in_folder(folder_path)

# Print the list of files and the count
print("Files in the folder:")
print(file_list)
print(f"Total number of files: {file_count}")
