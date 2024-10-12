import sys
import os
import yaml

os.system(f"echo 'dependencies resolved'")

# os.system(f"conda init")
# os.system(f"conda activate snowpark")
directory_path= sys.argv[1]

os.chdir(f"{directory_path}")
# Make sure all 6 SNOWFLAKE_ environment variables are set
# SnowCLI accesses the passowrd directly from the SNOWFLAKE_PASSWORD environmnet variable
os.system(f"snow snowpark build")
os.system(f"echo 'build done'")
os.system(f'snow snowpark deploy --replace --temporary-connection --account "lwfhzmy-dev_accountt" --user "inzamam" --role "ACCOUNTADMIN" --warehouse "COMPUTE_WH" --database "DEMO_DB" --password "Inzamam@123456"')  