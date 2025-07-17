import os

folder_path = "PUT_YOUR_FOLDER_PATH_HERE"

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

                name_only, extension = os.path.splitext(file)
                cleaned_name = name_only.replace(" ", "_").replace("(", "").replace(")", "")
                new_file = os.path.join(folder_path, cleaned_name + extension)

                try:
                    os.rename(old_file, new_file)
                    print(f"Renamed: {file} → {cleaned_name + extension}")
                except Exception as e:
                    print(f"Error renaming {file}: {e}")

except Exception as e:
    print(f"Unexpected error occurred: {e}")
