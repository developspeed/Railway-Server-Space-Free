import os
import time

directory = "/path/to/directory"  # Replace with your directory path
days_threshold = 1  # Files older than this number of days will be deleted

# Get the current time in seconds
current_time = time.time()

# Get a list of all files in the directory
file_list = os.listdir(directory)

# Iterate over the files and delete the ones older than the threshold
for file_name in file_list:
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        # Get the last modified time of the file
        last_modified = os.path.getmtime(file_path)
        # Calculate the number of days since the file was last modified
        days_diff = (current_time - last_modified) / (24 * 60 * 60)
        if days_diff > days_threshold:
            os.remove(file_path)
            print(f"Deleted file: {file_name}")

print("All files older than the threshold have been deleted.")