#!/home/chris/.virtualenvs/carputer/bin/python
from flask import Flask
from api import playlist

app = Flask(__name__)
app.register_blueprint(playlist, url_prefix = '/playlists')

if __name__ == '__main__':
	app.run(debug=True)
