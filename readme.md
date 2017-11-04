# OverlandOS
A really cool project to bring a custom sensor dashboard to my 2001 Tacoma via a modern IoT delivery toolchain: Docker, Resin.io, Electron, Node, and maybe React. All running on Raspberry Pi!

## To run locally
Build the project with Docker
```bash
$ sudo docker build -t overlandos-server .```

Then run with USB ports mapped through. Probably better to do this without privileged mode sometime when I stabilize the hardware configuration
```bash
sudo docker run -t -i --privileged -v /dev/usb:/dev/usb overlandos-server bash```

From within the terminal `run python3 data-server.py` and you should see IMU values start streaming

Websockets resource: https://websockets.readthedocs.io/en/stable/intro.html#
