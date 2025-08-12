### Never send your "passwords" in Production ###

FROM azul/zulu-openjdk:17
RUN apt update && apt upgrade -y && apt install wget apache2-utils -y
RUN wget -c https://dlcdn.apache.org/drill/1.22.0/apache-drill-1.22.0.tar.gz
RUN tar -xvzf apache-drill-1.22.0.tar.gz && mkdir -p /opt/drill/conf/ && \
    cd apache-drill-1.22.0/conf && rm -rf drill-override.conf && \
    mv * /opt/drill/conf/ && cd .. && rm -rf conf/ && mv * /opt/drill/ && \
    rm -rf /apache-drill-1.22.0
WORKDIR /opt/drill/
RUN htpasswd -nb lipebol t21Geh5sX7kP > /opt/drill/conf/htpasswd \
    && chmod 644 /opt/drill/conf/htpasswd

CMD ["bin/sqlline", "-u", "jdbc:drill:zk=local", "-n", "lipebol", "-p", "t21Geh5sX7kP"]

    