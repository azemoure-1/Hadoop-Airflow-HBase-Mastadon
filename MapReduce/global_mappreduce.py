#!/usr/bin/python3


import subprocess
import time
from datetime import datetime

# Get the current date in the format 'YYYY-MM-DD'
current_date = datetime.now().strftime('%Y-%m-%d')

# Define the input path with the current date
input_path = f"/Mostodon/Raw/mastodon_data_{current_date}.json"


# List of job configurations
jobs = [
    {
        "job_name": "user_content",
        "input_path": input_path,
        "output_path": "/processed_data/output/user_content",
        "mapper_script": "user_content_mapper.py",
        "reducer_script": "user_content_reducer.py",
    },
    {
        "job_name": "user_following",
        "input_path": input_path,
        "output_path": "/processed_data/output/user_following",
        "mapper_script": "user_following_mapper.py",
        "reducer_script": "user_following_reducer.py",
    },
    {
        "job_name": "user_engagement",
        "input_path": input_path,
        "output_path": "/processed_data/output",
        "mapper_script": "user_engagement_mapper.py",
        "reducer_script": "user_engagement_reducer.py",
    },
    {
       "job_name": "user_language",
        "input_path": input_path,
        "output_path": "/processed_data/output",
        "mapper_script": "user_language_mapper.py",
        "reducer_script": "user_language_reducer.py",
    },
    {
        "job_name": "user_growth",
        "input_path": input_path,
        "output_path": "/processed_data/output",
        "mapper_script": "user_growth_mapper.py",
        "reducer_script": "user_growth_reducer.py",
    },
    {
        "job_name": "user_media",
        "input_path": input_path,
        "output_path": "/processed_data/output",
        "mapper_script": "user_media_mapper.py",
        "reducer_script": "user_media_reducer.py",
    },
    {
        "job_name": "user_tags",
        "input_path": input_path,
        "output_path": "/processed_data/output",
        "mapper_script": "user_tags_mapper.py",
        "reducer_script": "user_tags_reducer.py",
    },
]

# Common Hadoop Streaming options
hadoop_streaming_jar = "/home/hadoop/Downloads/hadoop-streaming-2.7.3.jar"
common_opts = []

for job_config in jobs:
    output_path = job_config["output_path"]

    # Delete the output directory if it already exists
    subprocess.call(["hdfs", "dfs", "-rm", "-r", output_path])

    cmd = [
        "hadoop",
        "jar",
        hadoop_streaming_jar,
        "-input",
        job_config["input_path"],
        "-output",
        output_path,
        "-mapper",
        f"python3 /home/hadoop/python/{job_config['mapper_script']}",
        "-reducer",
        f"python3 /home/hadoop/python/{job_config['reducer_script']}",
    ]

    # Extend the command with common options
    cmd.extend(common_opts)

    # Execute the Hadoop Streaming job
    try:
        subprocess.check_call(cmd)
        print(f"Job for {job_config['job_name']} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running the job for {job_config['job_name']}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

print("All jobs completed.")

