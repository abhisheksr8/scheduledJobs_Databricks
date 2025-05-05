import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from regression_abhisheks_e2etests_automation_databricks_project_airflowscheduled_sql_mwaa_airflowscheduled_databricks.tasks import (
    Model_0
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "regression_abhisheks_e2etests_Automation_Databricks_Project_AirflowScheduled_SQL_MWAA_AirflowScheduled_Databricks", 
    schedule_interval = "*/5 9-10 5 5 *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    Model_0_op = Model_0()
