
# Author: Ajanthan

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
from flask import send_from_directory, render_template

import os
import glob

import model


# Create a basic flask app.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mosfet'  # You should probably change this to a random value!
# Add the DHT data model to the app config so templates can reach it and query
# the sensors & readings.
app.config['MODEL'] = model.DHTData()

# Add an admin view for the Peewee ORM-based DHT sensor and sensor reading models.
admin = Admin(app, name='Sound Sensors', template_mode='bootstrap3', url='/')
admin.add_view(ModelView(model.DHTSensor))
admin.add_view(ModelView(model.SensorReading))


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join("/home/pi/RaspberryPI/AD-DA/python/recorded_audio")
    return send_from_directory(directory=uploads, filename=filename)


@app.route('/sound', methods=['GET'])
def get_sound():
    files = glob.glob("/home/pi//RaspberryPI/AD-DA/python/recorded_audio/*.wav")
    file_names = []
    image_names = []
    for f in files:
        file_names.append(os.path.basename(f))
    images = glob.glob("/home/pi/RaspberryPI/AD-DA/python/recorded_audio/*.png")
    for i in images:
        image_names.append(os.path.basename(i))
    file_names.sort()
    image_names.sort()
    final_result=[]
    for i, f in enumerate(file_names):
        try:
            imag_name = image_names[i]
        except:
            imag_name = ''
        data = {'audio': f, 'image': imag_name}
        final_result.append(data)
    print(final_result)
    return render_template("admin/dropdown.html", sounds=final_result)


if __name__ == "__main__":
    app.run(debug=True)