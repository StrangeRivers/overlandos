import sys
import time
from Phidget22.Devices.Spatial import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
from fusion.fusion import Fusion

fuse = Fusion()

def SpatialAttached(e):
    try:
        attached = e
        attached.setDataInterval(50)

        print("\nAttach Event Detected (Information Below)")
        print("===========================================")
        print("Library Version: %s" % attached.getLibraryVersion())
        print("Serial Number: %d" % attached.getDeviceSerialNumber())
        print("Channel: %d" % attached.getChannel())
        print("Channel Class: %s" % attached.getChannelClass())
        print("Channel Name: %s" % attached.getChannelName())
        print("Device ID: %d" % attached.getDeviceID())
        print("Device Version: %d" % attached.getDeviceVersion())
        print("Device Name: %s" % attached.getDeviceName())
        print("Device Class: %d" % attached.getDeviceClass())
        print("\n")

    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)

def SpatialDetached(e):
    detached = e
    try:
        print("\nDetach event on Port %d Channel %d" % (detached.getHubPort(), detached.getChannel()))
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)

def ErrorEvent(e, eCode, description):
    print("Error %i : %s" % (eCode, description))

def SpatialDataHandler(e, acceleration, angularRate, fieldStrength, timestamp):
#     print("Acceleration  : %7.3f  %8.3f  %8.3f" % (acceleration[0], acceleration[1], acceleration[2]))
#     print("Angular Rate  : %7.3f  %8.3f  %8.3f" % (angularRate[0], angularRate[1], angularRate[2]))
#     print("Field Strength: %7.3f  %8.3f  %8.3f" % (fieldStrength[0], fieldStrength[1], fieldStrength[2]))
#     print("Timestamp: %f\n" % timestamp)
    global pitch
    global roll
    global heading
    fuse.update((acceleration[0], acceleration[1], acceleration[2]), (angularRate[0], angularRate[1], angularRate[2]), (fieldStrength[0], fieldStrength[1], fieldStrength[2]))
    pitch = fuse.pitch
    roll = fuse.roll
    heading = fuse.heading
    print(pitch, roll, heading)
