import os
import shutil

def organize_images_by_label(source_folder, max_images=5000):
    # Create subfolders (0 to 5) in the source folder
    for label in range(6):  # Create folders for 0, 1, 2, 3, 4, 5
        label_folder = os.path.join(source_folder, str(label))
        os.makedirs(label_folder, exist_ok=True)

    # Process images in the source folder
    count = 0
    for filename in os.listdir(source_folder):
        if count >= max_images:
            break

        # Skip directories, only process files
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            # Get the second last character from the filename
            if len(filename) >= 2:  # Ensure the filename is long enough
                label = filename[-2]
                # Check if it's a digit between 0 and 5
                if label.isdigit() and int(label) in range(6):
                    # Move the file to the respective folder
                    destination_folder = os.path.join(source_folder, label)
                    shutil.move(file_path, destination_folder)
                    count += 1

    print(f"Processed {count} images and organized them into subfolders.")

# Example usage
source_folder = r"D:\AARUSH\finger_gesture_datasets\train"  # Replace with the path to your folder
organize_images_by_label(source_folder, max_images=5000)
