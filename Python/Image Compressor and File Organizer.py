import os
import shutil
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def compress_image(input_path, output_path, quality=85):
    """
    Compresses an image and saves it to the specified output path.

    Parameters:
        input_path (str): Path to the input image.
        output_path (str): Path to save the compressed image.
        quality (int): Compression quality (1 to 95). Higher means better quality but larger size.
    """
    try:
        img = Image.open(input_path)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.save(output_path, "JPEG", optimize=True, quality=quality)
    except Exception as e:
        print(f"An error occurred while compressing {input_path}: {e}")

def organize_files(path):
    """
    Organizes files in the specified directory into subfolders by their extensions
    and compresses image files.

    Parameters:
        path (str): Path to the directory to organize.
    """
    if not os.path.isdir(path):
        print(f"The specified path does not exist: {path}")
        return

    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            filename, extension = os.path.splitext(file)
            extension = extension[1:]  # Remove the dot

            if not extension:
                continue

            target_folder = os.path.join(path, extension)
            os.makedirs(target_folder, exist_ok=True)

            target_path = os.path.join(target_folder, file)
            shutil.move(file_path, target_path)

            # Compress image files
            if extension.lower() in ["jpg", "jpeg", "png"]:
                compressed_file = os.path.join(target_folder, f"compressed_{file}")
                compress_image(target_path, compressed_file, quality=70)

    print("Files organized and images compressed successfully!")

def browse_and_compress():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if not file_path:
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Files", "*.jpg")])
    if not output_path:
        return

    compress_image(file_path, output_path, quality=70)
    messagebox.showinfo("Success", "Image compressed and saved successfully!")

def browse_and_organize():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    organize_files(folder_path)
    messagebox.showinfo("Success", "Files organized successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Organizer and Image Compressor")

    label = tk.Label(root, text="Choose an action:")
    label.pack(pady=10)

    compress_button = tk.Button(root, text="Compress Image", command=browse_and_compress)
    compress_button.pack(pady=5)

    organize_button = tk.Button(root, text="Organize Files", command=browse_and_organize)
    organize_button.pack(pady=5)

    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.pack(pady=10)

    root.mainloop()
