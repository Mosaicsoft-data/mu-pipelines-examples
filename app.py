from mu_pipelines_driver.run_config import run_config
import sys

print("args are")
# Access arguments (excluding the script name itself)
job_config = "/home/scripts/raw/people.json"
connection_config = '/home/scripts/global-properties.json'
global_poperties = '/home/scripts/connection-properties.json'

#df = run_config(job_config, connection_config, global_poperties )

df = run_config(
    [
        {
            "execution": [
                {
                    "type": "CSVReadCommand",
                    "file_location": "/home/iceberg/warehouse/data/people.csv",
                    "delimiter": ",",
                    "quotes": "\"",
                    "additional_attributes": [
                        { "key": "header", "value": "True" }
                    ]
                }
            ],
            "destination": [
                {
                    "type": "table",
                    "connection": "iceberg-lakehouse",
                    "table_name": "crm.raw.people",
                    "mode": "overwrite"
                }
            ]
        }
    ],
    {
        "library": "spark"
    },
    {
        "connections":[]
    }
) 