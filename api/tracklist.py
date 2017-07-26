@app.route('/tracklist', methods = ['GET'])
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
