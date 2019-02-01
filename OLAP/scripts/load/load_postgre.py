import subprocess
from time import time
name_list = [
    "region",
    "nation",
    "supplier",
    "part",
    "customer",
    "partsupp",
    "orders",
    "lineitem",
]
print(time())
for name in name_list:
    print(name)
    command = "psql -d tpch -c \"copy "+name+" from \'/clean/"+name+".tbl\' delimiter \'|\';\""
    subprocess.run(command, shell=True)
print(time())
