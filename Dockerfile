FROM openjdk:11

RUN  apt-get update \
    && apt-get install python3 -y \
    && apt-get install python3-pip -y \
    && python3 -m pip install requests \
    && python3 -m pip install simplejson

EXPOSE 25565/tcp
EXPOSE 25565/udp

WORKDIR /minecraft-server

COPY ./mc/eula.txt /minecraft-server
COPY ./utils/mc_server_jar.py /minecraft-server/utils/

RUN python3 utils/mc_server_jar.py | xargs wget

CMD java -Xmx1024M -Xms1024M -jar server.jar nogui