# minecraft-server-docker
A Docker container for a vanilla Minecraft server.

There are a few helper scripts located in the scripts folder to help make things easier for building/running this docker container. They are not very customizable as of now in terms of options, but it helps if you are new to Docker and you just want to get something running.

The scripts and their uses are as followed:
* first_time_setup.sh --> creates docker volumes, builds the docker image, and runs the docker container
* build_volumes.sh --> creates the docker volumes that will be used for saving the server's world and config files
* build.sh --> builds the docker image and names it **minecraft-server**
* run.sh --> runs the **minecraft-server** image in a new container

Please run all scripts in the root folder (the folder you cloned/downloaded) 
e.g.`sh scripts/first_time_setup.sh`
