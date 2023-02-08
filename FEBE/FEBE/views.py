"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Response
from FEBE import app
import cv2

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
camera = cv2.VideoCapture('http://admin:admin@10.40.120.104:8081/video')
def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route("/sliderl", methods=["POST"])
def sliderl():
    left_slider = request.form["left_slider"]
    return left_slider
app.route("/sliderr", methods=["POST"])
def sliderr():
    right_slider = request.form["right_slider"]
    return right_slider