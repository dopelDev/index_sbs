# https://dopeldev.sbs index page site
from flask import Flask, render_template

index = Flask(__name__)

@index.route('/')
def index_page():
    return render_template('index.html')

if __name__ == '__main__':
    index.run(debug=True)
