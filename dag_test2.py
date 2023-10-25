from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define default_args for your DAG
default_args = {
    'owner': 'admin',
    'start_date': datetime(2023, 10, 23),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create an instance of the DAG
dag = DAG(
    'my_data_pipeline_2',
    default_args=default_args,
    description='Data pipeline for collecting and analyzing data from Mastodon',
    schedule_interval=timedelta(minutes=2),  # Updated to run every 2 minutes
    catchup=False,
)

# Define tasks in your DAG
# Task to run the Mapper script
run_mapper = BashOperator(
    task_id='run_mapper_task',
    bash_command="python3 /home/hadoop/python/get_data.py",  # Updated command
    dag=dag,
)

# Task to run the Reducer script
run_reducer = BashOperator(
    task_id='run_reducer_task',
    bash_command="python3 /home/hadoop/python/global_mappreduce.py",  # Updated command
    dag=dag,
)

# Set task dependencies
run_mapper >> run_reducer

if __name__ == "__main__":
    dag.cli()

