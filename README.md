# Hadoop, Airflow, Mapper, Reducer, and HBase Setup Guide

This repository provides step-by-step instructions for setting up Hadoop, Apache Airflow, Mapper, Reducer, and HBase on WSL2 (Ubuntu). 

## Hadoop Installation and Configuration

1. To install Hadoop, visit the [Hadoop releases page](https://hadoop.apache.org/releases.html).
2. Download Hadoop version 3.2.4 (binary) using the following command:
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz

# Data Collection

In this section, we'll walk you through the process of collecting data from the Mastodon API and saving it directly to HDFS. We'll be using a Python script for this purpose.

## Prerequisites

Before you begin, make sure you have the following prerequisites in place:

- Python installed on your system.
- Access tokens for the Mastodon API.
- HDFS set up and running.

## Data Collection Script

We've provided a Python script in this repository that collects data from the Mastodon API and stores it in HDFS. You can find the script in the `data_collection` folder.

### Running the Script

Follow these steps to run the data collection script:

1. Open a terminal and navigate to the `/usr/data/` folder (in my case).
2. Execute the script with the following command:
    ````
    python3 get_data.py
    ````

## Airflow Installation

Instructions for installing Apache Airflow.

## Mapper and Reducer

This section provides details on setting up the Mapper and Reducer components for your data processing pipeline.

## HBase Installation and Configuration

Instructions for installing and configuring HBase for data storage.

**Note:** Each section in this guide will have its own detailed instructions and configuration steps. Please navigate to the respective folders/files for more information on setting up these components.

---

*Disclaimer: This repository is a simplified overview of the installation and configuration process for the mentioned components. For a more in-depth understanding and troubleshooting, please refer to official documentation and community resources.*

**Contributors:** AZEMOUR Amine

**Date:** 20/10/2023