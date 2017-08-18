#!/usr/bin/env python

import asyncio
import time
import random
import websockets
import json
import Spatial
from Phidget22.PhidgetException import *

try:
    ch = Spatial.Spatial()
except RuntimeError as e:
    print("Runtime Exception %s" % e.details)
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)
    
try:
    ch.setOnAttachHandler(Spatial.SpatialAttached)
    ch.setOnDetachHandler(Spatial.SpatialDetached)
    ch.setOnErrorHandler(Spatial.ErrorEvent)

    ch.setOnSpatialDataHandler(Spatial.SpatialDataHandler)

    print("Waiting for the Phidget Spatial Object to be attached...")
    ch.openWaitForAttachment(10000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

async def JSON_sender(websocket, path):
	while True:
		payload = json.dumps({ 'pitch' : Spatial.pitch , 'roll' : Spatial.roll, 'heading' : Spatial.heading})
		await websocket.send(payload)
		await asyncio.sleep(0.050)

start_server = websockets.serve(JSON_sender, '127.0.0.1', 5678)

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
