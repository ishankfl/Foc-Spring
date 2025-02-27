import os

# Change working directory
os.chdir('C://Users//Dell//Desktop//Foc//')

# Ensure the base path is correctly set
base_path = "C://Users//Dell//Desktop//Foc//"

for each in range(1, 10):
    folder_name = f'Week{each}'
    folder_path = os.path.join(base_path, folder_name)
    
    # Create the main folder if it does not exist
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # Create subd  irectories inside the main folder
    os.mkdir(os.path.join(folder_path, 'Workshop'))
    os.mkdir(os.path.join(folder_path, 'Tutorial'))
