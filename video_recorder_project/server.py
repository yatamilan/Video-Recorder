from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('users.txt', 'r') as f:
            users = f.readlines()
        for user in users:
            stored_user, stored_pass = user.strip().split(',')
            if username == stored_user and password == stored_pass:
                return redirect('/dashboard')
        return "Invalid credentials. Try again!"
    return render_template('login.html')

# Route for signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('users.txt', 'a') as f:
            f.write(f"{username},{password}\n")
        return redirect('/login')
    return render_template('signup.html')

# Other pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/website')
def website():
    return render_template('website.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/recorder')
def recorder():
    return render_template('recorder.html')

@app.route('/recordings')
def recordings():
    return render_template('recordings.html')

if __name__ == '__main__':
    app.run(debug=True)
