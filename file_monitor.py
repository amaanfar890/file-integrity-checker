import hashlib
import os
import time

def calculate_hash(filepath, hash_function=hashlib.sha256):
  """Calculates the hash of a file."""
  try:
    with open(filepath, "rb") as f: # Open in binary mode
      file_hash = hash_function()
      while chunk := f.read(8192): # Read in chunks to handle large files
        file_hash.update(chunk)
    return file_hash.hexdigest()
  except FileNotFoundError:
    return None  # Handle file not found

def monitor_files(filepaths, interval=60):
  """Monitors files for changes at a given interval."""
  initial_hashes = {}
  for filepath in filepaths:
    initial_hashes[filepath] = calculate_hash(filepath)

  print("Monitoring files...")
  while True:
    time.sleep(interval) # Wait for the interval
    for filepath in filepaths:
      current_hash = calculate_hash(filepath)
      if current_hash is None:
        print(f"File not found: {filepath}")
        continue
      if current_hash != initial_hashes[filepath]:
        print(f"File changed: {filepath}")
        print(f"  Old hash: {initial_hashes[filepath]}")
        print(f"  New hash: {current_hash}")
        initial_hashes[filepath] = current_hash # Update the stored hash

# Example usage
files_to_monitor = ["myfile.txt", "important_config.ini", "my_script.py"]
monitor_files(files_to_monitor, interval=10) # Check every 10 seconds