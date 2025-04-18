from flask import Flask, render_template 
from hashlib import *;
## 

## the instances that Flask creates, are used to 
## manage the outes (URL triggers)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')

if __name__ == '__main__':
    app.run(debug = True)
