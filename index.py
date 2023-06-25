# https://dopeldev.sbs index page site
from flask import Flask, render_template

index = Flask(__name__)

services = ['Chat', 'Cloud', 'Jitsi', 'Minecraft', 'Mumble', 'Nextcloud', 'OpenVPN']

@index.route('/')
def index_page(services = services):
    return render_template('index.html', services=services)

if __name__ == '__main__':
    index.run(debug=True)
