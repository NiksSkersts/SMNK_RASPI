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
@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )
@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route("/sliderl", methods=["POST"])
def sliderl():
    left_slider = request.form["sliderl"]
    move(1, left_slider)
    return left_slider
app.route("/sliderr", methods=["POST"])
def sliderr():
    right_slider = request.form["sliderr"]
    move(2, right_slider)
    return right_slider


#Backend.py part Dunno why that shit doesn't want to work

import cv2
camera = cv2.VideoCapture('http://admin:admin@10.40.121.102:8081/video')
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
    roboclaw = RoboClaw(port='COM4',address=address_hex)
    if(motor == 1):
        roboclaw.set_speed(motor,slider_value)
    if(motor == 2):
        roboclaw.set_speed(2,slider_value)
    pass