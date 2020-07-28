const WebSocket = require('ws');

const wss = new WebSocket.Server({
  port: 12730,
  perMessageDeflate: {
    zlibDeflateOptions: {
      chunkSize: 1024,
      memLevel: 7,
      level: 3
    },
    zlibInflateOptions: {
      chunkSize: 10 * 1024
    },
    clientNoContextTakeover: true,
    serverNoContextTakeover: true,
    serverMaxWindowBits: 10,
    concurrencyLimit: 10,
    threshold: 1024
  }
});

console.log('Server listen on: ' + 12730)

var latches = [];
var latchesID = [];
 
wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
    latchesID.push(message)
    // sendSomeData(message)
  });
  ws.send('Connected to JS server. Listening:')
  latches.push(ws)
});

function sendSomeData(UUID){
    for(latch in latchesID){
      if(latchesID[latch] === UUID){
        latches[latch].send(UUID + ' open door !')
      }
    }
}

wss.on('close', function deconnection(ws){
    ws.on('message', function incoming(message){
        console.log('received: %s', message);
    })
    ws.send('Bye!')
})
