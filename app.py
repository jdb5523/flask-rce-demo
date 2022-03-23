from flask import Flask, render_template, request
from dotenv import load_dotenv
import subprocess
import re


app = Flask(__name__)

load_dotenv()


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        selected_year = request.form['years']
    else:
        selected_year = '2022'

    pattern  = "\d{4}"
    match = re.search(pattern, selected_year)
    if not match or selected_year == '0000':
        selected_year = '2022'
    
    try:
        cal = subprocess.check_output(['cal', selected_year]).decode('ascii')
    except:
        cal = subprocess.check_output(['cal', '2022']).decode('ascii')

    return render_template('index.html', cal=cal)

app.run(port=5500)