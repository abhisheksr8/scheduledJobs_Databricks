from ikfrx_6ozuy9or_t_9w2w_.utils import *

def Model_0():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "Model_0",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": True,
          "run_deps": False,
          "run_seeds": True,
          "run_parents": False,
          "run_children": False,
          "run_tests": True,
          "run_mode": "project",
          "entity_kind": None,
          "entity_name": None,
          "project_id": "15772",
          "git_entity": "branch",
          "git_entity_value": "main",
          "git_ssh_url": "https://github.com/abhisheksr8/scheduledJobs_Databricks.git",
          "git_sub_path": "",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": " --profile run_profile",
          "envs": {
            "DBT_DATABRICKS_INVOCATION_ENV": "prophecy", 
            "DBT_SEND_ANONYMOUS_USAGE_STATS": "false", 
            "DBT_FULL_REFRESH": "true"
          }, 
          "git_token_secret": "xmPlILCkDn7Gwnwn9ks6Pw_", 
          "dbt_profile_secret": "FHLS_orKxQSz2sjtrAx7z"
        },
    )
