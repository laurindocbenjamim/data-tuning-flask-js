
import os

# Check if the directory exists, if not, create it
def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        

def create_file(file_path):    
    # check if the file exist, if not, create it
    if not os.path.exists(file_path):
        # Create the file
        with open(file_path, 'w') as file:
            file.write('# THIS IS A LOG FILE \n')