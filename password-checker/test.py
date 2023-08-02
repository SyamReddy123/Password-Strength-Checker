from flask import Flask, render_template, request
import math
import random
import string

app = Flask(_name_)

def crack_time(password):
    characters = 0
    if any(c.isdigit() for c in password):
        characters += 10
    if any(c.isalpha() for c in password):
        characters += 26
    if any(c.islower() for c in password):
        characters += 26
    if any(c.isupper() for c in password):
        characters += 26
    if any(c.isalnum() for c in password):
        characters += 26

    possibilities = characters ** len(password)
    crack_seconds = possibilities / 1000  # Assuming 1000 attempts per second
    crack_time = crack_seconds / 60 / 60 / 24 / 365  # In years
    return crack_time

def calculate_entropy(password):
    characters = 0
    if any(c.isdigit() for c in password):
        characters += 10
    if any(c.isalpha() for c in password):
        characters += 26
    if any(c.islower() for c in password):
        characters += 26
    if any(c.isupper() for c in password):
        characters += 26
    if any(c.isalnum() for c in password):
        characters += 26

    entropy = math.log2(characters) * len(password)
    return entropy

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form.get('password')

        password_length = len(password) if password else 0

        if password_length > 0:
            strength = "Weak"
            if password_length >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
                strength = "Strong"

            crack_time_years = crack_time(password)
            crack_time_str = f"{math.ceil(crack_time_years)} years"

            entropy = calculate_entropy(password)
            entropy_str = f"{entropy:.2f} bits"

            return render_template('result.html', password=password, strength=strength, crack_time=crack_time_str, entropy=entropy_str)

    return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)