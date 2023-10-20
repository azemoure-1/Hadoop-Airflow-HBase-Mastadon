## ***Hadoop*** *Installation & Configuration on WSL2 (ubuntu)*
> To install Hadoop, follow the [link](https://hadoop.apache.org/releases.html). In my case, I'm using Hadoop version 3.2.4 (binary).
[Download Hadoop 3.2.4](https://dlcdn.apache.org/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz)

To download Hadoop 3.2.4, click the link above or use the following command:

    ```bash
    wget https://dlcdn.apache.org/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz
    ```

    ```bash
    sudo apt update 
    sudo apt upgrade
    sudo vim
    ```
After you've set up the WSL environment, make sure to install the dependencies :
    ``` bash
    sudo apt-get update
    sudo apt-get install -y openssh-client openssh-server vim ssh -y
    sudo apt install openjdk-8-jdk openjdk-8-jre
    ```
Open .bashrc file
    ```bash
    sudo vim ~/.bashrc
    ```
    ```bash
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    export JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
    ```
If you are denied permission to save, close without saving, run the code below, and then repeat the above steps.
    ```bash
    sudo chown -R jane ~/.bashrc
    ```
Now that you have completed the Bash configuration, it's time to install the Hadoop file you downloaded.

Decompress the file using the command below:
    ```bash
    tar -xzf hadoop-3.2.4.tar.gz
    ```
Make sure you rename the file to 'hadoop' using the command below:
    ```bash
    sudo mv hadoop-3.2.4 hadoop
    ```
Now, move Hadoop to the '/usr/local' path:
    ```bash
    sudo mv hadoop /usr/local
    ```
The command sets read, write, and execute permissions (777) for all users on the :
    ```bash
    sudo chmod 777 /usr/local/hadoop
    ```
Open the file:
    ```bash
    code ~/.bashrc
    ```
Sets environment variables for Hadoop:
    ```bash
    export HADOOP_HOME=/usr/local/hadoop
    export HADOOP_INSTALL=$HADOOP_HOME
    export HADOOP_MAPRED_HOME=$HADOOP_HOME
    export HADOOP_COMMON_HOME=$HADOOP_HOME
    export HADOOP_HDFS_HOME=$HADOOP_HOME
    export HADOOP_YARN_HOME=$HADOOP_HOME
    export YARN_HOME=$HADOOP_HOME
    export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
    export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
    ```
Reload the changes made above and create directories for HDFS, including the Namenode, Datanode, and logs (Jane, replace 'my user' with your username.):
    ```bash
    source ~/.bashrc
    mkdir -p /home/jane/hdfs/namenode
    mkdir -p /home/jane/hdfs/datanode
    mkdir $HADOOP_HOME/logs
    ```
To edit series HFDS configuration files, change directory to the folder and open hadoop-env.sh:
    ```bash
    cd $HADOOP_HOME/etc/hadoop
    sudo vim hadoop-env.sh
    ```
Sets the environment variable JAVA_HOME to the path where Java Development Kit (JDK) version 8 is installed (save and close the file)
    ```bash
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    ```
In the same path, edit core-site.xml:
    ```bash
    sudo vim core-site.xml
    ```
    ```bash
    <configuration>
     <property>
     <name>fs.defaultFS</name>
     <value>hdfs://localhost:9000/</value>
     </property>
    </configuration>
    ```
Edit hdfs-site.xml:
    ```bash
    sudo vim hdfs-site.xml
    ```
    ```bash
    <configuration>
     <property>
     <name>dfs.namenode.name.dir</name>
     <value>file:///home/jane/hdfs/namenode</value>
     <description>NameNode directory for namespace and transaction logs storage.</description>
     </property>
     <property>
     <name>dfs.datanode.data.dir</name>
     <value>file:///home/jane/hdfs/datanode</value>
     <description>DataNode directory</description>
     </property>
     <property>
     <name>dfs.replication</name>
     <value>1</value>
     </property>
    </configuration>
    ```

Edit mapred-site.xml:
    ```bash
    sudo vim mapred-site.xml
    ```
    ```bash
    <configuration>
     <property>
     <name>mapreduce.framework.name</name>
     <value>yarn</value>
     </property>
     <property>
     <name>yarn.app.mapreduce.am.env</name>
     <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
     </property>
     <property>
     <name>mapreduce.map.env</name>
     <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
     </property>
     <property>
     <name>mapreduce.reduce.env</name>
     <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
     </property>
    </configuration>
    ```
Edit yarn-site.xml:
    ```bash
    sudo vim yarn-site.xml
    ```
    ```bash
    <configuration>
     <property>
     <name>yarn.nodemanager.aux-services</name>
     <value>mapreduce_shuffle</value>
     </property>
     <property>
     <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
     <value>org.apache.hadoop.mapred.ShuffleHandler</value>
     </property>
     <property>
     <name>yarn.resourcemanager.hostname</name>
     <value>localhost</value>
     </property>
    </configuration>
    ```
Generate ssh key and add to authorized keys in Ubuntu:
    ```bash
    cd ~
    ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
    chmod 600 ~/.ssh/authorized_keys
    ```
Open these 2 files:
    ```bash
    sudo vim /etc/ssh/ssh_config
    ```
    ```bash
    Port 22
    ```
Do the same for the other file:
    ```bash
    sudo vim /etc/ssh/sshd_config
    ```
    ```bash
    port 22
    ```
    
    ```bash
    sudo vim ~/.ssh/config
    ```
(save and exit.)
    ```bash
    Host *
     StrictHostKeyChecking no
    ```
Prepare Namenode for HDFS and restart ssh service:
    
    ```bash
    hdfs namenode -format
    sudo /etc/init.d/ssh restart
    ```
Finally Start hadoop by command:


    ```bash
    start-dfs.sh
    start-yarn.sh
    ```
Now, ensure that all these services are started successfully:
    ```bash
    jps
    ```
Result:
    ```bash
    1456 NodeManager
    560 NameNode
    1137 ResourceManager
    38072 Jps
    910 SecondaryNameNode
    719 DataNode
    ```
Check the version of the website at 'localhost:9870':
    ```bash
    localhost:9870
    ```
try to create folder in hdfs :
    ```bash
    #create new directory 
    hdfs dfs -mkdir /temp
    #show to folder
    hdfs dfs -ls /

![6](https://github.com/azemoure-1/Hadoop-Airflow-HBase-Mastadon/assets/113553607/9f85dddc-11ad-4017-92db-61ce157f6b4b)



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
## Open a web browser and go to http://localhost:8080


# HBase Installation and Configuration

In this section, you'll find a script that consolidates the steps for installing and configuring HBase, a critical component for data storage in your pipeline.

## Prerequisites

Before running this script, make sure you have the following prerequisites in place:

- Java Development Kit (JDK) installed (recommended version).
- Hadoop set up and running, as HBase relies on Hadoop's HDFS for storage.

    ```bash
## Download HBase
### Replace 'X.X.X' with the desired HBase version.
    wget https://archive.apache.org/dist/hbase/X.X.X/hbase-X.X.X-bin.tar.gz

### Extract HBase Archive
    tar -xvf hbase-X.X.X-bin.tar.gz

### Set HBase Configuration
Edit the HBase configuration file 'hbase-site.xml' in the 'conf' directory with your desired settings.

### Start HBase
    /path/to/hbase-X.X.X/bin/start-hbase.sh

### Access HBase Shell
    /path/to/hbase-X.X.X/bin/hbase shell

### HBase Web UI
 Open a web browser and go to http://localhost:16010 to access the HBase Web UI.

### Table Creation
 Use the HBase shell or a preferred client to create tables and define schemas for your data storage.


**Note:** Each section in this guide will have its own detailed instructions and configuration steps. Please navigate to the respective folders/files for more information on setting up these components.

---

*Disclaimer: This repository is a simplified overview of the installation and configuration process for the mentioned components. For a more in-depth understanding and troubleshooting, please refer to official documentation and community resources.*

**Contributors:** AZEMOUR Amine

**Date:** 20/10/2023
