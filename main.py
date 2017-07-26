#!/home/chris/.virtualenvs/carputer/bin/python
from flask import Flask
from api import playlist_api, tracklist_api

app = Flask(__name__)
app.register_blueprint(playlist_api, url_prefix = '/playlists')
app.register_blueprint(tracklist_api, url_prefix = '/tracklist')

if __name__ == '__main__':
	app.run(debug=True)
