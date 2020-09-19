all: build run

# Get the local timezone
TZ:=$(shell timedatectl | grep "Time zone" | sed "s/ *Time zone: //;s/ (.*, .*)//")

build:
	docker build -t ibmosquito/clock:1.0.0 -f Dockerfile .

dev: build stop
	-docker rm -f clock 2> /dev/null || :
	docker run -it --privileged -e TZ=$(TZ) --name clock --volume `pwd`:/outside ibmosquito/clock:1.0.0 /bin/bash

run: stop
	-docker rm -f clock 2>/dev/null || :
	docker run -d --restart=unless-stopped --privileged -e TZ=$(TZ) --name clock ibmosquito/clock:1.0.0

exec:
	docker exec -it clock /bin/sh

push:
	docker push ibmosquito/clock:1.0.0

stop:
	-docker rm -f clock 2>/dev/null || :

clean: stop
	-docker rmi ibmosquito/clock:1.0.0 2>/dev/null || :

.PHONY: all build dev run exec push stop clean
