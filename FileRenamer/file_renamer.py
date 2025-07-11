import os

folder_path = "C:/Users/MNNNW/OneDrive/Desktop/main_folder"

files = os.listdir(folder_path)
count = 1

for file in files:
    old_file = os.path.join(folder_path, file)
    extension = os.path.splitext(file)[1]
    new_name = f"Khushi_{count}{extension}"
    new_file = os.path.join(folder_path, new_name)
    os.rename(old_file, new_file)
    count += 1
