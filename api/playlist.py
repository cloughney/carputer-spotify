from flask import Blueprint, jsonify

playlist = Blueprint('playlist', __name__)

@playlist.route('/', methods = ['GET'])
def get_playlists():
	return jsonify({
		'playlists': []
	})
