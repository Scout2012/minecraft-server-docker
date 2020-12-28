docker volume create minecraft-server-world
docker volume create minecraft-server-config

docker build -t minecraft-server .

docker run -d -p 25565:25565 -v minecraft-server-world:/minecraft-server/world -v minecraft-server-config:/minecraft-server/config minecraft-server