from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__, template_folder="temps")

@auth.route('/login', methods=['GET', 'POST'])
def login():
      return render_template("login.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
      if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')

            if len(password1) < 8:
                  flash('Password must be at least 8 characters', category='error')
            elif password1 != password2:
                  flash('Passwords do not match', category='error')
            elif len(username) < 4:
                  flash('Username must be at least 4 characters', category='error')
            elif len(email) < 3:
                  flash('Email too short', category='error')
            else:
                  flash('Account created successfully', category='success')

      return render_template("signup.html")



@auth.route('/logout')
def logout():
      return render_template("logout.html")