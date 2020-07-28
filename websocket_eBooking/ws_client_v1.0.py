import asyncio
import websockets
import sys

async def hello():
    url = "ws://localhost:12730"
    async with websockets.connect(url) as websocket:
        await websocket.send(sys.argv[1])
        recv = await websocket.recv()
        print(recv)
        while True:
            print(await websocket.recv())

if len(sys.argv) > 1:
    asyncio.get_event_loop().run_until_complete(hello())
# asyncio.get_event_loop().run_forever()

