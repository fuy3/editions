import os
import re

def batch_rename_images(folder_path):
    for root, _, files in os.walk(folder_path):
        image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        if not image_files:
            continue  # Skip folders without image files
        
        # Sort the image files based on numbers in their names
        image_files = sorted(image_files, key=lambda x: int(re.sub('\D', '', x)))

        # Get the number of digits needed for zero-padding
        num_digits = len(str(len(image_files)))

        for index, file_name in enumerate(image_files):
            # Get the file extension
            file_ext = os.path.splitext(file_name)[1]

            # Generate the new file name with zero-padded index
            new_file_name = f"{index + 1:0{num_digits}d}{file_ext}"
            
            # Generate new file paths
            old_file_path = os.path.join(root, file_name)
            new_file_path = os.path.join(root, new_file_name)

            # Perform the renaming operation
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {file_name} to {new_file_name}")

# Specify the folder path for renaming images
folder_path = './111'  # Replace with your folder path

# Execute the batch renaming operation
batch_rename_images(folder_path)




