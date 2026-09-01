import os
import shutil

# 1. Automatically finds the Mac user's Desktop path.
phat_desktop = os.path.expanduser("~/Desktop")

# 2. Define the folder where the screenshots are located and the folder to move them to.
source_folder = phat_desktop
destination_folder = os.path.join(phat_desktop, "Screenshot_organizer")

# 3. Create the "screenshot" folder on the Desktop if it doesn't already exist.
os.makedirs(destination_folder, exist_ok=True)

# 4. Let's read all the files on the Desktop.
all_file = os.listdir(source_folder)

print("Scanning desktop...")
moved_counter = 0

# 5. We check the files one by one.
for single_file in all_file:
    
    # If the file we are examining is our folder, or contains the name of the destination folder, SKIP IT!
    if single_file == "Screenshot_organizer" or single_file == "screenshot":
        continue
        
    # If it passes the check above, we apply the logic.
    if "Screenshot" in single_file or "Screen Recording" in single_file:
        
        old_position = os.path.join(source_folder, single_file)
        new_position = os.path.join(destination_folder, single_file)
        
        # Let's move the file from the Desktop to the "Screenshot_organizer" folder.
        shutil.move(old_position, new_position)
        
        print("Moved to the desktop -> Screenshot_organizer: " + single_file)
        moved_counter = moved_counter + 1

print("Cleanup complete! Moved a total of " + str(moved_counter) + " file.")
