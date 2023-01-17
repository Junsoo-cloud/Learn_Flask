from flask import Flask, render_template, url_for
import sys
app = Flask(__name__)

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

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=int(sys.argv[1]))
