"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Response, request
from FEBE import app
from roboclaw import RoboClaw


@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/update_sliderl",methods=["GET", "POST"])
def update_speedl():
    if request.method == "POST":
        #left_slider = request.form["sliderl"]
        left_slider = request.data
        move(1, left_slider)
@app.route("/update_sliderr",methods=["GET", "POST"])
def update_speedr():
    if request.method == "POST":
       #right_slider = request.form["sliderr"]
       right_slider = request.data
       move(2, right_slider)


# Backend.py part. Was supposed to place it in Backend.py, but it fails to find it. CBA.

import cv2

camera = cv2.VideoCapture('http://admin:admin@10.40.121.187:8081/video')


def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'


def move(motor, slider_value):
    address_hex = 0x80
    roboclaw = RoboClaw(port='COM11', address=address_hex)
    if motor == 1:
        roboclaw.drive_motor(motor, int(slider_value))
    if motor == 2:
        roboclaw.drive_motor(2, int(slider_value))
    pass
