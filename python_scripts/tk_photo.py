import tkinter as tk
import os

# Create the main window
window = tk.Tk()
window.title("Take Photo")

# Create a button that will trigger the camera to take a photo
def take_photo():
    # Take a photo using the device's camera
    os.system('ffmpeg -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:2 -frames 1 /home/abari/out.jpg')

button = tk.Button(text="Take Photo", command=take_photo)
button.pack()

# Run the Tkinter event loop
window.mainloop()