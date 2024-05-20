#!/bin/bash
echo "starting our new containers"
sudo docker container run -d --name=frontend -p 5000:5000 akanksha2501/frontend:latest
sudo docker container ps 
echo "Containers are running now ..................."
