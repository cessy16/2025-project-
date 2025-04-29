from flask import Flask, render_template 
from hashlib import *;
## 

## the instances that Flask creates, are used to 
## manage the outes (URL triggers)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dominican')
def dominican_recipe():
    return render_template('DominicanRecipe.html')

@app.route('/ecuadorian')
def ecuadorian_recipe():
    return render_template('EcuadorianRecipe.html')

@app.route('/contact')
def contact():
    return render_template('Userlogin.html')

if __name__ == '__main__':
    app.run(debug = True)
