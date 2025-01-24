import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
    path = entry.get()
    files = os.listdir(path)
    
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]
        
        if os.path.exists(os.path.join(path, extension)):
            shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
        else:
            os.makedirs(os.path.join(path, extension))
            shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
            
    messagebox.showinfo("Success", "Files organized successfully!")

def browse_path():
    path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, path)

root = tk.Tk()
root.title("File Organizer")

label = tk.Label(root, text="Enter Path:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_path)
browse_button.pack()

organize_button = tk.Button(root, text="Organize Files", command=organize_files)
organize_button.pack()

root.mainloop()
