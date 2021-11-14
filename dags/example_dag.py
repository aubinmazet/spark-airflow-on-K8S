from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from datetime import datetime, timedelta

default_args = {
    'start_date': datetime.utcnow()
}
with DAG("kube-example", default_args=default_args) as dag:
    spark_submit = KubernetesPodOperator(namespace="airflow", pod_template_file="spark-driver-pod.yml")