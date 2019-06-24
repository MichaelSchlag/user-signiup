from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#global_username = ''
#global_email = ''


@app.route("/")
def index():
    return render_template('signup.html', title="User Signup")


@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    confirm_password_error = ''
    email_error = ''

    if username == '':
        username_error = 'Please enter a username'
    elif " " in username:
        username_error = "No spaces"
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters long"

    if password == '':
        password_error = 'Please enter a password'
    elif " " in password:
        password_error = "No spaces"
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters long"

    if confirm_password == '':
        confirm_password_error = 'Please confirm your password'
    elif " " in confirm_password:
        confirm_password_error = "No spaces"
    elif not confirm_password == password:
        confirm_password_error = "Password doesn't match"

    if not email == '':
        if not '@' in email or not '.' in email or len(email) < 3 or len(email) > 20:
            email_error = "Email must be between 3 and 20 characters and contain a '@' and '.'"
        elif " " in email:
            email_error = "No spaces"

    if not username_error and not password_error and not confirm_password_error and not email_error:
        return redirect("/welcome?username="+ username)
    else:
        return render_template('signup.html',
            keep_username =  username,
            keep_email = email,
            username_error = username_error,
            password_error = password_error,
            confirm_error = confirm_password_error,
            email_error = email_error)


@app.route("/welcome", methods=['GET'])
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)

app.run()