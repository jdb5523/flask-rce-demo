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
        selected_year = 2022

    command = f'cal {selected_year}'
    cal = subprocess.check_output(command, shell=True).decode('ascii')

    return render_template('index.html', cal=cal)

app.run(port=5500)