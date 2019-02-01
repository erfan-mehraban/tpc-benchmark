import sys
from subprocess import Popen, DEVNULL, STDOUT
from time import time
dstat_proc = None
def run_dstat(log_path):
    global dstat_proc
    if dstat_proc is not None:
        dstat_proc.kill()
    dstat_proc = Popen([
            "dstat",
            "-lcmdrsyTt",
            "--full",
            "--output",
            log_path
        ],
        stdout=DEVNULL)

def run_test(sf, out_file_path, stat_file_path):
    temp_stat_file_handler = open(stat_file_path, "w")
    temp_stat_file_handler.close()
    with open(out_file_path, "w") as out_file_handler:
        test_proc = Popen([
            "bash",
            "run.sh",
            "client",
            str(int(2*3600)), #duration
            str(sf), #warehous
            "30", #stat interval show
            stat_file_path, #class stats file
        ],stdout=out_file_handler, stderr=STDOUT)
        test_proc.wait()

def truncate():
    trucate_query = """
    truncate table CUSTOMER;
    truncate table CUSTOMER_NAME;
    truncate table DISTRICT;
    truncate table HISTORY;
    truncate table ITEM;
    truncate table LOADER_PERMIT;
    truncate table NEW_ORDER;
    truncate table ORDERS;
    truncate table ORDER_LINE;
    truncate table RUN_PERMIT;
    truncate table STOCK;
    truncate table WAREHOUSE;
    """
    truncate_proc = Popen([
            "sqlcmd",
            "--query="+trucate_query
        ], stdout=DEVNULL)
    truncate_proc.wait()

def print_disk_memory_usage():
    proc = Popen([
        "sqlcmd",
        "--query=exec @Statistics MEMORY, 0"
    ])
    proc.wait()
    proc = Popen([
        "sqlcmd",
        "--query=exec @Statistics COMMANDLOG, 0"
    ])
    proc.wait()
    proc = Popen([
        "sqlcmd",
        "--query=exec @Statistics SNAPSHOTSTATUS, 0"
    ])
    proc.wait()

def resume_databse():
    proc = Popen([
        "voltadmin",
        "resume"
    ])
    proc.wait()

report_folder = "/root/reports/"

for sf in [1, 5, 10, 100]:
    resume_databse()
    truncate()
    print_disk_memory_usage()
    print("run test at:", time(), "by sf:", sf)
    run_dstat(report_folder + str(sf) + ".dstat")
    run_test(sf, report_folder + str(sf) + ".out", report_folder + str(sf) + ".stat")
    print("test ends at:", time())
    dstat_proc.kill()
    print_disk_memory_usage()
    print("-----------")
    sys.stdout.flush()

dstat_proc.kill()
