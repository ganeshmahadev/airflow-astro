from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import  datetime

#define the tasks
def pre_process():
    print("preprocessing data")

def train():
    print("training model")

def evaluate_model():
    print("evalute the model")

#define DAG
with DAG(
    'ml_pipeline',
    start_schedule=datetime(2024,1,1),
    schedule_interval='@weekly',
    catchup=False

) as dag: 

#define task
    preprocess=PythonOperator(task_id='preprocessing', python_callable=pre_process)
    trainmodel=PythonOperator(task_id='trainig',python_callable=train)
    evaluate=PythonOperator(task_id='evaluating', python_callable=evaluate_model)

    #set order
    pre_process >> train >> evaluate_model

