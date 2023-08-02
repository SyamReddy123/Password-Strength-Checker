from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    result = subprocess.run(['python', 'password_strength.py'], capture_output=True, text=True)
    output = result.stdout
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run()
