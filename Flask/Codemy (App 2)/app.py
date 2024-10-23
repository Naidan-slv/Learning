from flask import Flask, render_template
from Flask_wtf import FLaskForm
from wtforms import StringFIeld, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
