import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def process_m4b(input_file):
    # Check if the input file exists
    if not os.path.exists(input_file):
        print("Input file does not exist.")
        return

    # Get the directory and filename of the input file
    directory = os.path.dirname(input_file)
    filename = os.path.basename(input_file)
    filename_no_extension, extension = os.path.splitext(filename)

    # Define the output filename
    output_filename = os.path.join(directory, f"{filename_no_extension}_remuxed{extension}")

    # Run FFmpeg to process the file
    try:
        subprocess.run(['ffmpeg', '-i', input_file, '-map', '0:a', '-map', '0:v', '-c', 'copy', output_filename], check=True)
        print("File remuxed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error remuxing file:", e)

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(filetypes=[("M4B files", "*.m4b")])
    if file_path:
        process_m4b(file_path)

if __name__ == "__main__":
    open_file_dialog()
