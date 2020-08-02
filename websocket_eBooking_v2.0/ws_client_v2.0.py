import asyncio
import websockets
import ssl

ssl_context = ssl._create_unverified_context()

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000" 
  return cpuserial

def OpenDoor():
    print('The door is open.')

def CloseDoor():
    print('The door is closed.')

async def connect_wss():
    url = "wss://localhost:8080"
    async with websockets.connect(url, ssl=ssl_context) as websocket:
        await websocket.send(getserial())
        recv = await websocket.recv()
        print(recv)
        while True:
            order = await websocket.recv()
            if order == getserial() + ' open':
                OpenDoor()
            elif order == getserial() + ' close':
                CloseDoor()
            else :
                print('Invalid order received.')

asyncio.get_event_loop().run_until_complete(connect_wss())