import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Image Viewer")

# Create a label to display the image
image_label = tk.Label(window)
image_label.pack()

# Create a button to open the file selector
def select_image():
  # Open the file selector
  file_path = filedialog.askopenfilename()
  
  # Load the image
  image = Image.open(file_path)
  image = image.resize((300, 300), Image.ANTIALIAS)
  image = ImageTk.PhotoImage(image)
  
  # Update the label with the new image
  image_label.config(image=image)
  image_label.image = image

select_button = tk.Button(window, text="Select Image", command=select_image)
select_button.pack()

# Run the main loop
window.mainloop()