from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
from flask import Flask, render_template,request,jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'
CORS(app)
@app.route("/", methods=["GET"])
def index_get():
    return render_template("login.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json(force=True).get("message")
# text = request.is_json().get("message")
# text = "hi"
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'project'
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the MySQL database
        cur = mysql.connection.cursor()

        # Check if the username and password match the records in the users table
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()

        if user:
            session['username'] = username
            return redirect('/dashboard')
        else:
            error_message = 'Invalid username or password. Please try again.'
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')



@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if 'username' in session:
        username = session['username']

        # Connect to the MySQL database
        cur = mysql.connection.cursor()

        # Fetch additional user details from the users table
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()

        # Pass the user details to the template
        return render_template('base.html', username=username, user=user)
    else:
        return redirect('/')
# @app.route('/profile')
# def profile():
#     if 'username' in session:
#         username = session['username']
#         return render_template('profile.html')
#     else:
#         return redirect('/')
# def fetch_details():
#     cursor = mysql.connection.cursor()
#     cursor.execute("SELECT * FROM details")
#     details = cursor.fetchall()
#     cursor.close()
#     return details



@app.route('/page2')
def page2():
    # Check if the user is logged in
    if 'username' in session:
        username = session['username']

        # Connect to the MySQL database
        cur = mysql.connection.cursor()

        # Fetch additional user details from the users table
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()

        # Pass the user details to the template
        return render_template('page2.html', username=username, user=user)
    else:
        return redirect('/')


@app.route('/yoga')
def yoga():
    # Check if the user is logged in
    if 'username' in session:
        username = session['username']

        # Connect to the MySQL database
        cur = mysql.connection.cursor()

        # Fetch additional user details from the users table
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()

        # Pass the user details to the template
        return render_template('yoga.html', username=username, user=user)
    else:
        return redirect('/')
    
@app.route('/ex')
def ex():
    # Check if the user is logged in
    if 'username' in session:
        username = session['username']

        # Connect to the MySQL database
        cur = mysql.connection.cursor()

        # Fetch additional user details from the users table
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()

        # Pass the user details to the template
        return render_template('ex.html', username=username, user=user)
    else:
        return redirect('/')
    
@app.route('/fd')
def fd():
    # Check if the user is logged in
    if 'username' in session:
        username = session['username']

        # Connect to the MySQL database
        cur = mysql.connection.cursor()

        # Fetch additional user details from the users table
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()

        # Pass the user details to the template
        return render_template('fd.html', username=username, user=user)
    else:
        return redirect('/')
@app.route('/rv')
def rv():
    # Check if the user is logged in
    if 'username' in session:
        username = session['username']

        # Connect to the MySQL database
        cur = mysql.connection.cursor()

        # Fetch additional user details from the users table
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()

        # Pass the user details to the template
        return render_template('review.html', username=username, user=user)
    else:
        return redirect('/')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the MySQL database
        cur = mysql.connection.cursor()

        # Check if the username already exists in the users table
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()

        if user:
            error_message = 'Username already exists. Please choose a different username.'
            return render_template('signup.html', error_message=error_message)

        # Insert the username and password into the users table
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()

        session['username'] = username
        return render_template('login.html', registration_successful=True)

    return render_template('login.html')
@app.route('/contact', methods=['POST'])
def submit_contact_form():
    message = request.form['message']
    
    # Create a cursor object to execute SQL queries
    cur = mysql.connection.cursor()
    
    # Insert the submitted data into the database
    cur.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
    
    # Commit the transaction and close the cursor
    mysql.connection.commit()
    cur.close()
    # flash('Tq feedback submitted successfully!')
    return redirect('/show_alert')

# @app.route('/base')
# def base_page():
#     return render_template('base.html')
@app.route('/show_alert')
def show_alert():
    return render_template('alert.html')



@app.route('/logout')
def logout():
    # Clear the session and redirect to the login page
    session.clear()
    return redirect('/')


if __name__ =='__main__':
    app.run(host='127.0.0.1',debug=True)