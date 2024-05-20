#!/bin/bash
echo "getting down the containers"
sudo docker container stop frontend
sudo docker contaiener rm -f frontend
sudo docker rmi -f akanksha2501/frontend:latest
