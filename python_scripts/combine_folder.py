import os
import shutil
import tkinter as tk
from tkinter import filedialog


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        # Create widgets
        self.folder_selector_1 = tk.Button(self, text='Select Folder 1', command=self.select_folder_1)
        self.folder_selector_2 = tk.Button(self, text='Select Folder 2', command=self.select_folder_2)
        self.combine_button = tk.Button(self, text='Combine Folders', command=self.combine_folders)
        self.combine_button.config(state='disabled')

        # Add widgets to the layout
        self.folder_selector_1.pack()
        self.folder_selector_2.pack()
        self.combine_button.pack()

        # Set window properties
        self.title('Folder Combiner')
        self.geometry('300x100')

    def select_folder_1(self):
        """Open a file dialog and select the first folder."""
        folder_1 = filedialog.askdirectory()
        if folder_1:
            self.folder_1 = folder_1
            self.folder_selector_1.config(text=folder_1)
            self.combine_button.config(state='normal')

    def select_folder_2(self):
        """Open a file dialog and select the second folder."""
        folder_2 = filedialog.askdirectory()
        if folder_2:
            self.folder_2 = folder_2
            self.folder_selector_2.config(text=folder_2)
            self.combine_button.config(state='normal')

    
    def combine_folders(self):
        """Combine the two selected folders."""
        for root, dirs, files in os.walk(self.folder_1):
            for file in files:
                src = os.path.join(root, file)
                dst = os.path.join(self.folder_2, file)
                shutil.copy(src, dst)
        tk.messagebox.showinfo('Success', 'Folders combined successfully!')


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
