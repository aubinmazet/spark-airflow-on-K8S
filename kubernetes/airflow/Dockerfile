FROM apache/airflow:2.1.2-python3.8
ARG AIRFLOW_HOME=/opt/airflow
USER root
RUN  apt-get update -y && apt-get install -y \
    procps \
    vim \
    git
RUN pip install --upgrade pip && pip install 'apache-airflow-providers-apache-spark'
RUN chown -R airflow:airflow ${AIRFLOW_HOME}
USER airflow
EXPOSE 8080