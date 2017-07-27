#!/home/chris/.virtualenvs/car/bin/python
import asyncio
import websockets
import json

async def on_connect(socket):
	await socket.send(json.dumps({
		'test': 'test'
	}))

async def listen():
	async with websockets.connect('ws://localhost:3000') as socket:
		await on_connect(socket)
		while True:
			message = await socket.recv()
			print(message)

asyncio.get_event_loop().run_until_complete(listen())
