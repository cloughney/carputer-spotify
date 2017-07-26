from flask import Blueprint, jsonify

tracklist_api = Blueprint('tracklist_api', __name__)

@tracklist_api.route('/', methods = ['GET'])
def get_tracklist():
	return jsonify({
			'tracklist': {
				'tracks': [
					{
						'id': 1,
						'title': 'Blah'
					}
				]
			}
		})
