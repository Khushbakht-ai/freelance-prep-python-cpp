import os
import shutil

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
                file_path = os.path.join(folder_path, file)

                if not os.path.isfile(file_path):
                    continue

                extension = os.path.splitext(file)[1].lower()

                if not extension:
                    extension = "no_extension"
                else:
                    extension = extension[1:]

                target_folder = os.path.join(folder_path, extension)
                os.makedirs(target_folder, exist_ok=True)

                new_location = os.path.join(target_folder, file)

                try:
                    shutil.move(file_path, new_location)
                    print(f"Moved: {file} → {extension}/")
                except Exception as e:
                    print(f"Error moving {file}: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
