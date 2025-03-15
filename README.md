# file-integrity-checker
 A Python-based tool that monitors specified files for unauthorized modifications by detecting changes in their cryptographic hash values.

## Features

* **Real-time File Monitoring:** Continuously checks files for changes.
* **SHA256 Hashing:** Uses a secure hashing algorithm to detect modifications.
* **Simple Configuration:** Easily add or remove files to monitor.
* **Command-Line Output:** Provides clear alerts when changes are detected.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Usage

1. Clone the Repository:** If you're viewing this on GitHub, you can clone the repository to your local machine:

    ```bash
    git clone https://github.com/amaanfar890/file-integrity-checker.git
    ```

2.  Place Files: Ensure the files you wish to monitor are in the same directory as the `file_monitor.py` script.
3.  Run the Script: Open your command line or terminal, navigate to the directory where the script is located, and run:

    ```bash
    python file_monitor.py
    ```

4.  Monitoring: The script will continuously monitor the files at a defined interval (default is 60 seconds).
5.  Changes Detected: If a file is modified, the script will print a message to the console with the old and new hash values.

### Configuring Monitored Files

To add or remove files from the monitoring list:

1.  Open the `file_monitor.py` script in a text editor.
2.  Locate the `files_to_monitor` list:

    ```python
    files_to_monitor = ["myfile.txt", "important_config.ini"] # Add or remove files here
    ```

3.  Modify the list by adding or removing file names (strings).
4.  Save the script.

### Example Output

If `myfile.txt` is changed, the script might output something like this:

File changed: myfile.txt
Old hash: f29bc64a9d3732b4b9035125fdb3285f5b6455778edca72414671e0ca3b2e0de
New hash: c6caa69a1dd061c76a987d67e1c1795b8440ce1b98b19f933c56b8f0e4ff5ec5

# Contact:
Email: faroquiamaan@gmail.com
