# https://dopeldev.sbs index page site
from flask import Flask, render_template, send_from_directory

index = Flask(__name__)

services = ['Chat', 'Cloud', 'Jitsi', 'Minecraft', 'Mumble', 'Nextcloud', 'OpenVPN']

@index.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

@index.route('/')
def index_page(services = services):
    return render_template('index.html', services=services)

if __name__ == '__main__':
    index.run(debug=True)
