#!/bin/bash

docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)

docker run --name foam_pet_1 -td -e HOST_IP=host.docker.internal -p 22000:22000 -p 21000:21000 -p 443:443 -p 80:80 foam_pet:v1_3_0.0 /bin/bash -c "bash /embark.sh"