FROM openjdk:11

RUN  apt-get update
EXPOSE 25565/tcp
EXPOSE 25565/udp

WORKDIR /minecraft-server

COPY ./mc/server.jar /minecraft-server
COPY ./mc/eula.txt /minecraft-server

CMD java -Xmx1024M -Xms1024M -jar server.jar nogui