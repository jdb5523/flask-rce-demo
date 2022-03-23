from flask import Flask, render_template, request
from dotenv import load_dotenv
import subprocess
import re


app = Flask(__name__)
load_dotenv()


@app.route('/', methods=['GET', 'POST'])
def main():
    selected_year = '2022'
    
    if request.method == 'POST':
        selected_year = request.form['years']
        
    print(selected_year)
    pattern  = r'^\d{1,4}$'
    match = re.search(pattern, selected_year)
    if not match or int(selected_year) <= 0 or int(selected_year) > 9999:
        return render_template('error.html'), 400
    
    try:
        cal = subprocess.check_output(['cal', selected_year]).decode('ascii')
        return render_template('index.html', cal=cal)
    except:
        return render_template('error.html'), 400


app.run(port=5500)