import os
import shutil
import datetime
import schedule
import time

# Define your source and destination directories
source_dir = "/path/to/source"  # Replace with your source folder path
destination_dir = "/path/to/destination"  # Replace with your destination folder path

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Schedule the task to run daily at 18:10
schedule.every().day.at("23:02").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# Run the schedule loop
while True:
    schedule.run_pending()
    time.sleep(60)
