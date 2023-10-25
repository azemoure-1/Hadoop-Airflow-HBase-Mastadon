# Hadoop, Airflow, Mapper, Reducer, and HBase Setup Guide

This repository provides step-by-step instructions for setting up Hadoop, Apache Airflow, Mapper, Reducer, and HBase on Ubuntu. 

# RGPD :
Garantir le respect du règlement général sur la protection des données (RGPD) est primordial lors du traitement des données personnelles au sein du pipeline de données Mastodon. Ce document décrit les principales étapes prises pour adhérer à la réglementation GDPR, démontrant notre engagement à protéger les données personnelles et à respecter le droit à la vie privée des individus.
Étapes clés pour la conformité au RGPD
Anonymisation des données :

Les informations personnelles jouent un rôle essentiel dans la conformité au RGPD. Afin de répondre aux exigences du RGPD, toutes les données personnelles non pertinentes pour l'analyse sont soit supprimées, soit hachées avant traitement. Cette procédure garantit que les informations personnelles sensibles restent protégées tout au long du pipeline de données.

### Minimisation des données :

Seules les données nécessaires à l'analyse sont conservées, tandis que toute information superflue ou non pertinente est supprimée afin de minimiser l'exposition des données et d'atténuer les risques potentiels pour la vie privée.

### Mesures de sécurité:

Notre pipeline de données utilise des mesures de sécurité robustes pour protéger les données. Les systèmes de stockage HDFS et HBase sont sécurisés pour empêcher tout accès non autorisé. Des contrôles d'accès, des mécanismes de cryptage et d'authentification sont mis en œuvre pour protéger les données au repos, garantissant ainsi une sécurité complète des données.

### Gestion des lacs de données :

Pour réduire les risques de rétention des données, une politique stricte est en place pour supprimer les données du lac de données une fois qu'elles ont été traitées. Cette pratique aligne la conservation des données strictement sur les finalités du traitement des données telles que spécifiées dans le RGPD.

### Évaluation d’impact sur la protection des données (DPIA) :

Une DPIA est menée pour identifier et atténuer les risques potentiels en matière de confidentialité au sein du pipeline de données. Cette évaluation aide à prendre des décisions éclairées concernant les pratiques et les garanties de traitement des données.

### Gestion du consentement :

Le cas échéant, les activités de traitement des données ne sont menées qu'après avoir obtenu le consentement explicite des personnes concernées, comme l'exige le RGPD. Les enregistrements de consentement sont conservés et gérés avec diligence.

### Droits des personnes concernées :

Des mécanismes sont établis pour respecter les droits des personnes concernées tels que définis par le RGPD. Cela inclut de fournir aux personnes concernées la possibilité d'accéder, de corriger ou de supprimer leurs données personnelles sur demande.

### Documentation et dossiers de conformité :

Une documentation détaillée des activités de traitement des données, des garanties et des mesures de conformité est systématiquement conservée. Cette documentation garantit la transparence et la responsabilité en cas d’enquêtes réglementaires.

### Audits et contrôles de conformité réguliers :

Des audits réguliers sont effectués pour vérifier le respect cohérent des mesures de conformité au RGPD tout au long du pipeline de données. Cela implique de s'assurer que le pipeline est conforme à toute modification ou mise à jour de la réglementation GDPR.

### Réponse aux violations de données :

Un protocole bien défini est établi pour répondre rapidement à toute violation de données conformément aux exigences du RGPD. Les personnes concernées et les autorités de contrôle sont informées si nécessaire.


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
