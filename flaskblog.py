from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import sys 
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd6e2fcf20403bfea892f8ad76d455690'


posts = [
  {
    'author': 'Junsoo',
    'title': 'Blog Post1',
    'content': 'First post content',
    'date_posted': 'April 20, 2020'
  },
  
  { 
    
    'autor': 'seung wu',
    'title': 'Blog Post2',
    'content': 'Second post content',
    'data_posted': 'April 22, 2020' 
  } 
  
  
    
]

@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html',posts = posts)
  
@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm() # Create Instance
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') 
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm() # Create Instance
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in !', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger') # Bootstrap -> danger : Red Alert
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    



# Part 3 - Forms and User Input : WT forms
