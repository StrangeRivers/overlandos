FROM python:3.6-jessie

WORKDIR /app

RUN apt-get update && apt-get install -y libusb-1.0-0-dev

RUN wget https://www.phidgets.com/downloads/phidget22/libraries/linux/libphidget22/libphidget22-1.0.0.20170818.tar.gz \
  && tar zxvf libphidget22-1.0.0.20170818.tar.gz \
  && ./libphidget22-1.0.0.20170818/configure --prefix=/usr\
  && make -j8 \
  && make install \
  && cp plat/linux/udev/99-libphidget22.rules /etc/udev/rules.d

RUN mkdir /app/Phidget22Python
COPY Phidget22Python app/Phidget22Python
WORKDIR app/Phidget22Python
RUN python3 setup.py install

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

EXPOSE 5678

CMD ["python3", "data-server.py"]
