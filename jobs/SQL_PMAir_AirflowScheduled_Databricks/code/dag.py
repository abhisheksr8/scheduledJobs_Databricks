import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from ikfrx_6ozuy9or_t_9w2w_.tasks import Model_0
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "iKfrx_6ozUY9OR_T_9w2w_", 
    schedule_interval = "*/5 9-10 5 5 *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "yfn3jbcR"}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2034, 9, 17, tz = "UTC"), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    Model_0_op = Model_0()
