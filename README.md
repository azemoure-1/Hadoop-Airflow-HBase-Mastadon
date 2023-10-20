# Hadoop, Airflow, Mapper, Reducer, and HBase Setup Guide

This repository provides step-by-step instructions for setting up Hadoop, Apache Airflow, Mapper, Reducer, and HBase on WSL2 (Ubuntu). 

## Hadoop Installation and Configuration

1. To install Hadoop, visit the [Hadoop releases page](https://hadoop.apache.org/releases.html).
2. Download Hadoop version 3.2.4 (binary) using the following command:
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz


![3](https://github.com/azemoure-1/Hadoop-Airflow-HBase-Mastadon/assets/113553607/599687b3-339e-40c5-8e5a-e815862e6c95)


![4](https://github.com/azemoure-1/Hadoop-Airflow-HBase-Mastadon/assets/113553607/b22eecec-5eb4-4593-bd9a-fae4c1e3a185)


# Data Collection

In this section, we'll walk you through the process of collecting data from the Mastodon API and saving it directly to HDFS. We'll be using a Python script for this purpose.

## Prerequisites

Before you begin, make sure you have the following prerequisites in place:

- Python installed on your system.
- Access tokens for the Mastodon API.
- HDFS set up and running.

## Data Collection Script

We've provided a Python script in this repository that collects data from the Mastodon API and stores it in HDFS. You can find the script in the `get_data.py` folder.


### Running the Script

Follow these steps to run the data collection script:

1. Open a terminal and navigate to the `/usr/data/` folder (in my case).
2. Execute the script with the following command:
    ````
    python3 get_data.py
    ````

   ![2](https://github.com/azemoure-1/Hadoop-Airflow-HBase-Mastadon/assets/113553607/a68e5b53-8b0f-4df5-af47-f7ec1362c1cd)


# MapReduce Processing

In this section, we'll discuss the MapReduce processing for different axes of analysis. For each analysis, we've created separate Mapper and Reducer Python scripts. Here are the scripts and instructions on how to run them using Hadoop streaming.

## User Analysis

**Mapper:** `user_following_mapper.py`

**Reducer:** `user_following_reducer.py`


![5](https://github.com/azemoure-1/Hadoop-Airflow-HBase-Mastadon/assets/113553607/242cb621-bc43-4132-b568-8abf91e964c1)


## Content Analysis

**Mapper:** `user_content_mapper.py`

**Reducer:** `user_content_reducer.py`



### Running User Analysis

To perform user analysis, follow these steps:

1. Execute the following Hadoop streaming command, replacing the paths with your actual file paths and script locations:

   ```bash
   hadoop jar /path/to/hadoop-streaming-2.7.3.jar -input /input/data.json -output /output/user_analysis -mapper /path/to/user_following_mapper.py -reducer /path/to/user_following_reducer.py


# Apache Airflow Installation

In this section, you'll find a script that consolidates the steps for installing Apache Airflow. This script will create a virtual environment, install Apache Airflow, initialize the database, start the Airflow web server and scheduler, and provide access to the web interface.

## Prerequisites

Before running this script, make sure you have the following prerequisites in place:

- Python installed on your system (recommended version).
- Python package manager (pip) installed.

    ```bash
    # Create a Virtual Environment
    python -m venv airflow-env

## Activate the Virtual Environment
source airflow-env/bin/activate

## On Windows:
    airflow-env\Scripts\activate

## Install Apache Airflow
    pip install apache-airflow

## Initialize the Airflow Database
    airflow initdb

## Start the Airflow Web Server and Scheduler
    airflow webserver -p 8080

## In a separate terminal:
    airflow scheduler

## Access the Airflow Web Interface
### Open a web browser and go to http://localhost:8080


# HBase Installation and Configuration

In this section, you'll find a script that consolidates the steps for installing and configuring HBase, a critical component for data storage in your pipeline.

## Prerequisites

Before running this script, make sure you have the following prerequisites in place:

- Java Development Kit (JDK) installed (recommended version).
- Hadoop set up and running, as HBase relies on Hadoop's HDFS for storage.


### Download HBase (Example: HBase version 2.4.6)
    ```bash
    wget https://archive.apache.org/dist/hbase/2.4.6/hbase-2.4.6-bin.tar.gz

### Extract HBase Archive
    tar -xvf hbase-2.4.6-bin.tar.gz

### Set HBase Configuration
#### Edit the HBase configuration file 'hbase-site.xml' in the 'conf' directory with your desired settings.

#### Start HBase
    /path/to/hbase-2.4.6/bin/start-hbase.sh

### Access HBase Shell
    /path/to/hbase-2.4.6/bin/hbase shell

### HBase Web UI
#### Open a web browser and go to http://localhost:16010 to access the HBase Web UI.

### Table Creation
#### Use the HBase shell or a preferred client to create tables and define schemas for your data storage.



**Note:** Each section in this guide will have its own detailed instructions and configuration steps. Please navigate to the respective folders/files for more information on setting up these components.

---

*Disclaimer: This repository is a simplified overview of the installation and configuration process for the mentioned components. For a more in-depth understanding and troubleshooting, please refer to official documentation and community resources.*

**Contributors:** AZEMOUR Amine

**Date:** 20/10/2023
