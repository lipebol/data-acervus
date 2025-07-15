### Never send your "passwords" in Production ###

FROM azul/zulu-openjdk:17
ENV SPARK_VERSION=4.0.0 \
    SPARK_HOME=/usr/local/spark \
    PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH \
    PATH=$SPARK_HOME/bin:$PATH
RUN apt update && apt upgrade -y && apt autoremove -y && \
    apt install -y wget python3 python3-pip --no-install-recommends
RUN wget -c \
    https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz
RUN tar -xzf spark-$SPARK_VERSION-bin-hadoop3.tgz && \
    mv spark-$SPARK_VERSION-bin-hadoop3 /usr/local/spark && \
    rm -rf spark-$SPARK_VERSION-bin-hadoop3
RUN pip install pyspark