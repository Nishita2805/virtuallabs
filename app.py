from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    displacement = float(request.form['displacement'])
    distance_GB = float(request.form['distance_GB'])
    angle_tilt = float(request.form['angle_tilt'])
    
    angle_radians = math.radians(angle_tilt)
    GM = displacement / (distance_GB * math.tan(angle_radians))
    
    return render_template('result.html', GM=GM)

if __name__ == '__main__':
    app.run(debug=True)
