import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Image Transformer")

# Create a label to display the image
image_label = tk.Label(window)
image_label.pack()

# Create a function to apply the transformation
def apply_transform(transform):
  # Load the image
  image = Image.open(file_path)
  
  # Apply the transformation
  transformed_image = transform(image)
  
  # Convert the image to a PhotoImage object
  image = ImageTk.PhotoImage(transformed_image)
  
  # Update the label with the new image
  image_label.config(image=image)
  image_label.image = image

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

# Create buttons to apply the transformations
invert_button = tk.Button(window, text="Invert", command=lambda: apply_transform(Image.invert))
invert_button.pack()

rotate_button = tk.Button(window, text="Rotate 90°", command=lambda: apply_transform(Image.rotate))
rotate_button.pack()

# Run the main loop
window.mainloop()

