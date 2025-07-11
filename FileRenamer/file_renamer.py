import os

folder_path = "C:/Users/MNNNW/OneDrive/Desktop/main_folder"
count = 1

try:
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
    else:
        files = os.listdir(folder_path)

        if not files:
            print("Folder is empty.")
        else:
            for file in files:
                old_file = os.path.join(folder_path, file)

                if not os.path.isfile(old_file):
                    print(f"Skipping {file} (not a file)")
                    continue

                extension = os.path.splitext(file)[1]

                new_name = f"Khushi_{count}{extension}"
                new_file = os.path.join(folder_path, new_name)

                try:
                    os.rename(old_file, new_file)
                    print(f"Renamed: {file} → {new_name}")
                    count += 1
                except Exception as e:
                    print(f"Error renaming {file}: {e}")

except Exception as e:
    print(f"Unexpected error occurred: {e}")

