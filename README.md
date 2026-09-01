# Screenshot Organizer 🖥️✨

## Description
A lightweight and smart Python automation script that keeps your macOS Desktop clean and organized. It automatically scans your Desktop for screenshots and screen recordings and moves them into a dedicated `Screenshot_organizer` folder, saving you time and decluttering your workspace.

## Key Features
- **Automatic Desktop Detection:** Dynamically finds the user's Desktop path using `os.path.expanduser`, making it work for any Mac user.
- **Intelligent File Filtering:** Detects all macOS screenshot formats by name, including `Screenshot`, and `Screen Recording`.
- **Safe Organization:** Automatically creates the `Screenshot_organizer` destination folder if it doesn't already exist.
- **Prevents Infinite Loops:** Includes smart logic to skip the destination folder itself to avoid errors.
- **User Feedback:** Provides a real-time log in the console of every file moved and a final summary with the total count.

## Technologies Used
- **Python 3**
- **os** - For path manipulation and file system interaction
- **shutil** - For high-level file moving operations

## How to Run
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/edo-800/Screenshot_organizer.git
    cd Screenshot_organizer
    ```

2.  **Run the script:**
    Make sure you have Python 3 installed. Then run the script from your terminal:
    ```bash
    python3 main.py
    ```
    The script will scan your Desktop and automatically organize your screenshots into the `~/Desktop/Screenshot_organizer/` folder.

    > **Note:** You can automate this script to run at startup or at regular intervals using macOS Automator or `crontab` for a permanently clean Desktop.

## Author
Created by an aspiring Full-Stack Software Engineer as part of a long-term portfolio for Top Tech companies.
