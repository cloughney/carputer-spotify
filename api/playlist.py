from flask import Blueprint, jsonify

playlist_api = Blueprint('playlist_api', __name__)

@playlist_api.route('/', methods = ['GET'])
def get_playlists():
	return jsonify({
		'playlists': []
	})
