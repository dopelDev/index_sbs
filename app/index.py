# https://dopeldev.sbs index page site
from typing import List
from flask import Flask, render_template, send_from_directory
from pathlib import Path

BASE_DIR = Path(__name__).parent.absolute()
index = Flask(__name__)

services = ['Chat', 'Cloud', 'Jitsi', 'Humble', 'Nextcloud', 'OpenVPN']

@index.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

@index.route('.well-known/acme-challenge/<path:filename>')
def acme_challenge(filename):
    path = BASE_DIR / 'cert' / '.well-known' / 'acme-challenge'
    return send_from_directory(path, filename)

@index.route('/')
def index_page(services = services):
    return render_template('index.html', services=services)

if __name__ == '__main__':
    index.run(debug=True)
