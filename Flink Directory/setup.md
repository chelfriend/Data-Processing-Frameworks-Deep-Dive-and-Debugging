# Apache Flink Setup Guide

## Prerequisites

- Java Development Kit (JDK) 8+
- Apache Maven

## Installation

1. Download and extract Apache Flink:
    ```sh
    wget https://downloads.apache.org/flink/flink-1.13.2/bin/flink-1.13.2-bin-scala_2.11.tgz
    tar -xzf flink-1.13.2-bin-scala_2.11.tgz
    ```

2. Set up Flink:
    ```sh
    cd flink-1.13.2
    ./bin/start-cluster.sh
    ```

3. Build the Flink project using Maven:
    ```sh
    mvn clean package
    ```

## Running the Pipeline

Submit the Flink job to the cluster:
```sh
./bin/flink run target/wordcount-0.1.jar
