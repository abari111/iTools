
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/take_photo', methods=['POST'])
def take_photo():
    # Take a photo using the device's camera
    os.system('ffmpeg -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:2 -frames 1 /home/abari/out.jpg')
    return 'Photo saved!'

if __name__ == '__main__':
    app.run()
