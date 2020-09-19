FROM raspbian/stretch

# Install tzdata (for timezone) pip3
RUN apt update && apt install -y tzdata python3-pip

# Install the HT16K33 support library
RUN pip3 install adafruit-circuitpython-ht16k33

# Copy over the clock daemon source
COPY clock.py /
WORKDIR /

# Run the clock daemon
CMD python3 clock.py

