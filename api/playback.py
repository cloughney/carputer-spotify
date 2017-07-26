from flask import Blueprint, jsonify, request, abort

playback_api = Blueprint('playback_api', __name__)

def command_play():
	print('play!')

valid_commands = {
	'play': command_play
}

@playback_api.route('/', methods = ['POST'])
def play():
	if not request.json or not 'command' in request.json:
		abort(400)

	command = valid_commands
	if command == None:
		abort(400)

	command()
