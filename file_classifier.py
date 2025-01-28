import os
import shutil

def organize_images_by_label(source_folder, max_images=5000):
    # Create subfolders (0 to 5) in the source folder
    for label in range(6):
        label_folder = os.path.join(source_folder, str(label))
        os.makedirs(label_folder, exist_ok=True)

    count = 0
    for filename in os.listdir(source_folder):
        if count >= max_images:
            break

        # Full file path
        file_path = os.path.join(source_folder, filename)

        # Skip directories
        if os.path.isfile(file_path):
            # Remove file extension to get the core filename
            core_filename, _ = os.path.splitext(filename)

            # Ensure filename length is valid
            if len(core_filename) >= 2:
                label = core_filename[-2]  # Second last character of the core filename
                print(f"Second last character of {filename}: {label}")

                # Check if the label is a valid digit (0-5)
                if label.isdigit() and int(label) in range(6):
                    # Move the file to the respective folder
                    destination_folder = os.path.join(source_folder, label)
                    print(f"Moving {filename} to {destination_folder}")
                    shutil.move(file_path, destination_folder)
                    count += 1
                else:
                    print(f"Skipping {filename}: Second last character '{label}' is not between 0 and 5.")
            else:
                print(f"Skipping {filename}: Filename too short.")

    print(f"Processed {count} images and organized them into subfolders.")

# Example usage
source_folder = r"D:\AARUSH\finger_gesture_datasets\test"  # Your path as a raw string
organize_images_by_label(source_folder, max_images=5000)
