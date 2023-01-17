from flask import Flask, render_template, url_for
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

@app.route("/register")
def register():
    form = RegistrationForm() # Create Instance
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm() # Create Instance
    return render_template('login.html', title='Login', form=form)

print(len(sys.argv))
try: 
    print(sys.argv[1]) 
except IndexError: 
    print("No command-line argument provided") 

arg = sys.argv[1] if len(sys.argv) > 1 else "default value" 
print(type(sys.argv[0]))
print(sys.argv[0])
sys.argv.append(80)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
    



# Part 3 - Forms and User Input : WT forms
